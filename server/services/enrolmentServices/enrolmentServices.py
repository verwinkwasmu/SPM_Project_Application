from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from allClasses import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}
db = SQLAlchemy(app)

CORS(app)

# get learnerId + learnerName enrolled in a class


@app.route("/enrolment/<string:classId>", methods=['GET'])
def getLearnersInClass(classId):

    class_existence = Class.query.filter(Class.classId == classId).all()

    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404

    enrolments = Enrolment.query.filter(
        (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).all()

    learner_name_list = []
    for enrolment in enrolments:
        learner_object = Learner.query.filter(
            Learner.userId == enrolment.to_dict()['learnerId']).first()
        learner_name_list.append(learner_object.to_dict()['employeeName'])

    enrolment_list_dic = []
    n = 0
    for enrolment in enrolments:
        learner_dict = {}
        learner_dict['learnerId'] = enrolment.to_dict()['learnerId']
        learner_dict['learnerName'] = learner_name_list[n]
        enrolment_list_dic.append(learner_dict)
        n += 1

    if not enrolments:
        return jsonify({
            "message": "No learners found.",
            "data": []
        }), 200
    return jsonify(
        {
            "data": enrolment_list_dic
        }
    ), 200

# get number of learners enrolled in a class


@app.route("/enrolment/number/<string:classId>", methods=['GET'])
def getNumberOfLearnersInClass(classId):
    class_existence = Class.query.filter(Class.classId == classId).all()

    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404

    num_enrolments = Enrolment.query.filter(
        (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

    return jsonify(
        {
            "data": num_enrolments
        }
    ), 200


# get number of learners enrolled in a classes taught by a Trainer
@app.route("/enrolment/size/<string:trainerId>/<string:courseId>", methods=['GET'])
def getCurrentClassSizeTrainer(trainerId, courseId):

    trainer_existence = Trainer.query.filter(Trainer.userId == trainerId).all()
    # check if trainer exists
    if not trainer_existence:
        return jsonify({
            "message": "Trainer not found."
        }), 404

    course_existence = Course.query.filter(Course.courseId == courseId).all()
    # check if course exists
    if not course_existence:
        return jsonify({
            "message": "Course not found."
        }), 405

    trainerCourseClasses = Class.query.filter(
        (Class.trainerAssigned == trainerId) & (Class.courseId == courseId)).all()

    classList = []
    for trainerCourseClass in trainerCourseClasses:
        classList.append(trainerCourseClass.classId)

    classDict = {}
    for classId in classList:
        class_existence = Class.query.filter(Class.classId == classId).all()

        # check if class exists
        if not class_existence:
            return jsonify({
                "message": "No class found."
            }), 406

        num_enrolments = Enrolment.query.filter(
            (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

        classDict[classId] = num_enrolments

    return jsonify(
        {
            "data": classDict
        }
    ), 200

# get number of learners enrolled in classes of a course


@app.route("/enrolment/size/<string:courseId>", methods=['GET'])
def getCurrentClassSize(courseId):

    course_existence = Course.query.filter(Course.courseId == courseId).all()
    # check if course exists
    if not course_existence:
        return jsonify({
            "message": "Course not found."
        }), 405

    CourseClasses = Class.query.filter(Class.courseId == courseId).all()

    classList = []
    for CourseClass in CourseClasses:
        classList.append(CourseClass.classId)

    classDict = {}
    for classId in classList:
        num_enrolments = Enrolment.query.filter(
            (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()

        classDict[classId] = num_enrolments

    return jsonify(
        {
            "data": classDict
        }
    ), 200

# get learnerId + learnerName of qualified learners to be enrolled into a class


@app.route("/enrolment/qualifiedlearners/<string:classId>", methods=['GET'])
def getQualifiedLearnersOfClass(classId):
    class_existence = Class.query.filter(Class.classId == classId).first()
    # check if class exists
    if not class_existence:
        return jsonify({
            "message": "No class found."
        }), 404
    courseId = class_existence.courseId

    # create list of userid of those who are already enrolled
    enrolments = Enrolment.query.filter(Enrolment.courseId == courseId).all()
    enrolment_list = []
    for enrolment in enrolments:
        enrolment_list.append(enrolment.learnerId)
    # create list of userid of those who are not enrolled into class
    learners_not_enrolled = Learner.query.filter(
        Learner.userId.notin_(enrolment_list)).all()
    intermediate_qualified_learnerIds = []
    for learner_not_enrolled in learners_not_enrolled:
        intermediate_qualified_learnerIds.append(learner_not_enrolled.userId)

    # get prequisite course
    course_id = class_existence.courseId
    this_course = Course.query.filter(Course.courseId == course_id).first()
    pre_requisiteId = (this_course.prerequisites).split(':')[0]

    if pre_requisiteId != "":
        qualified_enrolment_objects = Enrolment.query.filter(Enrolment.learnerId.in_(
            intermediate_qualified_learnerIds), Enrolment.courseId == pre_requisiteId, Enrolment.completedClass == True).all()

        qualified_learnerIds = []
        for qualified_enrolment_object in qualified_enrolment_objects:
            qualified_learnerIds.append(qualified_enrolment_object.learnerId)

        qualified_learner_objects = Learner.query.filter(
            Learner.userId.in_(qualified_learnerIds)).all()

    else:
        qualified_learner_objects = learners_not_enrolled

    # create list of dictionary for qualified_learners
    qualified_learners = []
    for qualified_learner_object in qualified_learner_objects:
        learner_dict = {}
        learner_dict['learnerId'] = qualified_learner_object.userId
        learner_dict['learnerName'] = qualified_learner_object.employeeName
        qualified_learners.append(learner_dict)

    return jsonify(
        {
            "data": qualified_learners
        }
    ), 200

# enrol learners into class


@app.route("/enrolment", methods=['POST'])
def create_enrolment():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('classId', 'learnerIds')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classCheck = Class.query.filter_by(classId=data['classId']).first()

    if not classCheck:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate learner
    learner_Ids = data['learnerIds']
    enrolment_objects = []
    enrolment_objects2 = []
    for learner_Id in learner_Ids:
        learner = Learner.query.filter_by(userId=learner_Id).first()
        if not learner:
            return jsonify({
                "message": "There is an invalid learner."
            }), 502

        # (3): Check for enrolment record
        enrolments = Enrolment.query.filter(
            Enrolment.classId == data["classId"],
            Enrolment.learnerId == learner_Id
        ).first()

        if enrolments:
            return jsonify({
                "message": "Enrolment already added."
            }), 503

        # Compute total number of Sections in the class
        numSections = Section.query.filter(
            Section.classId == data["classId"]).count()
        class_object = Class.query.filter(
            Class.classId == data["classId"]).first()
        course_Id = class_object.to_dict()['courseId']
        enrolment = Enrolment(
            courseId=course_Id,
            classId=data['classId'],
            learnerId=learner_Id,
            totalNumSections=numSections,
            status='ACCEPTED'
        )
        enrolment_objects.append(enrolment)
        enrolment_objects2.append(enrolment.to_dict())

    # return jsonify({
    #         "data": enrolment_objects
    #     }), 201

    # (4): Commit to DB
    try:
        db.session.add_all(enrolment_objects)
        db.session.commit()
        return jsonify({
            "data": enrolment_objects2
        }), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504


# Remove learner from course
@app.route("/removeLearner", methods=['DELETE'])
def removeLearner():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classCheck = Class.query.filter_by(classId=data['classId']).first()

    if not classCheck:
        return jsonify({
            "message": "Class not valid."
        }), 501

    # (2): Validate learner
    learner = Learner.query.filter_by(userId=data['learnerId']).first()

    if not learner:
        return jsonify({
            "message": "Learner not valid."
        }), 502

    # (3): Create enrolment record
    enrolment = Enrolment.query.filter(
        Enrolment.classId == data["classId"],
        Enrolment.learnerId == data['learnerId']
    ).first()

    if not enrolment:
        return jsonify({
            "message": "Enrolment does not exist."
        }), 503

    # (4): Commit to DB
    try:
        db.session.query(Enrolment).filter(
            Enrolment.classId == data['classId'], Enrolment.learnerId == data['learnerId']).delete()
        db.session.commit()
        return jsonify({
            "message": "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Self-enrolling of learner


@app.route('/enrolLearner', methods=['POST'])
def enrolLearner():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # Compute total number of Sections in the class
    numSections = Section.query.filter(
        Section.classId == data["classId"]).count()
    class_object = Class.query.filter(
        Class.classId == data["classId"]).first()
    course_Id = class_object.courseId

    enrolment = Enrolment(
        courseId=course_Id,
        classId=data['classId'],
        learnerId=data['learnerId'],
        totalNumSections=numSections,
        status="PENDING"
    )
    # Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# learner withdraw from course


@app.route("/withdrawLearner", methods=['DELETE'])
def withdrawLearner():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('courseId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    enrolment = db.session.query(Enrolment).filter(Enrolment.learnerId == data['learnerId'], Enrolment.courseId == data["courseId"], Enrolment.status.in_(['PENDING', 'ACCEPTED'])).first()

    if not enrolment:
        return jsonify({
            "message": "Enrolment does not exist."
        }), 503
        
    try:
        db.session.delete(enrolment)
        db.session.commit()
        return jsonify({
            "message": "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# VIEW ALL ENROLMENT BASED ON STATUS
@app.route('/viewPendingEnrolments')
def getPendingEnrolments():
    classId = request.args.get('classId')        

    pending_enrolments = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.status=="PENDING").all()

    if not pending_enrolments:
        return jsonify({
            "message": "No pending enrolments found.",
            "data": []
        }), 200
    return jsonify(
        {
            "message": "Pending enrolments found",
            "data": [enrolment.to_dict() for enrolment in pending_enrolments]
        }
    ), 200


# ACCEPT OR REJECT PENDING ENROLMENT REQUESTS
@app.route('/updateEnrolmentRequest', methods=['PUT'])
def updateEnrolmentRequest():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId', 'status')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    learnerId = data['learnerId']
    classId = data['classId']
    status = data['status']

    # update enrolment record
    enrolmentObj = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.learnerId==learnerId).first()
    enrolmentObj.status = status

    try:
        db.session.merge(enrolmentObj)
        db.session.commit()
        return jsonify({
            "data": enrolmentObj.to_dict(),
            "message": "enrolment updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

# Award badge upon completing 
@app.route('/updateCompletionStatus', methods=['PUT'])
def updateCompletionStatus():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    learnerId = data['learnerId']
    classId = data['classId']

    # update enrolment record
    enrolmentObj = Enrolment.query.filter(Enrolment.classId==classId, Enrolment.learnerId==learnerId).first()

    course_id = enrolmentObj.to_dict()['courseId']
    courseObj = Course.query.filter(Course.courseId==course_id).first()

    if enrolmentObj.completedClass: 
        return jsonify({
            "message": "Learner has already completed the class"
        }), 501

    enrolmentObj.completedClass = True
    # course_id = enrolmentObj.courseId
    # courseObj = Course.query.filter(Course.courseId==course_id).first()

    try:
        db.session.merge(enrolmentObj)
        db.session.commit()
        return jsonify({
            "data": courseObj.to_dict(),
            "message": "enrolment updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

# get user's awarded badges
@app.route("/awardedBadges")
def awardedBadges():
    learner_id = request.args.get('learnerId')

    # (1): Validate learner
    learnerCheck = Learner.query.filter(Learner.userId==learner_id).first()

    if not learnerCheck:
        return jsonify({
            "message": "Learner does not exist"
        }), 501

    badges = Enrolment.query.filter((Enrolment.learnerId==learner_id) & (Enrolment.completedClass==True)).all()

    awarded_badge = []
    for badge in badges: 
        badgeDict = {}
        badgeDict['courseId'] = badge.courseId
        courseObject = Course.query.filter(Course.courseId==badge.courseId).first()
        badgeDict['courseName'] = courseObject.courseName
        awarded_badge.append(badgeDict)

    if len(awarded_badge) == 0: 
        return jsonify({
            "message": "Learner has not completed any courses",
            "data": []
        }), 200
    
    return jsonify(
        {
            "data": awarded_badge
        }
    ), 200

@app.route('/viewUserEnrolmentStatus')
def viewUserEnrolmentStatus():
    learnerId = request.args.get('learnerId')
    courseId = request.args.get('courseId')

    enrolment = Enrolment.query.filter(
        (Enrolment.learnerId==learnerId) & (Enrolment.courseId==courseId) & ((Enrolment.status=="ACCEPTED") | (Enrolment.status=="PENDING"))).first()
    if enrolment:
        return jsonify({
            "enrolmentStatus": enrolment.status
        }), 200
    else:
        return jsonify({
            "enrolmentStatus": "NOT ENROLLED"
        })
        # num_enrolments = Enrolment.query.filter(
        #     (Enrolment.classId == classId) & (Enrolment.completedClass == False) & (Enrolment.status == 'ACCEPTED')).count()
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
