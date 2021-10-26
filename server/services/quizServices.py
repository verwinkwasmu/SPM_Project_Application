from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from allClasses import *
from sqlalchemy.sql import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:admin123@spm-database.cjmo3wwh5ar9.ap-southeast-1.rds.amazonaws.com:3306/spm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}
db = SQLAlchemy(app)

CORS(app)

# Get all questions in a Quiz
@app.route("/quiz/<string:classId>/<string:sectionId>/<string:quizId>", methods=['GET'])
def getAllQuestions(classId, sectionId, quizId):
    quiz = Quiz.query.filter(
                                Quiz.sectionId == sectionId, 
                                Quiz.classId == classId,
                                Quiz.quizId == quizId
                            ).first()
    
    # check if class exists 
    if not quiz:
        return jsonify({
            "message": "No quiz found."    
        }), 404

    questions = Question.query.filter(
                                        Question.sectionId == sectionId, 
                                        Question.classId == classId,
                                        Question.quizId == quizId
                                    ).all()

    if not questions:
        return jsonify({
            "message": "No learners found."
        }), 404

    return jsonify(
        {
            "data": [question.to_dict() for question in questions]
        }
    ), 200

# create quiz in a section
@app.route("/createQuiz", methods=['POST'])
def createQuiz():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkQuiz = Quiz.query.filter(
                            Quiz.sectionId == data["sectionId"], 
                            Quiz.classId == data['classId'],
                            Quiz.quizId == data['quizId']
                        ).first()


    if checkQuiz:
        return jsonify({
            "message": "Quiz already exists."
        }), 501


    quiz = Quiz(
            sectionId = data['sectionId'],
            classId = data['classId'],
            quizId = data['quizId']
        )

    # (4): Commit to DB
    try:
        db.session.add(quiz)
        db.session.commit()
        return jsonify(quiz.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Get a specific question in a quiz of a section
@app.route("/question/<string:classId>/<string:sectionId>/<string:quizId>/<string:questionId>", methods=['GET'])
def getQuestion(classId, sectionId, quizId, questionId):

    question = Question.query.filter(
                                Question.sectionId == sectionId, 
                                Question.classId == classId,
                                Question.quizId == quizId,
                                Question.questionId == questionId
                            ).first()
    
    # check if question exists 
    if not question:
        return jsonify({
            "message": "No question found."    
        }), 404

    return jsonify(question.to_dict()), 200

# create a question for a quiz
@app.route("/createQuestion", methods=['POST'])
def createQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId', 'question', 'option', 'answer', 'explanation')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    checkQuestion = Question.query.filter(
                                Question.sectionId == data["sectionId"], 
                                Question.classId == data['classId'],
                                Question.quizId == data['quizId'],
                                Question.questionId == data['questionId']
                            ).first()

    if checkQuestion:
        return jsonify({
            "message": "Question already exists"
        }), 501


    question = Question(
            sectionId = data['sectionId'],
            classId = data['classId'],
            quizId = data['quizId'],
            questionId = data['questionId'],
            question = data['question'],
            option = data['option'],
            answer = data['answer'],
            explanation = data['explanation']
        )
    print(question.to_dict())

    # (4): Commit to DB
    try:
        db.session.add(question)
        db.session.commit()
        return jsonify(question.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to commit to database.",
            "data": str(request.get_data())
        }), 504

# Update a specific Question in a quiz
@app.route("/updateQuestion", methods=['PUT'])
def updateQuestion():
    # retrieve data
    data = request.get_json()

    if not all(key in data.keys() for
               key in ('sectionId', 'classId', 'quizId', 'questionId')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate Section
    question = Question.query.filter(
                                Question.sectionId == data["sectionId"], 
                                Question.classId == data['classId'],
                                Question.quizId == data['quizId'],
                                Question.questionId == data['questionId']
                            ).first()

    if not question:
        return jsonify({
            "message": "Question is not valid"
        }), 501
    
    # (3): Update Class DB record
    if 'question' in data:
        question.question = data['question']
    if 'option' in data:
        question.option = data['option']
    if 'answer' in data:
        question.answer = data['answer']
    if 'explanation' in data:
        question.explanation = data['explanation']
        
    # (4): Commit to DB
    try:
        db.session.merge(question)
        db.session.commit()
        return jsonify({
            "data": question.to_dict(),
            "message": "Question updated"
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)