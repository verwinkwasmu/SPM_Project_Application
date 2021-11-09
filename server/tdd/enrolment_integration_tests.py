import unittest
import flask_testing
import json
from app import app, db, Course, Learner, Trainer, Class, Enrolment, Section


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        self.trainer1 = Trainer(userId=13, employeeName='Verwin', userName='Trainer13',
                                email='verwin@hotmail.com', userType='Trainer', designation='Director', department='Fixing')

        self.course1 = Course(courseId='SPM', courseName='Software Project Management',
                              courseDescription='This is SPM', prerequisites='')
        self.course1class1 = Class(classId='SPM G1', courseId=self.course1.courseId, classSize=10, classTitle='G1', startTime='01:00', endTime='10:00', startDate='2021-10-11',
                                   endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)
        self.course1class2 = Class(classId='SPM G2', courseId=self.course1.courseId, classSize=10, classTitle='G2', startTime='01:00', endTime='10:00', startDate='2021-10-11',
                                   endDate='2021-10-12', enrolmentStartDate='2021-10-01', enrolmentEndDate='2021-10-09', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)

        self.course2 = Course(courseId='OOP', courseName='Object Oriented Programming',
                              courseDescription='This is OOP', prerequisites='SPM:Software Project Management')
        self.course2class1 = Class(classId='OOP G1', courseId=self.course2.courseId, classSize=20, classTitle='G1', startTime='02:00', endTime='12:00', startDate='2021-10-15',
                                   endDate='2021-10-30', enrolmentStartDate='2021-10-05', enrolmentEndDate='2021-10-10', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)

        self.course3 = Course(courseId='CT', courseName='Computational Thinking',
                              courseDescription='This is CT', prerequisites='')
        self.course3class1 = Class(classId='CT G1', courseId=self.course3.courseId, classSize=30, classTitle='G1', startTime='02:00', endTime='12:00', startDate='2021-10-15',
                                   endDate='2021-10-30', enrolmentStartDate='2021-10-05', enrolmentEndDate='2021-10-10', trainerAssigned=self.trainer1.userId, trainerName=self.trainer1.employeeName)
        self.c3c1s1 = Section(
            classId=self.course3class1.classId, sectionId='Section1', fileName='')

        self.learner1 = Learner(userId=1, employeeName='Wayne', userName='Learner1',
                                email='wayne@hotmail.com', userType='Learner', designation='Manager', department='Fixing')
        self.learner1enrolment1 = Enrolment(courseId=self.course1class1.courseId, classId=self.course1class1.classId,
                                            learnerId=self.learner1.userId, totalNumSections=10, status='ACCEPTED')

        self.learner2 = Learner(userId=2, employeeName='Fiona', userName='Learner2',
                                email='fiona@hotmail.com', userType='Learner', designation='Admin', department='Fixing')
        self.learner2enrolment1 = Enrolment(courseId=self.course1class1.courseId, classId=self.course1class1.classId,
                                            learnerId=self.learner2.userId, totalNumSections=10, status='ACCEPTED')

        self.learner3 = Learner(userId=3, employeeName='Ezra', userName='Learner3',
                                email='ezra@hotmail.com', userType='Learner', designation='Assistant', department='Fixing')
        self.learner3enrolment1 = Enrolment(courseId=self.course2class1.courseId, classId=self.course2class1.classId,
                                            learnerId=self.learner3.userId, totalNumSections=10, status='PENDING')

        self.learner4 = Learner(userId=4, employeeName='WX', userName='Learner4',
                                email='wx@hotmail.com', userType='Learner', designation='Intern', department='Fixing')
        self.learner4enrolment1 = Enrolment(courseId=self.course1class2.courseId, classId=self.course1class2.classId,
                                            learnerId=self.learner4.userId, totalNumSections=10, status='ACCEPTED')

        self.learner5 = Learner(userId=5, employeeName='Nicki', userName='Learner5', email='nicki@hotmail.com',
                                userType='Learner', designation='Intern', department='Troubleshooting')
        self.learner5enrolment1 = Enrolment(courseId=self.course1class2.courseId, classId=self.course1class2.classId,
                                            learnerId=self.learner5.userId, totalNumSections=10, status='ACCEPTED', completedClass=True)

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


