from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from allClasses import *
from sqlalchemy.sql import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}
db = SQLAlchemy(app)

CORS(app)

# create Course
@app.route("/createCourse", methods=['POST'])
def createCourse():

    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not all(key in data.keys() for
               key in ('courseName', 'courseDescription', 'prerequisites')):
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
               key in ('classId', 'courseId', 'classSize', 'classTitle', 'startTime', 'endTime', 'startDate', 'endDate','enrolmentPeriod')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    _class = Class.query.filter_by(classId=data['classId']).first()
    

    if _class: 
        return jsonify({
            "message": "Class exists."
        }), 200
    
    new_class = Class(classId=data['classId'], courseId=data['courseId'], classSize=data['classSize'], classTitle=data['classTitle'], startTime=data['startTime'], endTime=data['endTime'], startDate=data['startDate'], endDate=data['endDate'], enrolmentPeriod=data['enrolmentPeriod'], trainerAssigned=None, trainerName=None)

    
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
        }), 404
    
    return jsonify(_class.to_dict()), 200

# get classes based on specific courseId
@app.route("/getClasses/<string:courseId>", methods=['GET'])
def getClasses(courseId):
    
    classes = Class.query.filter_by(courseId=courseId).all()
    
    # check if user exists and validate password
    if not classes:
        return jsonify({
            "message": "No classes found."
        }), 404
    
    return jsonify(
        {
            "data": [_class.to_dict() for _class in classes]
        }
    ), 200 

# get learnerId + learnerName enrolled in a class 
@app.route("/enrolment/<string:classId>", methods=['GET'])
def getLearnersInClass(classId):

    class_existence = Class.query.filter(Class.classId==classId).all()
    
    # check if class exists 
    if not class_existence:
        return jsonify({
            "message": "No class found."    
        }), 404
    
    enrolments = Enrolment.query.filter((Enrolment.classId==classId) & (Enrolment.completedClass==False)).all()

    learner_name_list = []
    for enrolment in enrolments:
        learner_object = Learner.query.filter(Learner.userId==enrolment.to_dict()['learnerId']).first()
        learner_name_list.append(learner_object.to_dict()['employeeName'])

    enrolment_list_dic = []
    n = 0
    for enrolment in enrolments:
        learner_dict = {}
        learner_dict['learnerId'] = enrolment.to_dict()['learnerId']
        learner_dict['learnerName'] = learner_name_list[n]
        enrolment_list_dic.append(learner_dict)
        n+=1
    
    if not enrolments:
        return jsonify({
            "message": "No learners found."
        }), 404
    return jsonify(
        {
            "data": enrolment_list_dic
        }
    ), 200

# get number of learners enrolled in a class 
@app.route("/enrolment/number/<string:classId>", methods=['GET'])
def getNumberOfLearnersInClass(classId):

    class_existence = Class.query.filter(Class.classId==classId).all()
    
    # check if class exists 
    if not class_existence:
        return jsonify({
            "message": "No class found."    
        }), 404
    
    num_enrolments = Enrolment.query.filter((Enrolment.classId==classId) & (Enrolment.completedClass==False)).count()

    return jsonify(
        {
            "data": num_enrolments
        }
    ), 200

# get learnerId + learnerName of qualified learners to be enrolled into a class
@app.route("/enrolment/qualifiedlearners/<string:classId>", methods=['GET'])
def getQualifiedLearnersOfClass(classId):

    class_existence = Class.query.filter(Class.classId==classId).first()
    
    # check if class exists 
    if not class_existence:
        return jsonify({
            "message": "No class found."    
        }), 404

    #create list of userid of those who are already enrolled
    enrolments = Enrolment.query.filter(Enrolment.classId==classId).all()
    enrolment_list = []
    for enrolment in enrolments:
        enrolment_list.append(enrolment.to_dict()['learnerId'])

    #create list of userid of those who are not enrolled into class
    learners_not_enrolled = Learner.query.filter(Learner.userId.not_in(enrolment_list)).all()
    intermediate_qualified_learnerIds = []
    for learner_not_enrolled in learners_not_enrolled:
        intermediate_qualified_learnerIds.append(learner_not_enrolled.to_dict()['userId'])

    #get prequisite course
    course_id = class_existence.to_dict()['courseId']
    this_course = Course.query.filter(Course.courseId==course_id).first()
    pre_requisite = this_course.to_dict()['prerequisites']

    if pre_requisite != "":
        qualified_enrolment_objects = Enrolment.query.filter(Enrolment.learnerId.in_(intermediate_qualified_learnerIds), Enrolment.courseId==pre_requisite, Enrolment.completedClass==True).all()

        qualified_learnerIds = []
        for qualified_enrolment_object in qualified_enrolment_objects:
            qualified_learnerIds.append(qualified_enrolment_object.to_dict()['learnerId'])

        qualified_learner_objects = Learner.query.filter(Learner.userId.in_(qualified_learnerIds)).all()

    else:
        qualified_learner_objects = learners_not_enrolled

    #create list of dictionary for qualified_learners
    qualified_learners = []
    for qualified_learner_object in qualified_learner_objects:
        learner_dict = {}
        learner_dict['learnerId'] = qualified_learner_object.to_dict()['userId']
        learner_dict['learnerName'] = qualified_learner_object.to_dict()['employeeName']
        qualified_learners.append(learner_dict)
    
    return jsonify(
    {
        "data": qualified_learners
    }
)   , 200
    
