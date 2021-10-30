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
        (Enrolment.classId == classId) & (Enrolment.completedClass == False)).all()

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
        (Enrolment.classId == classId) & (Enrolment.completedClass == False)).count()

    return jsonify(
        {
            "data": num_enrolments
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
    pre_requisite = this_course.prerequisites

    if pre_requisite != "":
        qualified_enrolment_objects = Enrolment.query.filter(Enrolment.learnerId.in_(
            intermediate_qualified_learnerIds), Enrolment.courseId == pre_requisite, Enrolment.completedClass == True).all()

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

        # (3): Create enrolment record
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
            totalNumSections=numSections
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
    #Commit to DB
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
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('classId', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    enrolment = Enrolment.query.filter(
        Enrolment.classId == data["classId"],
        Enrolment.learnerId == data['learnerId'],
        Enrolment.status == "ACCEPTED"
    ).first()

    if not enrolment:
        return jsonify({
            "message": "Enrolment does not exist."
        }), 503

    try:
        db.session.query(Enrolment).filter(
            Enrolment.classId == data['classId'], Enrolment.learnerId == data['learnerId'], Enrolment.status=="ACCEPTED").delete()
        db.session.commit()
        return jsonify({
            "message": "Learner Withdrawn"
        }), 200

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
