import unittest
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

        db.create_all()
        db.session.add(self.course1)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateCourse(TestApp):
    def testCreateCourse(self):
        request_body ={
            'courseId': 'IS213',
            'courseName': 'Software Project Management',
            'courseDescription': 'Fun Course',
            'prerequisites': 'IS113'
        }
        response = self.client.post("/createCourse",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'courseId': 'IS213',
            'courseName': 'Software Project Management',
            'courseDescription': 'Fun Course',
            'prerequisites': 'IS113'
        })

class TestGetCourses(TestApp):
    def testGetCourses(self):
        response = self.client.get("/getCourses",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [{
                'courseId': 'SPM',
                'courseName': 'Software Project Management',
                'courseDescription': 'This is SPM',
                'prerequisites': 'IS110'
            }]
        })

class TestGetCourse(TestApp):
    def testGetCourse(self):
        response = self.client.get("/getCourse/SPM",
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'courseId': 'SPM',
            'courseName': 'Software Project Management',
            'courseDescription': 'This is SPM',
            'prerequisites': 'IS110'
        })
    


if __name__ == '__main__':
    unittest.main()