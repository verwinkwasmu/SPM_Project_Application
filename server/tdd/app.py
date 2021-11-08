from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
from sqlalchemy.sql import select
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import ClientError
import logging
import os
from werkzeug.security import generate_password_hash, check_password_hash
import mimetypes

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database-new.clbmqgt8dbzr.us-east-1.rds.amazonaws.com:3306/spm_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@123@34.133.220.175:3306/spm_google_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}
db = SQLAlchemy(app)

CORS(app)

BUCKET = "spm-grp2-storage"
S3_DOMAIN = "http://spm-grp2-storage.s3.amazonaws.com/"

s3 = boto3.client(
    "s3",
    aws_access_key_id="AKIARI6FEUPE7XJKMOLA",
    aws_secret_access_key="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"
)

class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    employeeName = db.Column(db.String(50))
    userName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    userType = db.Column(db.String(50))
    designation = db.Column(db.String(50))
    department = db.Column(db.String(50))
    

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __init__(self, userId, employeeName, userName, email, userType, designation, department):
        self.userId = userId
        self.employeeName = employeeName
        self.userName = userName
        self.email = email
        self.userType = userType
        self.designation = designation
        self.department = department

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Learner(User):
    __tablename__ = 'learner'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'learner',
    }

    def __init__(self, userId, employeeName, userName, email, userType, designation, department):
        super().__init__(userId, employeeName, userName, email, userType, designation, department)

class Trainer(User):
    __tablename__ = 'trainer'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'trainer',
    }

    def __init__(self, userId, employeeName, userName, email, userType, designation, department):
        super().__init__(userId, employeeName, userName, email, userType, designation, department)

class Hr(User):
    __tablename__ = 'hr'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'hr',
    }

    def __init__(self, userId, employeeName, userName, email, userType, designation, department):
        super().__init__(userId, employeeName, userName, email, userType, designation, department)

class Course(db.Model):
    __tablename__ = 'course'
    
    courseId = db.Column(db.String(50), primary_key=True)
    courseName = db.Column(db.String(50))
    courseDescription = db.Column(db.String(50))
    prerequisites = db.Column(db.String(50))
    courseClass = db.relationship('Class', backref='course')

    __mapper_args__ = {
        'polymorphic_identity': 'course'
    }
    
    def __init__(self, courseId, courseName, courseDescription, prerequisites):
        self.courseId = courseId
        self.courseName = courseName
        self.courseDescription = courseDescription
        self.prerequisites = prerequisites


    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Class(db.Model):
    __tablename__ = 'class'

    classId = db.Column(db.String(50), primary_key=True) #course id + course Title //XRX-101 Class 1
    courseId = db.Column(db.String(50), db.ForeignKey('course.courseId'))
    classSize = db.Column(db.Integer)
    classTitle = db.Column(db.String(50))
    startTime = db.Column(db.String(50))
    endTime = db.Column(db.String(50))
    startDate = db.Column(db.String(50))
    endDate = db.Column(db.String(50))
    enrolmentStartDate = db.Column(db.String(50))
    enrolmentEndDate = db.Column(db.String(50))
    trainerAssigned = db.Column(db.Integer, db.ForeignKey('trainer.userId')) # userId
    trainerName = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'class'
    }

    def __init__(self, classId, courseId, classSize, classTitle, startTime, endTime, startDate, endDate, enrolmentStartDate, enrolmentEndDate, trainerAssigned, trainerName):
        self.classId = classId
        self.courseId = courseId
        self.classSize = classSize
        self.classTitle = classTitle
        self.startTime = startTime
        self.endTime = endTime
        self.startDate = startDate
        self.endDate = endDate
        self.enrolmentStartDate = enrolmentStartDate
        self.enrolmentEndDate = enrolmentEndDate
        self.trainerAssigned = trainerAssigned
        self.trainerName = trainerName
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Enrolment(db.Model):
    __tablename__ = 'enrolment'

    courseId = db.Column(db.String(50), db.ForeignKey('class.courseId'))
    classId = db.Column(db.String(50), db.ForeignKey('class.classId'), primary_key=True)
    learnerId = db.Column(db.Integer, db.ForeignKey('learner.userId'), primary_key=True)
    totalNumSections = db.Column(db.Integer)
    sectionsCompleted = db.Column(db.Integer)
    completedClass = db.Column(db.Boolean)
    status = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'enrolment'
    }

    def __init__(self, courseId, classId, learnerId, totalNumSections, status, sectionsCompleted = 0, completedClass = False):
        self.courseId = courseId
        self.classId = classId
        self.learnerId = learnerId
        self.sectionsCompleted = sectionsCompleted
        self.totalNumSections = totalNumSections
        self.completedClass = completedClass
        self.status = status
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Section(db.Model):
    __tablename__ = 'section'

    sectionId = db.Column(db.String(50), primary_key=True)
    classId = db.Column(db.String(50), db.ForeignKey('class.classId'), primary_key=True)
    fileName = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'section'
    }

    def __init__(self, classId, sectionId, fileName):
        self.classId = classId
        self.sectionId = sectionId
        self.fileName = fileName

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Quiz(db.Model):
    __tablename__ = 'quiz'

    quizId = db.Column(db.String(50), primary_key=True)
    sectionId = db.Column(db.String(50), db.ForeignKey('section.sectionId'), primary_key=True)
    classId = db.Column(db.String(50), db.ForeignKey('section.classId'), primary_key=True)
    time = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'quiz'
    }

    def __init__(self, classId, sectionId, quizId, time):
        self.classId = classId
        self.sectionId = sectionId
        self.quizId = quizId
        self.time = time
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
        
    def get_time(self):
        return self.time


