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

        self.course1 = Course(courseId='SPM', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='IS110')
        self.course2 = Course(courseId='SPM3', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='IS110')

        self.class1 = Class(classId='SPM G1', courseId="B-101", classSize=10, classTitle='SPM G1', startTime='01:00', endTime='10:00', 
        startDate='2021-10-11', endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=13, trainerName='Chris')

        self.class2 = Class(classId='SPM', courseId="SPM", classSize=10, classTitle='SPM', startTime='01:00', endTime='10:00', 
        startDate='2021-10-11', endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=1, trainerName='Chris')

        self.trainer1 = Trainer(userId=1, employeeName='Chris', userName='trainer1', email='trainer1@hotmail.com', userType='Trainer', designation='Manager', department='Fixing')
        self.section1 = Section(sectionId=2,classId='SPM2', fileName=None)

        self.course5 = Course(courseId='SPM5', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='IS110')
        self.class5 = Class(classId='SPM G5', courseId=self.course5.courseId, classSize=10, classTitle='SPM G5', startTime='01:00', endTime='10:00', startDate='2021-10-11', endDate='2021-10-12', 
        enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=13, trainerName='Chris')
        
        self.learner5 = Learner(userId=5, employeeName='Wayne', userName='Learner1', email='wayne@hotmail.com', userType='Learner', designation='Manager', department='Fixing')

        self.course6 = Course(courseId='SPM6', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='')
        self.class6 = Class(classId='SPM G6', courseId=self.course6.courseId, classSize=10, classTitle='SPM G6', startTime='01:00', endTime='10:00', startDate='2021-10-11', endDate='2021-10-12', 
        enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-12-09', trainerAssigned=13, trainerName='Chris')

        # self.course0 = Course(courseId='SPMG0', courseName='Software Project Management', courseDescription='This is SPM', prerequisites='')
        self.class0 = Class(classId='SPM G0', courseId="POP", classSize=10, classTitle='SPM G0', startTime='01:00', endTime='10:00', startDate='2021-10-11', endDate='2021-10-12', 
        enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-12-09', trainerAssigned=None, trainerName=None)
        self.trainer2 = Trainer(userId=6, employeeName='Puis', userName='trainer6', email='trainer6@hotmail.com', userType='Trainer', designation='Manager', department='Fixing')

        

        db.session.add(self.course1)
        db.session.add(self.class1)
        db.session.add(self.class2)
        db.session.add(self.trainer1)

        db.session.add(self.course5)
        db.session.add(self.class5)   
        db.session.add(self.course6)
        db.session.add(self.class6)   
        db.session.add(self.learner5)
          
        db.session.add(self.class0)
        db.session.add(self.trainer2)

        # db.session.add(self.course0)

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestCreateClass(TestApp):
    def testCreateClass(self):
        request_body ={ 
            'classId': 'B-102 Class 1',
            'courseId': 'B-101',
            'classSize': 49,
            'classTitle': 'Class 1',
            'startTime': '12:00',
            'endTime': '17:30',
            'startDate': '2021-10-10',
            'endDate': '2021-11-10',
            'enrolmentStartDate': '2021-10-01',
            'enrolmentEndDate': '2021-10-08',
            'trainerAssigned': None,
            'trainerName': None,
        }
        response = self.client.post("/createClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'classId': 'B-102 Class 1',
            'classSize': 49,
            'classTitle': 'Class 1',
            'courseId': 'B-101',
            'endDate': '2021-11-10',
            'endTime': '17:30',
            'enrolmentEndDate': '2021-10-08',
            'enrolmentStartDate': '2021-10-01',
            'startDate': '2021-10-10',
            'startTime': '12:00',
            'trainerAssigned': None,
            'trainerName': None,
        })
class TestGetClass(TestApp):
    def testGetClass(self):
        response = self.client.get("/getClass/SPM G1",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
           "classId": "SPM G1",
            "classSize": 10,
            "classTitle": "SPM G1",
            "courseId": "B-101",
            "endDate": "2021-10-12",
            "endTime": "10:00",
            "enrolmentEndDate": "2021-10-09",
            "enrolmentStartDate": "2021-10-01",
            "startDate": "2021-10-11",
            "startTime": "01:00",
            "trainerAssigned": 13,
            "trainerName": "Chris"
        })