class TestGetLearnersInClass(TestApp):
    def test_get_learners_in_class(self):

        response = self.client.get(
            "/enrolment/SPM G1", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [
                {
                    "learnerId": 1,
                    "learnerName": "Wayne",
                    "sectionsCompleted": 0,
                    "totalNumSections": 10
                },
                {
                    "learnerId": 2,
                    "learnerName": "Fiona",
                    "sectionsCompleted": 0,
                    "totalNumSections": 10
                }
            ]
        }
        )


class TestGetNumberOfLearnersInClass(TestApp):
    def test_get_number_of_learners_in_class(self):

        response = self.client.get(
            "/enrolment/number/SPM G1", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": 2
        }
        )


class TestGetNumberOfLearnersInClassTaughtByTrainer(TestApp):
    def test_get_number_of_learners_in_class_taught_by_trainer(self):

        response = self.client.get(
            "/enrolment/size/13/SPM", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": {
                "SPM G1": 2,
                "SPM G2": 1
            }
        }
        )


class TestGetNumberOfLearnersInClassesOfACourse(TestApp):
    def test_get_number_of_learners_in_classes_of_a_course(self):

        response = self.client.get(
            "/enrolment/size/SPM", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": {
                "SPM G1": 2,
                "SPM G2": 1
            }
        }
        )


class TestGetQualifiedLearnersOfAClass(TestApp):
    def test_get_qualified_learners_of_a_class(self):

        response = self.client.get(
            "/enrolment/qualifiedlearners/OOP G1", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [{
                "learnerId": 5,
                "learnerName": 'Nicki'
            }
            ]
        }
        )


class TestEnrolLearners(TestApp):
    def test_enrol_learners(self):

        request_body = {
            'classId': self.course3class1.classId,
            'learnerIds': [self.learner1.userId, self.learner2.userId]
        }

        response = self.client.post("/enrolment/enrolLearners",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            "data": [
                {
                    "classId": "CT G1",
                    "completedClass": False,
                    "courseId": "CT",
                    "learnerId": 1,
                    "sectionsCompleted": 0,
                    "status": "ACCEPTED",
                    "totalNumSections": 1
                },
                {
                    "classId": "CT G1",
                    "completedClass": False,
                    "courseId": "CT",
                    "learnerId": 2,
                    "sectionsCompleted": 0,
                    "status": "ACCEPTED",
                    "totalNumSections": 1
                }
            ]
        }
        )

    # def test_enrol_enrolledLearners(self):


class TestRemoveLearner(TestApp):
    def test_remove_learner(self):

        request_body = {
            'classId': self.course1class1.classId,
            'learnerId': self.learner1.userId
        }

        response = self.client.delete("/removeLearner",
                                      data=json.dumps(request_body),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "message": "Learner Withdrawn"
        }
        )

    # Remove non-existent learner


class TestSelfEnrolLearner(TestApp):
    def test_self_enrol_learner(self):

        request_body = {
            'classId': self.course3class1.classId,
            'learnerId': self.learner1.userId
        }

        response = self.client.post("/enrolLearner",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            "courseId": 'CT',
            "classId": 'CT G1',
            "learnerId": 1,
            "totalNumSections": 1,
            "status": "PENDING",
            "completedClass": False,
            "sectionsCompleted": 0
        }
        )


class TestWithdrawLearner(TestApp):
    def test_withdraw_learner(self):

        request_body = {
            'courseId': self.course2class1.courseId,
            'learnerId': self.learner3.userId
        }

        response = self.client.delete("/withdrawLearner",
                                      data=json.dumps(request_body),
                                      content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "message": "Learner Withdrawn"
        }
        )

        # Withdraw accepted


