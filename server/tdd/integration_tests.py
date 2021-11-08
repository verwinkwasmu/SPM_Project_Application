import unittest
import flask_testing
import json
from allClasses import *
from app import app, db, Course, User, Learner, Trainer, Hr, Class, Enrolment, Section, Quiz, Question, UserQuiz


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateCourse(TestApp):
    def testCreateCourse(self):
        # c1 = Course(courseId="IS213", 
        #             courseName="Software Project Management",
        #             courseDescription="Fun Course",
        #             prerequisites="IS113")
        # db.session.add(c1)
        # db.session.commit()

        request_body ={
            'courseId': 'IS213',
            'courseName': 'Software Project Management',
            'courseDescription': 'Fun Course',
            'prerequisites': 'IS113'
        }
        response = self.client.post("/createCourse",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.json, {
            'courseId': 'IS213',
            'courseName': 'Software Project Management',
            'courseDescription': 'Fun Course',
            'prerequisites': 'IS113'
        })


if __name__ == '__main__':
    unittest.main()