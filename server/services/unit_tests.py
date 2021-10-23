import unittest

from allClasses import *
from werkzeug.security import generate_password_hash, check_password_hash

class TestUser(unittest.TestCase):
    def setUp(self):
        self.pw = generate_password_hash("admin123")
        self.user = User(userId=1, 
                        userName="test1",
                        email="test1@email.com",
                        password=self.pw,
                        userType="HR"
                    )

    def tearDown(self):
        self.user = None
    
    def test_to_dict(self):
        self.assertEqual(self.user.to_dict(), {
                "userId":1, 
                "userName":"test1",
                "email":"test1@email.com",
                "password":self.pw,
                "userType":"HR"
            }
        )
    
    def test_verify_password_pass(self):
        self.assertEqual(self.user.verify_password("admin123"), True)
        
    def test_verify_password_fail(self):
        self.assertEqual(self.user.verify_password("12345"), False)

class TestLearner(unittest.TestCase):
    def test_to_dict(self):
        l1 = Learner(userId=1, 
                    userName="test1",
                    email="test1@email.com",
                    password="admin123",
                    userType="Learner"
                    )

        self.assertEqual(l1.to_dict(), {
                "userId":1, 
                "userName":"test1",
                "email":"test1@email.com",
                "password":"admin123",
                "userType":"Learner"
            }
        )

class TestTrainer(unittest.TestCase):
    def test_to_dict(self):
        t1 = Trainer(userId=1, 
                    userName="test1",
                    email="test1@email.com",
                    password="admin123",
                    userType="Trainer"
                    )

        self.assertEqual(t1.to_dict(), {
                "userId":1, 
                "userName":"test1",
                "email":"test1@email.com",
                "password":"admin123",
                "userType":"Trainer"
            }
        )

class TestHR(unittest.TestCase):
    def test_to_dict(self):
        h1 = Hr(userId=1, 
                userName="test1",
                email="test1@email.com",
                password="admin123",
                userType="HR"
            )

        self.assertEqual(h1.to_dict(), {
                "userId":1, 
                "userName":"test1",
                "email":"test1@email.com",
                "password":"admin123",
                "userType":"HR"
            }
        )

class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(courseId="XRX-101", 
                    courseName="Software Project Management",
                    courseDescription="Fun Course",
                    prerequisites="coursename")

        self.assertEqual(c1.to_dict(), {
            'courseId': 'XRX-101',
            'courseName': 'Software Project Management',
            'courseDescription': 'Fun Course',
            'prerequisites':'coursename'
            }
        )

class TestClass(unittest.TestCase):
    def test_to_dict(self):
        c1 = Class(classId="XRX-101 Class 1",
                    courseId="XRX-101", 
                    classSize=40,
                    classTitle="Class 1",
                    startTime = "10:00",
                    endTime = "13:00",
                    startDate = "2021-11-30",
                    endDate = "2021-12-30",
                    enrolmentPeriod="2021-10-30 to 2021-11-29",
                    trainerAssigned=13,
                    trainerName="Sir Verwin"
                    )

        self.assertEqual(c1.to_dict(), {
                "classId":"XRX-101 Class 1",
                "courseId":"XRX-101", 
                "classSize":40,
                "classTitle":"Class 1",
                "startTime" : "10:00",
                "endTime" : "13:00",
                "startDate" : "2021-11-30",
                "endDate" : "2021-12-30",
                "enrolmentPeriod":"2021-10-30 to 2021-11-29",
                "trainerAssigned":13,
                "trainerName":"Sir Verwin"
            }
        )

class TestEnrolment(unittest.TestCase):
    def test_to_dict(self):
        e1 = Enrolment(classId="XRX-101 Class 1",
                        learnerId=13,
                        totalNumSections = 10,
                        sectionsCompleted = 2,
                        completedClass = False
                    )

        self.assertEqual(e1.to_dict(), {
                "classId":"XRX-101 Class 1",
                "learnerId":13,
                "totalNumSections" : 10,
                "sectionsCompleted" : 2,
                "completedClass" : False
            }
        )

class TestSection(unittest.TestCase):
    def test_to_dict(self):
        s1 = Section(classId="XRX-101 Class 1",
                    sectionId="Section 1",
                    fileName = "Introduction_Lesson_1"
                    )

        self.assertEqual(s1.to_dict(), {
                "classId":"XRX-101 Class 1",
                "sectionId":"Section 1",
                "fileName" : "Introduction_Lesson_1"
            }
        )

class TestQuiz(unittest.TestCase):
    def test_to_dict(self):
        q1 = Quiz(classId="XRX-101 Class 1",
                    sectionId="Section 1",
                    quizId = "Quiz 1"
                    )

        self.assertEqual(q1.to_dict(), {
                "classId":"XRX-101 Class 1",
                "sectionId":"Section 1",
                "quizId" : "Quiz 1"
            }
        )

class TestQuestion(unittest.TestCase):
    def test_to_dict(self):
        q1 = Question(classId="XRX-101 Class 1",
                        sectionId="Section 1",
                        quizId = "Quiz 1",
                        questionId = "Question 1",
                        question = "What's is your mother's name?",
                        option = "Mary;Laobu;Karen;Ni Mama",
                        answer = "Ni Mama"
                    )

        self.assertEqual(q1.to_dict(), {
                "classId": "XRX-101 Class 1",
                "sectionId": "Section 1",
                "quizId": "Quiz 1",
                "questionId": "Question 1",
                "question": "What's is your mother's name?",
                "option": [
                    "Mary",
                    "Laobu",
                    "Karen",
                    "Ni Mama"
                ],
                "answer": "Ni Mama"
            }
        )

if __name__ == "__main__":
    unittest.main()