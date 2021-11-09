import unittest
from app import *
from werkzeug.security import generate_password_hash, check_password_hash

class TestUser(unittest.TestCase):
    def setUp(self):
        self.pw = generate_password_hash("admin123")
        self.user = User(userId=1, 
                        employeeName="Jacbo",
                        userName="test1",
                        email="test1@email.com",
                        userType="HR",
                        designation=None,
                        department=None
                    )

    def tearDown(self):
        self.user = None
    
    def test_to_dict(self):
        self.assertEqual(self.user.to_dict(), {
                "userId":1, 
                "employeeName": "Jacbo",
                "userName":"test1",
                "email":"test1@email.com",
                "userType":"HR",
                "designation": None,
                "department": None
            }
        )
    

class TestLearner(unittest.TestCase):
    def test_to_dict(self):
        l1 = Learner(userId=1, 
                    employeeName="Jacbo",
                    userName="test1",
                    email="test1@email.com",
                    userType="Learner",
                    designation=None,
                    department=None
                    )

        self.assertEqual(l1.to_dict(), {
                "userId":1, 
                "employeeName": "Jacbo",
                "userName":"test1",
                "email":"test1@email.com",
                "userType":"Learner",
                "designation": None,
                "department": None
            }
        )

class TestTrainer(unittest.TestCase):
    def test_to_dict(self):
        t1 = Trainer(userId=1, 
                    employeeName="Jacbo",
                    userName="test1",
                    email="test1@email.com",
                    userType="Trainer",
                    designation=None,
                    department=None
                    )

        self.assertEqual(t1.to_dict(), {
                "userId":1, 
                "employeeName": "Jacbo",
                "userName":"test1",
                "email":"test1@email.com",
                "userType":"Trainer",
                "designation": None,
                "department": None
            }
        )

class TestHR(unittest.TestCase):
    def test_to_dict(self):
        h1 = Hr(userId=1, 
                employeeName="Jacbo",
                userName="test1",
                email="test1@email.com",
                userType="HR",
                designation=None,
                department=None
            )

        self.assertEqual(h1.to_dict(), {
                "userId":1, 
                "employeeName": "Jacbo",
                "userName":"test1",
                "email":"test1@email.com",
                "userType":"HR",
                "designation": None,
                "department": None
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
                    enrolmentStartDate= "2021-10-30",
                    enrolmentEndDate= "2021-11-29",
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
                "enrolmentStartDate" : "2021-10-30",
                "enrolmentEndDate" : "2021-11-29",
                "trainerAssigned":13,
                "trainerName":"Sir Verwin"
            }
        )

class TestEnrolment(unittest.TestCase):
    def test_to_dict(self):
        e1 = Enrolment(
                        courseId="XRX-101",
                        classId="XRX-101 Class 1",
                        learnerId=13,
                        totalNumSections = 10,
                        sectionsCompleted = 2,
                        completedClass = False,
                        status="PENDING"
                    )

        self.assertEqual(e1.to_dict(), {
                "courseId": "XRX-101",
                "classId":"XRX-101 Class 1",
                "learnerId":13,
                "totalNumSections" : 10,
                "sectionsCompleted" : 2,
                "completedClass" : False,
                "status": "PENDING"
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
                    quizId = "Quiz 1",
                    time= 30
                    )

        self.assertEqual(q1.to_dict(), {
                "classId":"XRX-101 Class 1",
                "sectionId":"Section 1",
                "quizId" : "Quiz 1",
                "time": 30
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
                        answer = "Ni Mama",
                        explanation="Your mother is a lovely women"
                        
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
                "answer": "Ni Mama",
                "explanation": "Your mother is a lovely women"
            }
        )

class TestUserQuiz(unittest.TestCase):
    def test_to_dict(self):
        uq1 = UserQuiz(sectionId="Section 1",
                    classId="XRX-101 Class 1",
                    quizId="Quiz 1",
                    learnerId= 1,
                    option="Hi;hey;ho;woo",
                    grade="Pass"
                    )
        self.assertEqual(uq1.to_dict(), {
                "sectionId": "Section 1",
                "classId": "XRX-101 Class 1",
                "quizId": "Quiz 1",
                "learnerId": 1,
                "option": [
                    "Hi",
                    "hey",
                    "ho",
                    "woo"
                ],
                "grade": "Pass"
            }
        )

class TestFile(unittest.TestCase):
    def test_to_dict(self):
        file1 = File(learnerId=1,
                    fileId="XRX-101/Class1/Section1/Hello.png",
                    completed=True
                    )
        self.assertEqual(file1.to_dict(),{
            "learnerId": 1,
            "fileId": "XRX-101/Class1/Section1/Hello.png",
            "completed": True
        })
        
if __name__ == "__main__":
    unittest.main()