from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from userServices import Learner


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# what does this do?
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

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
    classTiming = db.Column(db.String(120))
    classTimeline = db.Column(db.String(120))
    enrolmentPeriod = db.Column(db.String(120))
    trainerAssigned = db.Column(db.Integer) # userId

    __mapper_args__ = {
        'polymorphic_identity': 'class'
    }
    
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

    classId = db.Column(db.String(50), db.ForeignKey('class.classId'), primary_key=True)
    learnerId = db.Column(db.Integer, db.ForeignKey('learner.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'enrolment'
    }
    
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

# get all courses
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
    enrolment = Enrolment(
        classId = data['classId'], learnerId = data['learnerId']
    )
    print(enrolment)

    # (4): Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)