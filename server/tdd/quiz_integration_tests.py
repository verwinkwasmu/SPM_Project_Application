import unittest
import flask_testing
import json
from app import app, db, Course, Learner, Class, Enrolment, Section, Quiz, Question, UserQuiz

## Fiona ##
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


class TestGetAllQuestions(TestApp):
    def test_get_all_questions(self):

        response = self.client.get("/quiz/XRX-101 Class 1/Final Quiz",
                                   content_type='application/json')

        self.assertEqual(response.json, {
            "questions": [
                {
                    "answer": "Sustainable",
                    "classId": "XRX-101 Class 1",
                    "explanation": "Does not use that much sun power",
                    "option": [
                        "Cheap",
                        "Fast",
                        "Sustainable",
                        "IDK"
                    ],
                    "question": "Brother printers are cost effective, Why?",
                    "questionId": "Question 3",
                    "quizId": "Final Quiz",
                    "sectionId": "Final Quiz",
                    "value": ""
                },
            ],
            "quiz": {
                "classId": "XRX-101 Class 1",
                "quizId": "Final Quiz",
                "sectionId": "Final Quiz",
                "time": 30
            },
            "time": 30
        })
        self.assertEqual(response.status_code, 200)

    def test_get_all_questionsNoQuiz(self):
        response = self.client.get("/quiz/XRX-101 Class 1/Final Quizz",
                            content_type='application/json')

        self.assertEqual(response.status_code, 203)
        self.assertEqual(response.json, {
            "message": "No quiz found."
        })

        

class TestLearnerSubmitQuiz(TestApp):
    def test_learner_submit_quiz(self):
        request_body = {

            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'learnerId': '1',
            'option': "Cheap;Fast;Sustainable;IDK",
            'grade': 'Pass',
            'message': 'Learner has already attempted Quiz.'

        }
        response = self.client.post("/learnerSubmitQuiz",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.json, {

            'message': 'Learner has already attempted Quiz.'

        })


class TestSubmitFinalQuiz(TestApp):
    def test_submit_final_quiz(self):

        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            'quizId': 'Final Quiz',
            'learnerId': '1',
            'option': "Cheap;Fast;Sustainable;IDK",
            'grade': 0.85
        }
        response = self.client.put("/submitFinalQuiz",
                                   data=json.dumps(request_body),
                                   content_type='application/json')

        self.assertEqual(response.json, {
            'data': {'classId': 'XRX-101 Class 1',
                     'grade': 'Pass',
                     'learnerId': '1',
                     'option': ['Cheap', 'Fast', 'Sustainable', 'IDK'],
                     'quizId': 'Final Quiz',
                     'sectionId': 'Final Quiz'},
            'message': 'Question updated'}
        )


class TestRetrieveLearnerQuizAnswer(TestApp):
    def test_retrieve_learner_quiz_answer(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId': 'XRX-101 Class 1',
            # 'quizId':'Final Quiz',
            'learnerId': '1',
            'option': "True,True,Sustainable,Not wise as its hard to maintain",
            'grade': 'Pass'
        }
        response = self.client.post("/retrieveLearnerQuizAnswers",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'data': 'Cheap;Fast;Sustainable;ILK', 'grade': '0.85'})

    def test_retrieveLearnerQuizAnswerNotAttempted(self):
        request_body = {
            'sectionId': 'Final Quizz',
            'classId': 'XRX-101 Class 11',
            # 'quizId':'Final Quiz',
            'learnerId': '1',
            'option': "True,True,Sustainable,Not wise as its hard to maintain",
            'grade': 'Pass'
        }
        response = self.client.post("/retrieveLearnerQuizAnswers",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(
        response.json, {"message": "Learner has not attempted Quiz."})

if __name__ == '__main__':
    unittest.main()
