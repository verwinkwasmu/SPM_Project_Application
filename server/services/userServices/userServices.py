from flask import Flask, json, request, jsonify, current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from allClasses import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

# create user
@app.route("/createUser", methods=['POST'])
def create_trainer():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('employeeName', 'userName', 'email',
                       'password', 'userType', 'designation', 'department')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    user = User.query.filter_by(email=data['email']).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({
            "message": "User exists."
        }), 404
    
    if data['userType'] == 'Trainer':
        new_user = Trainer(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    elif data['userType'] == 'Learner':
        new_user = Learner(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    elif data['userType'] == 'HR':
        new_user = Hr(email=data['email'], employeeName=data['employeeName'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'], designation=data['designation'], department=data['department'])
    print(new_user.to_dict())
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# get trainer based on id or get all trainers
@app.route("/getTrainers")
def trainers():
    search_id = request.args.get('userId')
    if search_id:
        trainer_list = Trainer.query.filter(Trainer.userId.contains(search_id))
    else:
        trainer_list = Trainer.query.all()
    return jsonify(
        {
            "data": [trainer.to_dict() for trainer in trainer_list]
        }
    ), 200

# get learner based on id or get all learners
@app.route("/getLearners")
def learners():
    search_id = request.args.get('userId')
    if search_id:
        learner_list = Learner.query.filter(Learner.userId.contains(search_id))
    else:
        learner_list = Learner.query.all()
    return jsonify(
        {
            "data": [learner.to_dict() for learner in learner_list]
        }
    ), 200

# get hr based on id or get all hrs
@app.route("/getHrs")
def hrs():
    search_id = request.args.get('userId')
    if search_id:
        hr_list = Hr.query.filter(Hr.userId.contains(search_id))
    else:
        hr_list = Hr.query.all()
    return jsonify(
        {
            "data": [hr.to_dict() for hr in hr_list]
        }
    ), 200
   
# login to user account
@app.route("/login", methods=['POST'])
def login():

    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not data['userName']:
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # data_userName = data['userName']
    
    user = User.query.filter_by(userName=data['userName']).first()
    
    if not user:
        return jsonify({
            "message": "Person not found."
        }), 404
    
    else:
        return jsonify(
            {
                "data": user.to_dict()
            }
        ), 200

# set learner's course material as completed
@app.route('/setFileCompleted', methods=['POST'])
def setFileCompleted():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('learnerId', 'fileId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    file = File(learnerId=data['learnerId'], fileId=data['fileId'], completed=True)
    
    try:
        db.session.add(file)
        db.session.commit()
        return jsonify(file.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
        
@app.route('/getCompletedFiles', methods=['POST'])
def getCompletedFiles():
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('courseId', 'className', 'sectionName', 'learnerId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    courseId = data['courseId']
    className = data['className']
    sectionName = data['sectionName']
    learnerId = data['learnerId']

    file_path = f"{courseId}/{className}/{sectionName}/"
    
    files = File.query.filter(File.fileId.contains(file_path), File.learnerId==learnerId).all()

    if files:
        return jsonify(
            {
                "data": [file.fileId for file in files]
            }
        ), 200
    else:
        return jsonify(
            {
                "data": [],
                "message": "no files completed yet"
            }
        ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)