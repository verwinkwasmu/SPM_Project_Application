from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/is212_example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    userType = db.Column(db.String(50))
    

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Learner(User):
    __tablename__ = 'learner'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    userName = db.Column(db.String, db.ForeignKey('user.userName'))
    email = db.Column(db.String, db.ForeignKey('user.email'))

    __mapper_args__ = {
        'polymorphic_identity': 'learner',
    }

class Trainer(User):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    userName = db.Column(db.String, db.ForeignKey('user.userName'))
    email = db.Column(db.String, db.ForeignKey('user.email'))

    __mapper_args__ = {
        'polymorphic_identity': 'trainer',
    }

class Hr(User):
    __tablename__ = 'hr'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    userName = db.Column(db.String, db.ForeignKey('user.userName'))
    email = db.Column(db.String, db.ForeignKey('user.email'))

    __mapper_args__ = {
        'polymorphic_identity': 'hr',
    }


db.create_all()

## TRAINER ROUTES ##
# create trainer
@app.route("/createTrainer", methods=['POST'])
def create_trainer():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('userName', 'email',
                       'password', 'userType')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    user = User.query.filter_by(email=data['email']).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({
            "message": "Trainer exists."
        }), 404

    trainer = Trainer(**data)
    
    try:
        db.session.add(trainer)
        db.session.commit()
        return jsonify(trainer.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# get trainer based on id or get all trainers
@app.route("/getTrainers")
def doctors():
    search_id = request.args.get('id')
    if search_id:
        trainer_list = Trainer.query.filter(Trainer.id.contains(search_id))
    else:
        trainer_list = Trainer.query.all()
    return jsonify(
        {
            "data": [trainer.to_dict() for trainer in trainer_list]
        }
    ), 200

## LEARNER ROUTES ##
# create learner
@app.route("/createLearner", methods=['POST'])
def create_learner():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('userName', 'email',
                       'password', 'userType')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    user = User.query.filter_by(email=data['email']).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({
            "message": "Learner exists."
        }), 404

    learner = Learner(**data)
    
    try:
        db.session.add(learner)
        db.session.commit()
        return jsonify(learner.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# get learner based on id or get all learners
@app.route("/getLearners")
def learners():
    search_id = request.args.get('id')
    if search_id:
        learner_list = Learner.query.filter(Learner.id.contains(search_id))
    else:
        learner_list = Learner.query.all()
    return jsonify(
        {
            "data": [learner.to_dict() for learner in learner_list]
        }
    ), 200

## HR ROUTES ##
# create hr
@app.route("/createHr", methods=['POST'])
def create_hr():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('userName', 'email',
                       'password', 'userType')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    user = User.query.filter_by(email=data['email']).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({
            "message": "HR exists."
        }), 404

    hr = Hr(**data)

    try:
        db.session.add(hr)
        db.session.commit()
        return jsonify(hr.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# get hr based on id or get all hrs
@app.route("/getHrs")
def hrs():
    search_id = request.args.get('id')
    if search_id:
        hr_list = Hr.query.filter(Hr.id.contains(search_id))
    else:
        hr_list = Hr.query.all()
    return jsonify(
        {
            "data": [hr.to_dict() for hr in hr_list]
        }
    ), 200



# create User Account
# @app.route("/createUser", methods=['POST'])
# def createUser():

#     # retrieved data
#     data = request.get_json()

#     # check if proper data is sent
#     if not all(key in data.keys() for
#                key in ('userName, email', 'password', 'userType')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500
    
#     user = User.query.filter_by(email=data['email']).first()

#     if user: # if a user is found, we want to redirect back to signup page so user can try again
#         return jsonify({
#             "message": "User exists."
#         }), 404
    
#     # creating id based on userType
#     userType = data['userType']

#     if userType == 'Learner':
#         id = 'L-' + str(uuid.uuid4())
#     elif userType == 'Trainer':
#         id = 'T-' + str(uuid.uuid4())
#     elif userType == 'HR':
#         id = 'H-' + str(uuid.uuid4())

#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_user = User(id=id, email=data['email'], userName=data['userName'], password=generate_password_hash(data['password'], method='sha256'), userType=userType)
    
#     # add the new user to the database
#     try:
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify(new_user.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500

   
# login to user account
@app.route("/login", methods=['POST'])
def login():

    # retrieved data
    data = request.get_json()

    # check if proper data is sent
    if not all(key in data.keys() for
               key in ('email', 'password')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    user = User.query.filter_by(email=data['email']).first()

    # retrieve password
    password = data['password']

    # check if user exists and validate password
    # for hashed passwords
    # if not user or not check_password_hash(user.password, password):
    #     return jsonify({
    #         "message": "Person not found."
    #     }), 404
    if not user or not user.password == password:
        return jsonify({
            "message": "Person not found or incorrect password."
        }), 404

    return jsonify(
        {
            "data": user.to_dict()
        }
    ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)