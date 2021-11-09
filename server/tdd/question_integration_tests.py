import unittest
import flask_testing
import json
from app import app, db, Course, Learner, Class, Enrolment, Section, Quiz, Question, UserQuiz


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        self.course1 = Course(courseId="IS213", courseName="Software Project Management",
                              courseDescription="Fun Course", prerequisites="IS113")
        self.class1 = Class(classId="XRX-101 Class 1", courseId=self.course1.courseId, classSize=40, classTitle="Class 1", startTime="09:00", endTime="16:40",
                            startDate="2021-09-05", endDate="2021-09-30", enrolmentStartDate="2021-08-24", enrolmentEndDate="2021-09-01", trainerAssigned="3", trainerName="Ali")
        self.section1 = Section(
            classId=self.class1.classId, sectionId="Final Quiz", fileName="pdf")
        self.quiz1 = Quiz(classId=self.class1.classId,
                          sectionId=self.section1.sectionId, quizId="Final Quiz", time=30)
        self.question1 = Question(
            sectionId=self.quiz1.sectionId,
            classId=self.quiz1.classId,
            quizId=self.quiz1.quizId,
            questionId="Question 3",
            question="Brother printers are cost effective, Why?",
            option="Cheap;Fast;Sustainable;IDK",
            answer="Sustainable",
            explanation="Does not use that much sun power")
        self.learner1 = Learner(userId=1, employeeName='Wayne', userName='Learner1',
                                email='wayne@hotmail.com', userType='Learner', designation='Manager', department='Fixing')
        self.enrolment1 = Enrolment(courseId=self.class1.courseId, classId=self.class1.classId, learnerId=self.learner1.userId,
                                    totalNumSections=10, status='ACCEPTED', sectionsCompleted=0, completedClass=True)
        self.userquiz1 = UserQuiz(sectionId=self.section1.sectionId, classId=self.class1.classId,
                                  quizId=self.quiz1.quizId, learnerId=self.learner1.userId, option="Cheap;Fast;Sustainable;ILK", grade=0.85)

        db.session.add(self.course1)
        db.session.add(self.class1)
        db.session.add(self.section1)
        db.session.add(self.quiz1)
        db.session.add(self.question1)
        db.session.add(self.learner1)
        db.session.add(self.enrolment1)
        db.session.add(self.userquiz1)

        # db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCreateQuiz(TestApp):
    def test_createQuiz(self):
        request_body = {
            'sectionId': 'Section 3',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Quiz 3',
            'time': 20
        }

        response = self.client.post("/createQuiz",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,
                         {'sectionId': 'Section 3',
                          'classId': 'XRX-101 Class 1',
                          'quizId': 'Quiz 3',
                          'time': 20
                          }
                         )


class TestGetSpecificQuestionInQuiz(TestApp):
    def test_getSpecificQuestionInQuiz(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'questionId': 'Question 3'
        }

        response = self.client.get("/question/XRX-101%20Class%201/Final%20Quiz/Final%20Quiz/Question%203",
                                   data=json.dumps(request_body),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {'answer': 'Sustainable',
                          'classId': 'XRX-101 Class 1',
                          'explanation': 'Does not use that much sun power',
                          'option': ['Cheap', 'Fast', 'Sustainable', 'IDK'],
                          'question': 'Brother printers are cost effective, Why?',
                          'questionId': 'Question 3',
                          'quizId': 'Final Quiz',
                          'sectionId': 'Final Quiz'}
                         )


class TestCreateQuestion(TestApp):
    def test_createQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'questionId': 'Question 4',
            'question': 'Is it warm or cold?',
            'option': 'True;False;;',
            'answer': 'True',
            'explanation': 'Becus its very expensive!'
        }

        response = self.client.post("/createQuestion",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,
                         {'answer': 'True',
                          'classId': 'XRX-101 Class 1',
                          'explanation': 'Becus its very expensive!',
                          'option':
                          ['True',
                           'False',
                           '',
                           ''],
                             'question': 'Is it warm or cold?',
                             'questionId': 'Question 4',
                             'quizId': 'Final Quiz',
                             'sectionId': 'Final Quiz'

                          }
                         )


class TestUpdateQuestion(TestApp):
    def test_updateQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'questionId': 'Question 3',
            'question': 'Is it warm or cold?',
            'option': 'True;False;;',
            'answer': 'True',
            'explanation': 'Becus its very expensive!'
        }

        response = self.client.put("/updateQuestion",
                                   data=json.dumps(request_body),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {'data': {'answer': 'True',
                                   'classId': 'XRX-101 Class 1',
                                   'explanation': 'Becus its very expensive!',
                                   'option':
                                   ['True',
                                    'False',
                                    '',
                                    ''],
                                   'question': 'Is it warm or cold?',
                                   'questionId': 'Question 3',
                                   'quizId': 'Final Quiz',
                                   'sectionId': 'Final Quiz'},
                          'message': 'Question updated'})


class TestRemoveQuestion(TestApp):
    def test_removeQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'questionId': 'Question 3'

        }

        response = self.client.delete("/removeQuestion",
                                      data=json.dumps(request_body),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json,
                         {"message": "Question Deleted"}
                         )


if __name__ == '__main__':
    unittest.main()