#enrol learners into class
@app.route("/enrolment", methods=['POST'])
def create_enrolment():
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
    enrolments = Enrolment.query.filter(
                                    Enrolment.classId == data["classId"], 
                                    Enrolment.learnerId == data['learnerId']
                                ).first()

    if enrolments:
        return jsonify({
            "message": "Enrolment already added."
        }), 503
    
    # Compute total number of Sections in the class
    numSections = Section.query.filter(Section.classId == data["classId"]).count()
    enrolment = Enrolment(
        classId = data['classId'], 
        learnerId = data['learnerId'],
        totalNumSections = numSections
    )

    # (4): Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Updating Class Record with Trainer ID
@app.route("/assignTrainerClass", methods=['PUT'])
def assignTrainerClass():
    # retrieved data
    data = request.get_json()

    # if not all(key in data.keys() for
    #            key in ('classId', 'trainerAssigned, trainerName')):
    #     return jsonify({
    #         "message": "Incorrect JSON object provided."
    #     }), 500
    
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


# Remove learner from course
@app.route("/removeLearner", methods=['DELETE'])
def removeTrainer():
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
        db.session.query(Enrolment).filter(Enrolment.classId==data['classId'], Enrolment.learnerId==data['learnerId']).delete()
        db.session.commit()
        return jsonify({
            "message" : "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504


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
            classId = data['classId']
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

# Get all questions in a Quiz
@app.route("/quiz/<string:classId>/<string:sectionId>/<string:quizId>", methods=['GET'])
def getAllQuestions(classId, sectionId, quizId):
    quiz = Quiz.query.filter(
                                Quiz.sectionId == sectionId, 
                                Quiz.classId == classId,
                                Quiz.quizId == quizId
                            ).first()
    
    # check if class exists 
    if not quiz:
        return jsonify({
            "message": "No quiz found."    
        }), 404

    questions = Question.query.filter(
                                        Question.sectionId == sectionId, 
                                        Question.classId == classId,
                                        Question.quizId == quizId
                                    ).all()

    if not questions:
        return jsonify({
            "message": "No learners found."
        }), 404

    return jsonify(
        {
            "data": [question.to_dict() for question in questions]
        }
    ), 200

# create quiz in a section
@app.route("/createQuiz", methods=['POST'])
def createQuiz():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkQuiz = Quiz.query.filter(
                            Quiz.sectionId == data["sectionId"], 
                            Quiz.classId == data['classId'],
                            Quiz.quizId == data['quizId']
                        ).first()


    if checkQuiz:
        return jsonify({
            "message": "Quiz already exists."
        }), 501


    quiz = Quiz(
            sectionId = data['sectionId'],
            classId = data['classId'],
            quizId = data['quizId']
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
    
    # check if class exists 
    if not question:
        return jsonify({
            "message": "No question found."    
        }), 404

    return jsonify(question.to_dict()), 200

# create question for a quiz
@app.route("/createQuestion", methods=['POST'])
def createQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId', 'question', 'option', 'answer')):
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
            sectionId = data['sectionId'],
            classId = data['classId'],
            quizId = data['quizId'],
            questionId = data['questionId'],
            question = data['question'],
            option = data['option'],
            answer = data['answer']
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)