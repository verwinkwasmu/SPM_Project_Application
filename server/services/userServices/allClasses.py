from typing import ClassVar
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

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

db.create_all()