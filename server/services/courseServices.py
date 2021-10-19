from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from allClasses import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
        }), 404
    
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
               key in ('classId', 'courseId', 'classSize', 'classTitle', 'classTiming', 'classTimeline', 'enrolmentPeriod', 'trainerAssigned')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    _class = Class.query.filter_by(classId=data['classId']).first()
    

    if _class: 
        return jsonify({
            "message": "Class exists."
        }), 404
    
    new_class = Class(**data)
    print(new_class.to_dict())
    
    try:
        db.session.add(new_class)
        db.session.commit()
        return jsonify(new_class.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# get specific class
@app.route("/getClass/<string:courseId>", methods=['GET'])
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
    print(classCheck.to_dict())
    if not classCheck:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate learner
    learner = Learner.query.filter_by(userId=data['learnerId']).first()
    print(learner.to_dict())
    if not learner:
        return jsonify({
            "message": "Learner not valid."
        }), 502

                                    # classId=data["classId"], learnerId=data['learnerId']
    # (3): Create enrolment record
    enrolments = Enrolment.query.filter(
                                    Enrolment.classId == data["classId"], 
                                    Enrolment.learnerId == data['learnerId']
                                ).first()

    if enrolments:
        return jsonify({
            "message": "Enrolment already added."
        }), 503
    
    enrolment = Enrolment(
        classId = data['classId'], 
        learnerId = data['learnerId']
    )

    # (4): Commit to DB
    try:
        db.session.add(enrolment)
        print(enrolment.to_dict())

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

    if not all(key in data.keys() for
               key in ('classId', 'trainerAssigned')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
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

    # (4): Commit to DB
    try:
        db.session.commit()
        return jsonify({
            "trainer": data['trainerAssigned'],
            "class": data["classId"],
            "message": "Trainer added"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503


# Remove learner from course
@app.route("/removeLearner", methods=['POST'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)