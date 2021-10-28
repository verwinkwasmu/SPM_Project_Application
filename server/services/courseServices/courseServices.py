from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from allClasses import *
# from sqlalchemy.sql import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}
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

# get courses that a trainer is assigned to 
@app.route("/getTrainerCourses/<string:trainerId>", methods=['GET'])
def getTrainerCourses(trainerId):

    trainer_existence = Trainer.query.filter(Trainer.userId==trainerId).all()
    
    # check if class exists 
    if not trainer_existence:
        return jsonify({
            "message": "Trainer not found."    
        }), 404

    trainerClasses = Class.query.filter(Class.trainerAssigned==trainerId).all()

    courseList = {}
    for trainerClass in trainerClasses: 
        if trainerClass.courseId not in courseList: 
            trainerCourse = Course.query.filter(Course.courseId==trainerClass.courseId).first()
            courseList[trainerClass.courseId] = trainerCourse.courseName
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)