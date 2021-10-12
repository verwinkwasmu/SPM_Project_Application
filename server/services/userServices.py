from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(120))
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
    
    def verify_password(self, password):
        if check_password_hash(self.password, password):
            return True
        return False

class Learner(User):
    __tablename__ = 'learner'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'learner',
    }

class Trainer(User):
    __tablename__ = 'trainer'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'trainer',
    }

class Hr(User):
    __tablename__ = 'hr'

    userId = db.Column(db.Integer, db.ForeignKey('user.userId'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'hr',
    }


db.create_all()

# create user
@app.route("/createUser", methods=['POST'])
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
            "message": "User exists."
        }), 404
    
    if data['userType'] == 'Trainer':
        new_user = Trainer(email=data['email'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'])
    elif data['userType'] == 'Learner':
        new_user = Learner(email=data['email'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'])
    elif data['userType'] == 'HR':
        new_user = Hr(email=data['email'], userName=data['userName'], password=generate_password_hash(data['password'], method="sha256"), userType=data['userType'])
    
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
    if not all(key in data.keys() for
               key in ('email', 'password')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    
    user = User.query.filter_by(email=data['email']).first()
    
    # retrieve password
    password = data['password']
    
    if not user or not user.verify_password(password):
        return jsonify({
            "message": "Person not found."
        }), 404
    
    else:
        return jsonify(
            {
                "data": user.to_dict()
            }
        ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)