from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(120))
    userType = db.Column(db.String(50))
    

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __init__(self, userId, userName, email, password, userType):
        self.userId = userId
        self.userName = userName
        self.email = email
        self.password = password
        self.userType = userType

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
    
    def verify_password(self, password):
        if check_password_hash(self.password, password):
            return True
        return False

class Learner(User):
    __tablename__ = 'learner'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'learner',
    }

    def __init__(self, userId, userName, email, password, userType):
        super().__init__(userId, userName, email, password, userType)

class Trainer(User):
    __tablename__ = 'trainer'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'trainer',
    }

    def __init__(self, userId, userName, email, password, userType):
        super().__init__(userId, userName, email, password, userType)

class Hr(User):
    __tablename__ = 'hr'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'hr',
    }

    def __init__(self, userId, userName, email, password, userType):
        super().__init__(userId, userName, email, password, userType)

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
    classTiming = db.Column(db.String(120))
    classTimeline = db.Column(db.String(120))
    enrolmentPeriod = db.Column(db.String(120))
    trainerAssigned = db.Column(db.Integer, db.ForeignKey('trainer.userId')) # userId

    __mapper_args__ = {
        'polymorphic_identity': 'class'
    }

    def __init__(self, classId, courseId, classSize, classTitle, classTiming, classTimeline, enrolmentPeriod, trainerAssigned):
        self.classId = classId
        self.courseId = courseId
        self.classSize = classSize
        self.classTitle = classTitle
        self.classTiming = classTiming
        self.classTimeline = classTimeline
        self.enrolmentPeriod = enrolmentPeriod
        self.trainerAssigned = trainerAssigned
    
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

    def __init__(self, learnerId, classId):
        self.learnerId = learnerId
        self.classId = classId
    
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