class Question(db.Model):
    __tablename__ = 'question'

    sectionId = db.Column(db.String(50), db.ForeignKey('quiz.sectionId'), primary_key=True)
    classId = db.Column(db.String(50), db.ForeignKey('quiz.classId'), primary_key=True)
    quizId = db.Column(db.String(50), db.ForeignKey('quiz.quizId'), primary_key=True)
    questionId = db.Column(db.String(50), primary_key=True)
    question = db.Column(db.String(500))
    option = db.Column(db.String(500))
    answer = db.Column(db.String(500))
    explanation = db.Column(db.String(500))


    __mapper_args__ = {
        'polymorphic_identity': 'question'
    }

    def __init__(self, sectionId, classId, quizId, questionId, question, option, answer, explanation):
        self.sectionId = sectionId
        self.classId = classId
        self.quizId = quizId
        self.questionId = questionId
        self.question = question
        self.option = option
        self.answer = answer
        self.explanation = explanation


    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)

            # convert string to list for option
            if column == "option":
                option_str = result["option"]
                result["option"] = list(option_str.split(";"))
                
        return result

class UserQuiz(db.Model):
    __tablename__ = 'userquiz'

    sectionId = db.Column(db.String(50), db.ForeignKey('quiz.sectionId'), primary_key=True)
    classId = db.Column(db.String(50), db.ForeignKey('quiz.classId'), primary_key=True)
    quizId = db.Column(db.String(50), db.ForeignKey('quiz.quizId'), primary_key=True)
    learnerId = db.Column(db.String(50), db.ForeignKey('learner.userId'), primary_key=True)
    option = db.Column(db.String(500))
    grade = db.Column(db.String(500))


    __mapper_args__ = {
        'polymorphic_identity': 'userquiz'
    }

    def __init__(self, sectionId, classId, quizId, learnerId, option, grade):
        self.sectionId = sectionId
        self.classId = classId
        self.quizId = quizId
        self.learnerId = learnerId
        self.option = option
        self.grade = grade

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)

            # convert string to list for option
            if column == "option":
                option_str = result["option"]
                result["option"] = list(option_str.split(";"))
                
        return result
class File(db.Model):
    __tablename__ = 'file'

    learnerId = db.Column(db.Integer, db.ForeignKey('learner.userId'), primary_key=True)
    fileId = db.Column(db.String(100), primary_key=True)
    completed = db.Column(db.Boolean)

    __mapper_args__ = {
        'polymorphic_identity': 'file'
    }
    
    def __init__(self, learnerId, fileId, completed):
        self.learnerId = learnerId
        self.fileId = fileId
        self.completed = completed


    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
        
db.create_all()

