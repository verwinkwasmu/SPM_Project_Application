import unittest

from sqlalchemy.orm.session import sessionmaker
import flask_testing
import json
# from allClasses import *
from app import app, db, Course, User, Learner, Trainer, Hr, Class, Enrolment, Section, Quiz, Question, UserQuiz


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        self.trainer1 = Trainer(userId=13, employeeName='Verwin', userName='Trainer13', email='verwin@hotmail.com', userType='Trainer', designation='Director', department='Fixing')

        self.course1 = Course(courseId='SPM', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='')
        self.course1class1 = Class(classId='SPM G1', courseId=self.course1.courseId, classSize=10, classTitle='G1', startTime='01:00', endTime='10:00', startDate='2021-10-11', endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)
        self.course1class2= Class(classId='SPM G2', courseId=self.course1.courseId, classSize=10, classTitle='G2', startTime='01:00', endTime='10:00', startDate='2021-10-11', endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)

        self.course2 = Course(courseId='OOP', courseName='Object Oriented Programming', courseDescription='This is OOP', prerequisites='SPM:Software Project Management')
        self.course2class1 = Class(classId='OOP G1', courseId=self.course2.courseId, classSize=20, classTitle='G1', startTime='02:00', endTime='12:00', startDate='2021-10-15', endDate='2021-10-30', enrolmentStartDate='2021-10-05', enrolmentEndDate='2021-10-10', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)

        self.course3 = Course(courseId='CT', courseName='Computational Thinking', courseDescription='This is CT', prerequisites='')
        self.course3class1 = Class(classId='CT G1', courseId=self.course3.courseId, classSize=30, classTitle='G1', startTime='02:00', endTime='12:00', startDate='2021-10-15', endDate='2021-10-30', enrolmentStartDate='2021-10-05', enrolmentEndDate='2021-10-10', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)
        self.c3c1s1 = Section(classId=self.course3class1.classId, sectionId='Section1', fileName='')
        
        self.learner1 = Learner(userId=1, employeeName='Wayne', userName='Learner1', email='wayne@hotmail.com', userType='Learner', designation='Manager', department='Fixing')
        self.learner1enrolment1 = Enrolment(courseId=self.course1class1.courseId, classId=self.course1class1.classId, learnerId=self.learner1.userId, totalNumSections=10, status='ACCEPTED')

        self.learner2 = Learner(userId=2, employeeName='Fiona', userName='Learner2', email='fiona@hotmail.com', userType='Learner', designation='Admin', department='Fixing')
        self.learner2enrolment1 = Enrolment(courseId=self.course1class1.courseId, classId=self.course1class1.classId, learnerId=self.learner2.userId, totalNumSections=10, status='ACCEPTED')

        self.learner3 = Learner(userId=3, employeeName='Ezra', userName='Learner3', email='ezra@hotmail.com', userType='Learner', designation='Assistant', department='Fixing')
        self.learner3enrolment1 = Enrolment(courseId=self.course2class1.courseId, classId=self.course2class1.classId, learnerId=self.learner3.userId, totalNumSections=10, status='PENDING')

        self.learner4 = Learner(userId=4, employeeName='WX', userName='Learner4', email='wx@hotmail.com', userType='Learner', designation='Intern', department='Fixing')
        self.learner4enrolment1 = Enrolment(courseId=self.course1class2.courseId, classId=self.course1class2.classId, learnerId=self.learner4.userId, totalNumSections=10, status='ACCEPTED')

        self.learner5 = Learner(userId=5, employeeName='Nicki', userName='Learner5', email='nicki@hotmail.com', userType='Learner', designation='Intern', department='Troubleshooting')
        self.learner5enrolment1 = Enrolment(courseId=self.course1class2.courseId, classId=self.course1class2.classId, learnerId=self.learner5.userId, totalNumSections=10, status='ACCEPTED', completedClass=True)

        db.session.add(self.trainer1)
        db.session.add(self.course1)
        db.session.add(self.course1class1)  
        db.session.add(self.course1class2)
        db.session.add(self.course2)
        db.session.add(self.course2class1)   
        db.session.add(self.course3)
        db.session.add(self.course3class1) 
        db.session.add(self.c3c1s1)
        db.session.add(self.learner1)   
        db.session.add(self.learner1enrolment1)   
        db.session.add(self.learner2)   
        db.session.add(self.learner2enrolment1)   
        db.session.add(self.learner3)   
        db.session.add(self.learner3enrolment1)  
        db.session.add(self.learner4)   
        db.session.add(self.learner4enrolment1)
        db.session.add(self.learner5)   
        db.session.add(self.learner5enrolment1)          
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestGetBadges(TestApp):
    def testGetBadges(self):
        response = self.client.get("/awardedBadges?learnerId=5",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [
                {
                    "courseId": "SPM",
                    "courseName": "Software Project Management"
                },
            ]
        })
        
if __name__ == '__main__':
    unittest.main()