class TestPendingEnrolments(TestApp):
    def test_pending_enrolments(self):

        response = self.client.get(
            "/viewPendingEnrolments?classId=OOP G1", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "message": "Pending enrolments found",
            "data": [
                {
                    "classId": "OOP G1",
                    "completedClass": False,
                    "courseId": "OOP",
                    "learnerId": 3,
                    "learnerName": "Ezra",
                    "sectionsCompleted": 0,
                    "status": "PENDING",
                    "totalNumSections": 10
                }
            ]
        }
        )


class TestUpdateEnrolmentRequests(TestApp):
    def test_updateEnrolmentRequests(self):
        request_body = {
            'classId': 'OOP G1',
            'learnerIds': [3],
            'status': 'ACCEPTED',
        }

        response = self.client.put("/updateEnrolmentRequests",
                                   data=json.dumps(request_body),
                                   content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {'data': [{'classId': 'OOP G1',
                                    'completedClass': False,
                                    'courseId': 'OOP',
                                    'learnerId': 3,
                                    'sectionsCompleted': 0,
                                    'status': 'ACCEPTED',
                                    'totalNumSections': 10}],
                          'message': 'enrolment updated'}
                         )


class TestViewUserEnrolmentStatus(TestApp):
    def test_viewUserEnrolmentStatus(self):

        response = self.client.get("/viewUserEnrolmentStatus?learnerId=3&courseId=OOP",
                                   )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {'enrolmentStatus': 'PENDING'}
                         )


class TestGetEnrolmentsInProgress(TestApp):
    def test_get_Enrolments_In_Progress(self):

        response = self.client.get(
            "/getEnrolmentsInProgress?learnerId=4", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'data': [
                {'classId': 'SPM G2',
                 'completedClass': False,
                 'courseId': 'SPM',
                 'courseName': 'Software Project Management',
                 'endDate': '2021-10-12',
                 'endTime': '10:00',
                 'learnerId': 4,
                 'sectionsCompleted': 0,
                 'startDate': '2021-10-11',
                 'startTime': '01:00',
                 'status': 'ACCEPTED',
                 'totalNumSections': 10}],
            'message': 'Current enrolments found'})

        # if no pending enrolments


class TestGetLearnerPendingEnrolments(TestApp):
    def test_get_Learner_Pending_Enrolments(self):

        response = self.client.get(
            "/getLearnerPendingEnrolments?learnerId=3", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [
                {
                    "classId": "OOP G1",
                    "completedClass": False,
                    "courseId": "OOP",
                    "courseName": "Object Oriented Programming",
                    "learnerId": 3,
                    "sectionsCompleted": 0,
                    "status": "PENDING",
                    "totalNumSections": 10
                }
            ],
            "message": "Pending enrolments found"
        }
        )

        # if no pending enrolments


class TestGetCompletedEnrolments(TestApp):
    def test_get_Completed_Enrolments(self):

        response = self.client.get(
            "/getCompletedEnrolments?learnerId=5", content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "data": [
                {
                    "classId": "SPM G2",
                    "completedClass": True,
                    "courseId": "SPM",
                    "courseName": "Software Project Management",
                    "learnerId": 5,
                    "sectionsCompleted": 0,
                    "status": "ACCEPTED",
                    "totalNumSections": 10
                }
            ],
            "message": "Completed enrolments found"
        }
        )

        # if no completed enrolments


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


class TestGetEnrolmentDetails(TestApp):
    def test_getEnrolmentDetails(self):
        request_body = {
            'classId': 'OOP G1',
            'learnerId': 3
        }

        response = self.client.post("/getEnrolmentDetails",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {'classId': 'OOP G1',
                          'completedClass': False,
                          'courseId': 'OOP',
                          'learnerId': 3,
                          'sectionsCompleted': 0,
                          'status': 'PENDING',
                          'totalNumSections': 10}
                         )

    def test_getEnrolmentDetails_noEnrolment(self):
        request_body = {
            'classId': 'SPM G2',
            'learnerId': 3
        }
        response = self.client.post("/getEnrolmentDetails",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {"message": "no enrolment"}
                         )


if __name__ == '__main__':
    unittest.main()