# create Course
@app.route("/createCourse", methods=['POST'])
def createCourse():

    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not all(key in data.keys() for
               key in ('courseId', 'courseName', 'courseDescription', 'prerequisites')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    course = Course.query.filter_by(courseId=data['courseId']).first()

    if course: # if a course is found, we want to redirect to restart create course process
        return jsonify({
            "message": "Course exists."
        }), 200
    
    # create a new course with the form data. 
    new_course = Course(courseId=data['courseId'], courseName=data['courseName'], courseDescription=data['courseDescription'], prerequisites=data['prerequisites'])

    # add the new course to the database
    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify(new_course.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

   
# get all courses
@app.route("/getCourses", methods=['GET'])
def getCourses():
    
    courses = Course.query.all()
    
    # check if user exists and validate password
    if not courses:
        return jsonify({
            "message": "No courses found."
        }), 404
    
    return jsonify(
        {
            "data": [course.to_dict() for course in courses]
        }
    ), 200

# create Class
@app.route("/createClass", methods=['POST'])
def createClass():
    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not all(key in data.keys() for
               key in ('classId', 'courseId', 'classSize', 'classTitle', 'startTime', 'endTime', 'startDate', 'endDate','enrolmentStartDate', 'enrolmentEndDate')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    _class = Class.query.filter_by(classId=data['classId']).first()
    

    if _class: 
        return jsonify({
            "message": "Class exists."
        }), 200
    
    new_class = Class(classId=data['classId'], courseId=data['courseId'], classSize=data['classSize'], classTitle=data['classTitle'], startTime=data['startTime'], endTime=data['endTime'], startDate=data['startDate'], endDate=data['endDate'], enrolmentStartDate=data['enrolmentStartDate'], enrolmentEndDate=data['enrolmentEndDate'], trainerAssigned=None, trainerName=None)

    
    try:
        db.session.add(new_class)
        db.session.commit()
        return jsonify(new_class.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# get specific course
@app.route("/getCourse/<string:courseId>", methods=['GET'])
def getCourse(courseId):
    
    course = Course.query.filter_by(courseId=courseId).first()
    
    # check if user exists and validate password
    if not course:
        return jsonify({
            "message": "No course found."
        }), 404
    
    return jsonify(course.to_dict()), 200

# get specific class
@app.route("/getClass/<string:classId>", methods=['GET'])
def getClass(classId):
    
    _class = Class.query.filter_by(classId=classId).first()
    
    # check if user exists and validate password
    if not _class:
        return jsonify({
            "message": "No class found."
        }), 200
    
    return jsonify(_class.to_dict()), 200

# get classes based on specific courseId
@app.route("/getClasses/<string:courseId>", methods=['GET'])
def getClasses(courseId):

    today = date.today()    
    current_date = today.strftime("%Y-%m-%d")

    classes = Class.query.filter_by(courseId=courseId).all()
    
    if not classes:
        return jsonify({
            "message": "No classes found."
        }), 404

    result = [_class.to_dict() for _class in classes]
    for element in result:
        if element["enrolmentStartDate"] <= current_date <= element["enrolmentEndDate"]:
            element["ableToEnrol"] = True
        else:
            element["ableToEnrol"] = False

    return jsonify(
        {
            "message": "Classes found",
            "data": result
        }
    ), 200

# Updating Class Record with Trainer ID
@app.route("/assignTrainerClass", methods=['PUT'])
def assignTrainerClass():
    # retrieved data
    data = request.get_json()
    
    classObj = Class.query.filter_by(classId=data['classId']).first()
    # (1): Validate class
    if not classObj:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate Trainer
    trainer = Trainer.query.filter_by(userId=data['trainerAssigned']).first()
    if not trainer:
        return jsonify({
            "message": "Trainer not valid."
        }), 502

    # (3): Update Class DB record
    classObj.trainerAssigned = data['trainerAssigned']
    classObj.trainerName = data['trainerName']

    # (4): Commit to DB
    try:
        db.session.merge(classObj)
        db.session.commit()
        return jsonify({
            "data": classObj.to_dict(),
            "message": "Trainer added"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

# get dict of courses that a trainer is assigned to 
@app.route("/getTrainerCourses/<string:trainerId>", methods=['GET'])
def getTrainerCourses(trainerId):

    trainer_existence = Trainer.query.filter(Trainer.userId==trainerId).all()
    
    # check if trainer exists 
    if not trainer_existence:
        return jsonify({
            "message": "Trainer not found."    
        }), 404

    trainerClasses = Class.query.filter(Class.trainerAssigned==trainerId).all()

    courseList = []
    distinctCourses = []
    for trainerClass in trainerClasses: 
        if trainerClass.courseId not in distinctCourses: 
            trainerCourse = Course.query.filter(Course.courseId==trainerClass.courseId).first()
            courseDict = {}
            courseDict['courseId'] = trainerClass.courseId
            courseDict['courseName'] = trainerCourse.courseName
            distinctCourses.append(trainerClass.courseId)
            courseList.append(courseDict)
    
    if len(courseList) == 0:
        return jsonify({
            "message": "No course found.",
            "data" : []
        }), 200
    return jsonify(
        {
            "data": courseList
        }
    ), 200

# get list of classId of a specific course that a trainer is assigned to 
@app.route("/getTrainerClasses/<string:trainerId>/<string:courseId>", methods=['GET'])
def getTrainerClasses(trainerId, courseId):

    trainer_existence = Trainer.query.filter(Trainer.userId==trainerId).all()
    # check if trainer exists 
    if not trainer_existence:
        return jsonify({
            "message": "Trainer not found."    
        }), 404

    course_existence = Course.query.filter(Course.courseId==courseId).all()
    # check if course exists 
    if not course_existence:
        return jsonify({
            "message": "Course not found."    
        }), 404

    trainerCourseClasses = Class.query.filter((Class.trainerAssigned==trainerId) & (Class.courseId==courseId)).all()

    classList = []
    for trainerCourseClass in trainerCourseClasses: 
        classList.append(trainerCourseClass.classId)
    
    if len(classList) == 0:
        return jsonify({
            "message": "No class found.",
            "data" : []
        }), 200
    return jsonify(
        {
            "data": [trainerClass.to_dict() for trainerClass in trainerCourseClasses],
            "classList": classList
        }
    ), 200

# Create Section
@app.route("/createSection", methods=['POST'])
def createSection():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkSection = Section.query.filter(
                            Section.sectionId == data["sectionId"], 
                            Section.classId == data['classId']
                        ).first()

    if checkSection:
        return jsonify({
            "message": "Section already exists."
        }), 501


    section = Section(
            sectionId = data['sectionId'],
            classId = data['classId'],
            fileName = None
        )

    # (4): Commit to DB
    try:
        db.session.add(section)
        db.session.commit()
        return jsonify(section.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# View Section
@app.route("/viewSections/<string:classId>", methods=['GET'])
def viewSection(classId):
    # retrieve data
    # data = request.get_json()

    # (1): Validate Section
    checkClass = Class.query.filter(Class.classId == classId).first()

    if not checkClass:
        return jsonify({
            "message": "Class does not exist."
        }), 501

    Sections = Section.query.filter(Section.classId == classId).all()

    try:
        return jsonify(
        {
            "data": [section.to_dict() for section in Sections]
        }), 200
    except Exception:
        return jsonify({
            "message": "No sections found."
        }), 404

# View courses available for LEARNER
@app.route('/viewLearnerCourses', methods=['GET'])
def getLearnerCourses():
    learnerId = request.args.get('learnerId')
    result = []

    list_of_courses = Course.query.all()

    for course in list_of_courses:
        # check if not prereq and not currently enrolled
        if not course.prerequisites and not checkIfCurrentlyEnrolled(learnerId, course.courseId):
            result.append(course.to_dict())

        elif course.prerequisites and not checkIfCurrentlyEnrolled(learnerId, course.courseId):
            prerequisite_courseId = (course.prerequisites).split(':')[0]
            if checkIfCompleted(learnerId, prerequisite_courseId):
                result.append(course.to_dict())

    return jsonify({
        'data': result
    }), 200

def checkIfCompleted(learnerId, courseId):
    enrolment = Enrolment.query.filter(Enrolment.learnerId==learnerId, Enrolment.courseId==courseId, Enrolment.completedClass==True).first()
    if enrolment:
        return True
    return False

def checkIfCurrentlyEnrolled(learnerId, courseId):
    enrolment = Enrolment.query.filter(Enrolment.learnerId==learnerId, Enrolment.courseId==courseId).first()
    if enrolment:
        return True
    return False

# View classes available for LEARNER
@app.route('/viewLearnerClasses')
def getLearnerClasses():
    courseId = request.args.get('courseId')
    today = date.today()
    current_date = today.strftime("%Y-%m-%d")

    class_list = Class.query.filter(Class.courseId==courseId, current_date <= Class.enrolmentEndDate).all()
    return jsonify({
        "data": [_class.to_dict() for _class in class_list]
    })

# get learnerId + learnerName enrolled in a class
@app.route("/enrolment/<string:classId>", methods=['GET'])
def getLearnersInClass(classId):

    class_existence = Class.query.filter(Class.classId == classId).all()
    
    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404

    enrolments = Enrolment.query.filter(
        (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).all()

    learner_name_list = []
    for enrolment in enrolments:
        learner_object = Learner.query.filter(
            Learner.userId == enrolment.to_dict()['learnerId']).first()
        learner_name_list.append(learner_object.to_dict()['employeeName'])

    enrolment_list_dic = []
    n = 0
    for enrolment in enrolments:
        print(enrolment.sectionsCompleted)
        learner_dict = {}
        learner_dict['learnerId'] = enrolment.to_dict()['learnerId']
        learner_dict['learnerName'] = learner_name_list[n]
        learner_dict['totalNumSections'] = enrolment.totalNumSections
        learner_dict['sectionsCompleted'] = enrolment.sectionsCompleted
        enrolment_list_dic.append(learner_dict)
        n += 1

    if not enrolments:
        return jsonify({
            "message": "No learners found.",
            "data": []
        }), 200
    return jsonify(
        {
            "data": enrolment_list_dic
        }
    ), 200

# get number of learners enrolled in a class
@app.route("/enrolment/number/<string:classId>", methods=['GET'])
def getNumberOfLearnersInClass(classId):
    class_existence = Class.query.filter(Class.classId == classId).all()

    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404

    num_enrolments = Enrolment.query.filter(
        (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

    return jsonify(
        {
            "data": num_enrolments
        }
    ), 200


# get number of learners enrolled in a classes taught by a Trainer
@app.route("/enrolment/size/<string:trainerId>/<string:courseId>", methods=['GET'])
def getCurrentClassSizeTrainer(trainerId, courseId):

    trainer_existence = Trainer.query.filter(Trainer.userId == trainerId).all()
    # check if trainer exists
    if not trainer_existence:
        return jsonify({
            "message": "Trainer not found."
        }), 404

    course_existence = Course.query.filter(Course.courseId == courseId).all()
    # check if course exists
    if not course_existence:
        return jsonify({
            "message": "Course not found."
        }), 405

    trainerCourseClasses = Class.query.filter(
        (Class.trainerAssigned == trainerId) & (Class.courseId == courseId)).all()

    classList = []
    for trainerCourseClass in trainerCourseClasses:
        classList.append(trainerCourseClass.classId)

    classDict = {}
    for classId in classList:
        class_existence = Class.query.filter(Class.classId == classId).all()

        # check if class exists
        if not class_existence:
            return jsonify({
                "message": "No class found."
            }), 406

        num_enrolments = Enrolment.query.filter(
            (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

        classDict[classId] = num_enrolments

    return jsonify(
        {
            "data": classDict
        }
    ), 200

# get number of learners enrolled in classes of a course
@app.route("/enrolment/size/<string:courseId>", methods=['GET'])
def getCurrentClassSize(courseId):

    course_existence = Course.query.filter(Course.courseId == courseId).all()
    # check if course exists
    if not course_existence:
        return jsonify({
            "message": "Course not found."
        }), 405

    CourseClasses = Class.query.filter(Class.courseId == courseId).all()

    classList = []
    for CourseClass in CourseClasses:
        classList.append(CourseClass.classId)

    classDict = {}
    for classId in classList:
        num_enrolments = Enrolment.query.filter(
            (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

        classDict[classId] = num_enrolments

    return jsonify(
        {
            "data": classDict
        }
    ), 200

# get learnerId + learnerName of qualified learners to be enrolled into a class
@app.route("/enrolment/qualifiedlearners/<string:classId>", methods=['GET'])
def getQualifiedLearnersOfClass(classId):
    class_existence = Class.query.filter(Class.classId == classId).first()
    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404
    courseId = class_existence.courseId

    # create list of userid of those who are already enrolled
    enrolments = Enrolment.query.filter(Enrolment.courseId == courseId).all()
    enrolment_list = []
    for enrolment in enrolments:
        enrolment_list.append(enrolment.learnerId)
    # create list of userid of those who are not enrolled into class
    learners_not_enrolled = Learner.query.filter(
        Learner.userId.notin_(enrolment_list)).all()
    intermediate_qualified_learnerIds = []
    for learner_not_enrolled in learners_not_enrolled:
        intermediate_qualified_learnerIds.append(learner_not_enrolled.userId)

    # get prequisite course
    course_id = class_existence.courseId
    this_course = Course.query.filter(Course.courseId == course_id).first()
    pre_requisiteId = (this_course.prerequisites).split(':')[0]

    if pre_requisiteId != "":
        qualified_enrolment_objects = Enrolment.query.filter(Enrolment.learnerId.in_(
            intermediate_qualified_learnerIds), Enrolment.courseId == pre_requisiteId, Enrolment.completedClass == True).all()

        qualified_learnerIds = []
        for qualified_enrolment_object in qualified_enrolment_objects:
            qualified_learnerIds.append(qualified_enrolment_object.learnerId)

        qualified_learner_objects = Learner.query.filter(
            Learner.userId.in_(qualified_learnerIds)).all()

    else:
        qualified_learner_objects = learners_not_enrolled

    # create list of dictionary for qualified_learners
    qualified_learners = []
    for qualified_learner_object in qualified_learner_objects:
        learner_dict = {}
        learner_dict['learnerId'] = qualified_learner_object.userId
        learner_dict['learnerName'] = qualified_learner_object.employeeName
        qualified_learners.append(learner_dict)

    return jsonify(
        {
            "data": qualified_learners
        }
    ), 200

# enrol learners into class


@app.route("/enrolment/enrolLearners", methods=['POST'])
def create_enrolment():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('classId', 'learnerIds')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classCheck = Class.query.filter_by(classId=data['classId']).first()

    if not classCheck:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate learner
    learner_Ids = data['learnerIds']
    enrolment_objects = []
    enrolment_objects2 = []
    for learner_Id in learner_Ids:
        learner = Learner.query.filter_by(userId=learner_Id).first()
        if not learner:
            return jsonify({
                "message": "There is an invalid learner."
            }), 502

        # (3): Check for enrolment record
        enrolments = Enrolment.query.filter(
            Enrolment.classId == data["classId"],
            Enrolment.learnerId == learner_Id
        ).first()

        if enrolments:
            return jsonify({
                "message": "Enrolment already added."
            }), 503

        # Compute total number of Sections in the class
        numSections = Section.query.filter(
            Section.classId == data["classId"]).count()
        class_object = Class.query.filter(
            Class.classId == data["classId"]).first()
        course_Id = class_object.to_dict()['courseId']
        enrolment = Enrolment(
            courseId=course_Id,
            classId=data['classId'],
            learnerId=learner_Id,
            totalNumSections=numSections,
            status='ACCEPTED'
        )
        enrolment_objects.append(enrolment)
        enrolment_objects2.append(enrolment.to_dict())

    # return jsonify({
    #         "data": enrolment_objects
    #     }), 201

    # (4): Commit to DB
    try:
        db.session.add_all(enrolment_objects)
        db.session.commit()
        return jsonify({
            "data": enrolment_objects2
        }), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504


# Remove learner from course
@app.route("/removeLearner", methods=['DELETE'])
def removeLearner():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classCheck = Class.query.filter_by(classId=data['classId']).first()

    if not classCheck:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate learner
    learner = Learner.query.filter_by(userId=data['learnerId']).first()

    if not learner:
        return jsonify({
            "message": "Learner not valid."
        }), 502

    # (3): Create enrolment record
    enrolment = Enrolment.query.filter(
        Enrolment.classId == data["classId"],
        Enrolment.learnerId == data['learnerId']
    ).first()

    if not enrolment:
        return jsonify({
            "message": "Enrolment does not exist."
        }), 503

    # (4): Commit to DB
    try:
        db.session.query(Enrolment).filter(
            Enrolment.classId == data['classId'], Enrolment.learnerId == data['learnerId']).delete()
        db.session.commit()
        return jsonify({
            "message": "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Self-enrolling of learner
@app.route('/enrolLearner', methods=['POST'])
def enrolLearner():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # Compute total number of Sections in the class
    numSections = Section.query.filter(
        Section.classId == data["classId"]).count()
    class_object = Class.query.filter(
        Class.classId == data["classId"]).first()
    course_Id = class_object.courseId

    enrolment = Enrolment(
        courseId=course_Id,
        classId=data['classId'],
        learnerId=data['learnerId'],
        totalNumSections=numSections,
        status="PENDING"
    )
    # Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# learner withdraw from course


@app.route("/withdrawLearner", methods=['DELETE'])
def withdrawLearner():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('courseId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    enrolment = db.session.query(Enrolment).filter(Enrolment.learnerId == data['learnerId'], Enrolment.courseId == data["courseId"], Enrolment.status.in_(['PENDING', 'ACCEPTED'])).first()

    if not enrolment:
        return jsonify({
            "message": "Enrolment does not exist."
        }), 503
        
    try:
        db.session.delete(enrolment)
        db.session.commit()
        return jsonify({
            "message": "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# VIEW ALL ENROLMENT BASED ON STATUS
@app.route('/viewPendingEnrolments')
def getPendingEnrolments():
    classId = request.args.get('classId')        

    pending_enrolments = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.status=="PENDING").all()
    result = [enrolment.to_dict() for enrolment in pending_enrolments]
    for element in result:
        learnerId = element["learnerId"]
        learnerName = (Learner.query.filter_by(userId=learnerId).first()).employeeName
        element["learnerName"] = learnerName


    if not pending_enrolments:
        return jsonify({
            "message": "No pending enrolments found.",
            "data": []
        }), 200
    return jsonify(
        {
            "message": "Pending enrolments found",
            "data": result
        }
    ), 200


# ACCEPT OR REJECT PENDING ENROLMENT REQUESTS
@app.route('/updateEnrolmentRequests', methods=['PUT'])
def updateEnrolmentRequest():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerIds', 'status')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    learnerIds = data['learnerIds']
    classId = data['classId']
    status = data['status']
    result = []


    learner_rows = db.session.query(Enrolment).filter(Enrolment.learnerId.in_(learnerIds), Enrolment.classId==classId).all()
    print(learner_rows)



    for row in learner_rows:
        row.status = status
        result.append(row.to_dict())
        print(row.to_dict())
    try:
        db.session.commit()
        return jsonify({
            "data": result,
            "message": "enrolment updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

# get enrolment records of learners' classes in progress
@app.route("/getEnrolmentsInProgress", methods=['GET'])
def getEnrolmentsInProgress():

    learnerId = request.args.get('learnerId')
    
    learnerExistence = Learner.query.filter(Learner.userId==learnerId).first()
    
    # check if learner exists
    if not learnerExistence:
        return jsonify({
            "message": "No learner found."
        }), 404
    
    enrolmentRecords = Enrolment.query.filter((Enrolment.learnerId==learnerId), (Enrolment.completedClass==False), (Enrolment.status=='ACCEPTED')).all()

    if len(enrolmentRecords)==0:
        return jsonify(
        {
            "message": 'Learner is not currently taking any class',
            "data": []
        }
    ), 200

    result = [enrolment.to_dict() for enrolment in enrolmentRecords]
    for element in result:
        courseId = element["courseId"]
        courseName = (Course.query.filter_by(courseId=courseId).first()).courseName
        element["courseName"] = courseName

        # get enorlment start and end date
        classObj = Class.query.filter(Class.classId == element["classId"]).first()
        element["startDate"] = classObj.startDate
        element["startTime"] = classObj.startTime
        element["endDate"] = classObj.endDate
        element["endTime"] = classObj.endTime

    
    return jsonify(
        {
            "message": "Current enrolments found",
            "data": result
        }
    ), 200

# get enrolment records of learners' pending classes
@app.route("/getLearnerPendingEnrolments", methods=['GET'])
def getLearnerPendingEnrolments():

    learnerId = request.args.get('learnerId')
    
    learnerExistence = Learner.query.filter(Learner.userId==learnerId).first()
    
    # check if learner exists
    if not learnerExistence:
        return jsonify({
            "message": "No learner found."
        }), 404
    
    enrolmentRecords = Enrolment.query.filter((Enrolment.learnerId==learnerId), (Enrolment.status=='PENDING')).all()
    
    if len(enrolmentRecords)==0:
        return jsonify(
        {
            "message": 'Learner does not have any pending classes',
            "data": []
        }
    ), 200

    result = [enrolment.to_dict() for enrolment in enrolmentRecords]
    for element in result:
        courseId = element["courseId"]
        courseName = (Course.query.filter_by(courseId=courseId).first()).courseName
        element["courseName"] = courseName

    return jsonify(
        {
            "message": "Pending enrolments found",
            "data": result
        }
    ), 200

# get enrolment records of learners' completed classes
@app.route("/getCompletedEnrolments", methods=['GET'])
def getCompletedEnrolments():

    learnerId = request.args.get('learnerId')
    
    learnerExistence = Learner.query.filter(Learner.userId==learnerId).first()
    
    # check if learner exists
    if not learnerExistence:
        return jsonify({
            "message": "No learner found."
        }), 404
    
    enrolmentRecords = Enrolment.query.filter((Enrolment.learnerId==learnerId), (Enrolment.completedClass==True)).all()
    
    if len(enrolmentRecords)==0:
        return jsonify(
        {
            "message": 'Learner has not completed any class',
            "data": []
        }
    ), 200

    result = [enrolment.to_dict() for enrolment in enrolmentRecords]
    for element in result:
        courseId = element["courseId"]
        courseName = (Course.query.filter_by(courseId=courseId).first()).courseName
        element["courseName"] = courseName

    return jsonify(
        {
            "message": "Pending enrolments found",
            "data": result
        }
    ), 200

# Award badge upon completing 
@app.route('/updateCompletionStatus', methods=['PUT'])
def updateCompletionStatus():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    learnerId = data['learnerId']
    classId = data['classId']

    # update enrolment record
    enrolmentObj = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.learnerId==learnerId).first()

    course_id = enrolmentObj.to_dict()['courseId']
    courseObj = Course.query.filter(Course.courseId==course_id).first()

    if enrolmentObj.completedClass: 
        return jsonify({
            "message": "Learner has already completed the class"
        }), 501

    enrolmentObj.completedClass = True

    try:
        db.session.merge(enrolmentObj)
        db.session.commit()
        return jsonify({
            "data": courseObj.to_dict(),
            "message": "enrolment updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

# get user's awarded badges
@app.route("/awardedBadges")
def awardedBadges():
    learner_id = request.args.get('learnerId')

    # (1): Validate learner
    learnerCheck = Learner.query.filter(Learner.userId==learner_id).first()

    if not learnerCheck:
        return jsonify({
            "message": "Learner does not exist"
        }), 501

    badges = Enrolment.query.filter((Enrolment.learnerId==learner_id) & (Enrolment.completedClass==True)).all()

    awarded_badge = []
    for badge in badges: 
        badgeDict = {}
        badgeDict['courseId'] = badge.courseId
        courseObject = Course.query.filter(Course.courseId==badge.courseId).first()
        badgeDict['courseName'] = courseObject.courseName
        awarded_badge.append(badgeDict)

    if len(awarded_badge) == 0: 
        return jsonify({
            "message": "Learner has not completed any courses",
            "data": []
        }), 200
    
    return jsonify(
        {
            "data": awarded_badge
        }
    ), 200

@app.route('/viewUserEnrolmentStatus')
def viewUserEnrolmentStatus():
    learnerId = request.args.get('learnerId')
    courseId = request.args.get('courseId')

    enrolment = Enrolment.query.filter(
        (Enrolment.learnerId==learnerId) & (Enrolment.courseId==courseId) & ((Enrolment.status=="ACCEPTED") | (Enrolment.status=="PENDING"))).first()
    if enrolment:
        return jsonify({
            "enrolmentStatus": enrolment.status
        }), 200
    else:
        return jsonify({
            "enrolmentStatus": "NOT ENROLLED"
        })
        # num_enrolments = Enrolment.query.filter(
        #     (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

@app.route('/getEnrolmentDetails', methods=['POST'])
def getEnrolmentDetails():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    classId = data['classId']
    learnerId = data['learnerId']
    
    enrolment = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.learnerId==learnerId).first()

    if enrolment:
        return jsonify(enrolment.to_dict()), 200
    else:
        return jsonify({
            "message": "no enrolment"
        })

# Get all questions in a Quiz
@app.route("/quiz/<string:classId>/<string:sectionId>", methods=['GET'])
def getAllQuestions(classId, sectionId):
    quiz = Quiz.query.filter(
        Quiz.sectionId == sectionId,
        Quiz.classId == classId,
    ).first()

    # check if class exists
    if not quiz:
        return jsonify({
            "message": "No quiz found."
        }), 203

    questions = Question.query.filter(
        Question.sectionId == sectionId,
        Question.classId == classId,
        Question.quizId == quiz.quizId
    ).all()
    quiz = Quiz.query.filter(
        Quiz.sectionId == sectionId,
        Quiz.classId == classId,
        Quiz.quizId == quiz.quizId
    ).first()

    if not questions:
        return jsonify({
            "message": "No questions found."
        }), 204

    result = [question.to_dict() for question in questions]
    for element in result:
        element['value'] = ''

    return jsonify(
        {
            "questions": result,
            "time": quiz.get_time(),
            "quiz": quiz.to_dict()
        }
    ), 200


# create quiz in a section
@app.route("/learnerSubmitQuiz", methods=['POST'])
def learnerSubmitQuiz():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'option', 'learnerId', 'grade')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 501

    # (1): Validate userquiz
    checkUserQuiz = UserQuiz.query.filter(
        UserQuiz.sectionId == data["sectionId"],
        UserQuiz.classId == data['classId'],
        UserQuiz.learnerId == data['learnerId'],
    ).first()

    if checkUserQuiz:
        return jsonify({
            "message": "Learner has already attempted Quiz."
        }), 203

    sectionId = data['sectionId']
    quizId = sectionId.replace("Section", 'Quiz')

    user_enrolment = Enrolment.query.filter(
        Enrolment.classId == data['classId'], Enrolment.learnerId == data['learnerId']).first()
    user_enrolment.sectionsCompleted += 1

    userQuiz = UserQuiz(
        sectionId=sectionId,
        classId=data['classId'],
        quizId=quizId,
        learnerId=data['learnerId'],
        option=data['option'],
        grade=data['grade']
    )

    # (4): Commit to DB
    try:
        db.session.add(userQuiz)
        db.session.merge(user_enrolment)
        db.session.commit()
        return jsonify(userQuiz.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 500

# Update a specific record in userquiz
@app.route("/submitFinalQuiz", methods=['PUT'])
def submitFinalQuiz():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'learnerId', 'option', 'grade', 'quizId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    userQuiz = UserQuiz.query.filter(
        UserQuiz.sectionId == data["sectionId"],
        UserQuiz.classId == data['classId'],
        UserQuiz.learnerId == data['learnerId'],
    ).first()

    user_enrolment = Enrolment.query.filter(
        Enrolment.classId == data['classId'], Enrolment.learnerId == data['learnerId']).first()
    
    grade = ''
    
    if float(data['grade']) >= 0.85:
        grade = "Pass"
        user_enrolment.sectionsCompleted += 1
        user_enrolment.completedClass = True

    else:
        grade = "Fail"

    if not userQuiz:
        userQuiz = UserQuiz(
            sectionId=data['sectionId'],
            classId=data['classId'],
            quizId=data['sectionId'],
            learnerId=data['learnerId'],
            option=data['option'],
            grade=grade
        )

        # (4): Commit to DB
        try:
            db.session.add(userQuiz)
            db.session.merge(user_enrolment)
            db.session.commit()
            return jsonify(userQuiz.to_dict()), 201

        except Exception:
            return jsonify({
                "message": "Unable to commit to database.",
                "data": str(request.get_data())
            }), 500

    else:
        userQuiz.option = data['option']
        userQuiz.grade = grade

        # (4): Commit to DB
        try:
            db.session.merge(userQuiz)
            db.session.merge(user_enrolment)
            db.session.commit()
            return jsonify({
                "data": userQuiz.to_dict(),
                "message": "Question updated"
            }), 200
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 503

# retrieve stored answers for a particular quiz
@app.route("/retrieveLearnerQuizAnswers", methods=['POST'])
def retrieveLearnerQuizAnswers():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    userQuiz = UserQuiz.query.filter(
        UserQuiz.sectionId == data["sectionId"],
        UserQuiz.classId == data['classId'],
        UserQuiz.learnerId == data['learnerId'],
    ).first()

    if not userQuiz:
        return jsonify({
            "message": "Learner has not attempted Quiz."
        }), 500

    option = userQuiz.option
    grade = userQuiz.grade

    return jsonify({"data": option,
                    "grade": grade
                    }), 200

# create quiz in a section
@app.route("/createQuiz", methods=['POST'])
def createQuiz():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'time')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkQuiz = Quiz.query.filter(
        Quiz.sectionId == data["sectionId"],
        Quiz.classId == data['classId'],
        Quiz.quizId == data['quizId'],
        Quiz.time == data['time'],
    ).first()

    if checkQuiz:
        return jsonify({
            "message": "Quiz already exists."
        }), 501

    quiz = Quiz(
        sectionId=data['sectionId'],
        classId=data['classId'],
        quizId=data['quizId'],
        time=data['time']
    )

    # (4): Commit to DB
    try:
        db.session.add(quiz)
        db.session.commit()
        return jsonify(quiz.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Get a specific question in a quiz of a section
@app.route("/question/<string:classId>/<string:sectionId>/<string:quizId>/<string:questionId>", methods=['GET'])
def getQuestion(classId, sectionId, quizId, questionId):

    question = Question.query.filter(
        Question.sectionId == sectionId,
        Question.classId == classId,
        Question.quizId == quizId,
        Question.questionId == questionId
    ).first()

    # check if question exists
    if not question:
        return jsonify({
            "message": "No question found."
        }), 404

    return jsonify(question.to_dict()), 200

# create a question for a quiz
@app.route("/createQuestion", methods=['POST'])
def createQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId', 'question', 'option', 'answer', 'explanation')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkQuestion = Question.query.filter(
        Question.sectionId == data["sectionId"],
        Question.classId == data['classId'],
        Question.quizId == data['quizId'],
        Question.questionId == data['questionId']
    ).first()

    if checkQuestion:
        return jsonify({
            "message": "Question already exists"
        }), 501

    question = Question(
        sectionId=data['sectionId'],
        classId=data['classId'],
        quizId=data['quizId'],
        questionId=data['questionId'],
        question=data['question'],
        option=data['option'],
        answer=data['answer'],
        explanation=data['explanation']
    )
    print(question.to_dict())

    # (4): Commit to DB
    try:
        db.session.add(question)
        db.session.commit()
        return jsonify(question.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Update a specific Question in a quiz
@app.route("/updateQuestion", methods=['PUT'])
def updateQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    question = Question.query.filter(
        Question.sectionId == data["sectionId"],
        Question.classId == data['classId'],
        Question.quizId == data['quizId'],
        Question.questionId == data['questionId']
    ).first()

    if not question:
        return jsonify({
            "message": "Question is not valid"
        }), 501

    # (3): Update Class DB record
    if 'question' in data:
        question.question = data['question']
    if 'option' in data:
        question.option = data['option']
    if 'answer' in data:
        question.answer = data['answer']
    if 'explanation' in data:
        question.explanation = data['explanation']

    # (4): Commit to DB
    try:
        db.session.merge(question)
        db.session.commit()
        return jsonify({
            "data": question.to_dict(),
            "message": "Question updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503


# Remove learner from course
@app.route("/removeQuestion", methods=['DELETE'])
def removeQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    question = Question.query.filter(
        Question.sectionId == data["sectionId"],
        Question.classId == data['classId'],
        Question.quizId == data['quizId'],
        Question.questionId == data['questionId']
    ).first()

    if not question:
        return jsonify({
            "message": "Question is not valid"
        }), 501

    # Commit to DB
    try:
        db.session.query(Question).filter(
            Question.sectionId == data["sectionId"],
            Question.classId == data['classId'],
            Question.quizId == data['quizId'],
            Question.questionId == data['questionId']).delete()
        db.session.commit()
        return jsonify({
            "message": "Question Deleted"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

@app.route("/upload", methods=['PUT'])
def upload():
    courseId = request.args.get('courseId')
    className = request.args.get('className')
    sectionName = request.args.get('sectionName')
    file = request.files['file']

    filename = secure_filename(file.filename)

    file_type = mimetypes.guess_type(filename)
    
    try:
        response = s3.put_object(ACL='public-read',
                                 Body=file,
                                 Bucket=BUCKET,
                                 Key=f'{courseId}/{className}/{sectionName}/' + filename,
                                 ContentType=file_type[0]
                                 )
        return response

    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to commit to s3.",
            "data": str(request.get_data())
        }), 500


@app.route("/getFiles")
def list_files():
    """
    Function to list files in a given S3 bucket
    """
    courseId = request.args.get('courseId')
    className = request.args.get('className')
    sectionName = request.args.get('sectionName')
    result = []
    try:
        response = s3.list_objects(
            Bucket=BUCKET, Prefix=f'{courseId}/{className}/{sectionName}/')['Contents']
            
        for item in response:
            url = S3_DOMAIN + item['Key']
            filename = (item['Key']).split('/')[-1]
            betterFileId = ((item['Key']).replace('/', '')).replace('.', "")
            
            result.append({"filename": filename,
                           "url": url,
                           "completed": False,
                           "fileId": item['Key'],
                           "betterFileId": betterFileId
                           })
        return jsonify(result)

    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to get files from s3."
        }), 500


@app.route("/removeFile", methods=['DELETE'])
def removeFile():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('courseId', 'className', 'sectionName', 'fileName')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    courseId = data['courseId']
    className = data['className']
    sectionName = data['sectionName']
    fileName = data['fileName']

    try:
        response = s3.delete_object(
            Bucket=BUCKET,
            Key=f'{courseId}/{className}/{sectionName}/' + fileName
        )
        return response
    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to delete file from s3."
        }), 500

# create user
@app.route("/createUser", methods=['POST'])
def create_trainer():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('employeeName', 'userName', 'email',
                       'password', 'userType', 'designation', 'department')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    user = User.query.filter_by(email=data['email']).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({
            "message": "User exists."
        }), 404
    
    if data['userType'] == 'Trainer':
        new_user = Trainer(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    elif data['userType'] == 'Learner':
        new_user = Learner(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    elif data['userType'] == 'HR':
        new_user = Hr(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    print(new_user.to_dict())
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# get trainer based on id or get all trainers
@app.route("/getTrainers")
def trainers():
    search_id = request.args.get('userId')
    if search_id:
        trainer_list = Trainer.query.filter(Trainer.userId.contains(search_id))
    else:
        trainer_list = Trainer.query.all()
    return jsonify(
        {
            "data": [trainer.to_dict() for trainer in trainer_list]
        }
    ), 200

# get learner based on id or get all learners
@app.route("/getLearners")
def learners():
    search_id = request.args.get('userId')
    if search_id:
        learner_list = Learner.query.filter(Learner.userId.contains(search_id))
    else:
        learner_list = Learner.query.all()
    return jsonify(
        {
            "data": [learner.to_dict() for learner in learner_list]
        }
    ), 200

# get hr based on id or get all hrs
@app.route("/getHrs")
def hrs():
    search_id = request.args.get('userId')
    if search_id:
        hr_list = Hr.query.filter(Hr.userId.contains(search_id))
    else:
        hr_list = Hr.query.all()
    return jsonify(
        {
            "data": [hr.to_dict() for hr in hr_list]
        }
    ), 200
   
# login to user account
@app.route("/login", methods=['POST'])
def login():

    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not data['userName']:
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # data_userName = data['userName']
    
    user = User.query.filter_by(userName=data['userName']).first()
    
    if not user:
        return jsonify({
            "message": "Person not found."
        }), 404
    
    else:
        return jsonify(
            {
                "data": user.to_dict()
            }
        ), 200

# set learner's course material as completed
@app.route('/setFileCompleted', methods=['POST'])
def setFileCompleted():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('learnerId', 'fileId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    file = File(learnerId=data['learnerId'], fileId=data['fileId'], completed=True)
    
    try:
        db.session.add(file)
        db.session.commit()
        return jsonify(file.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
        
@app.route('/getCompletedFiles', methods=['POST'])
def getCompletedFiles():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('courseId', 'className', 'sectionName', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    courseId = data['courseId']
    className = data['className']
    sectionName = data['sectionName']
    learnerId = data['learnerId']

    file_path = f"{courseId}/{className}/{sectionName}/"
    
    files = File.query.filter(File.fileId.contains(file_path), File.learnerId==learnerId).all()

    if files:
        return jsonify(
            {
                "data": [file.fileId for file in files]
            }
        ), 200
    else:
        return jsonify(
            {
                "data": [],
                "message": "no files completed yet"
            }
        ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)