class TestGetClasses(TestApp):
    def testGetClasses(self):
        response = self.client.get("/getClasses/B-101",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [{
                "ableToEnrol": False,
                "classId": "SPM G1",
                "classSize": 10,
                "classTitle": "SPM G1",
                "courseId": "B-101",
                "endDate": "2021-10-12",
                "endTime": "10:00",
                "enrolmentEndDate": "2021-10-09",
                "enrolmentStartDate": "2021-10-01",
                "startDate": "2021-10-11",
                "startTime": "01:00",
                "trainerAssigned": 13,
                "trainerName": "Chris",
            }],
            "message": "Classes found"
        })

class TestGetTrainerCourses(TestApp):
    def testGeGetTrainerCourses(self):
        response = self.client.get("/getTrainerCourses/1",
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

class TestGetTrainerClasses(TestApp):
    def testGeGetTrainerClasses(self):
        response = self.client.get("/getTrainerClasses/1/SPM",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "classList": [
                    "SPM"
                ],
            "data": [
                {
                    "classId": "SPM",
                    "classSize": 10,
                    "classTitle": "SPM",
                    "courseId": "SPM",
                    "endDate": "2021-10-12",
                    "endTime": "10:00",
                    "enrolmentEndDate": "2021-10-09",
                    "enrolmentStartDate": "2021-10-01",
                    "startDate": "2021-10-11",
                    "startTime": "01:00",
                    "trainerAssigned": 1,
                    "trainerName": "Chris",
                }
            ]
        })

class TestCreateSection(TestApp):
    def testCreateSection(self):
        request_body ={ 
            "sectionId": "1",
            "classId": "SPM",
            "fileName": None
        }
        response = self.client.post("/createSection",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            "classId": "SPM",
            "sectionId": "1",
            "fileName": None
        })

class TestViewSection(TestApp):
    def testViewSection(self):
        request_body ={ 
            "sectionId": "2",
            "classId": "SPM2",
            "fileName": None
        }
        response = self.client.post("/createSection",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            "classId": "SPM2",
            "sectionId": "2",
            "fileName": None
        })

class TestGetLearnerCourses(TestApp):
    def testgetLearnerCourses(self):
        request_body ={ 
            "learnerId": 5
        }
        response = self.client.get("/viewLearnerCourses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
           "data": [
                {
                    "courseDescription": "This is SPM",
                    "courseId": "SPM6",
                    "courseName": "Software Project Management",
                    "prerequisites": ""
                },
            ]
        
        })

class TestGetLearnerClasses(TestApp):
    def testgetLearnerClasses(self):
        response = self.client.get("/viewLearnerClasses?courseId=SPM6",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
           "data": [
                {
                    "classId": "SPM G6",
                    "classSize": 10,
                    "classTitle": "SPM G6",
                    "courseId": "SPM6",
                    "endDate": "2021-10-12",
                    "endTime": "10:00",
                    "enrolmentEndDate": "2021-12-09",
                    "enrolmentStartDate": "2021-10-01",
                    "startDate": "2021-10-11",
                    "startTime": "01:00",
                    "trainerAssigned": 13,
                    "trainerName": "Chris"
                },
            ]
        })

class TestAssignTrainerClass(TestApp):
    def testAssignTrainerClass(self):
        request_body ={ 
            "classId": "SPM G0",
            "trainerAssigned": 6,
            "trainerName": "Puis"
        }
        
        response = self.client.put("/assignTrainerClass",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
           "data": 
                {
                    "classId": "SPM G0",
                    "classSize": 10,
                    "classTitle": "SPM G0",
                    "courseId": "POP",
                    "endDate": "2021-10-12",
                    "endTime": "10:00",
                    "enrolmentEndDate": "2021-12-09",
                    "enrolmentStartDate": "2021-10-01",
                    "startDate": "2021-10-11",
                    "startTime": "01:00",
                    "trainerAssigned": 6,
                    "trainerName": "Puis"
                },
            "message": "Trainer added"
        })
if __name__ == '__main__':
    unittest.main()