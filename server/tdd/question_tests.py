import unittest
import flask_testing
import json
# from allClasses import *
from app import app, db, Course, User, Learner, Trainer, Hr, Class, Enrolment, Section, Quiz, Question, UserQuiz

class TestCreateQuiz(flask_testing.TestCase):
    def test_createQuiz(self):
        request_body = {
            'sectionId': 'Section 3',
            'classId':'XRX-101 Class 1',
            'quizId':'Quiz 3',
            'time': 20
        }     

        response = self.client.post("/createQuiz",
                                        data=json.dumps(request_body),
                                        content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,
                 {  'sectionId': 'Section 3',
                    'classId': 'XRX-101 Class 1',
                    'quizId': 'Quiz 3',
                    'time': 20
                    }
                )

class TestGetSpecificQuestionInQuiz(flask_testing.TestCase):
    def test_getSpecificQuestionInQuiz(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId':'XRX-101 Class 1',
            'quizId':'Final Quiz',
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


class TestCreateQuestion(flask_testing.TestCase):
    def test_createQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId':'XRX-101 Class 1',
            'quizId':'Final Quiz',
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



class TestUpdateQuestion(flask_testing.TestCase):
    def test_updateQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId':'XRX-101 Class 1',
            'quizId':'Final Quiz',
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



class TestRemoveQuestion(flask_testing.TestCase):
    def test_removeQuestion(self):
        request_body = {
            'sectionId': 'Final Quiz',
            'classId':'XRX-101 Class 1',
            'quizId':'Final Quiz',
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