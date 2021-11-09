pipeline {
agent any
stages {
    stage ('Test'){

        steps {
            sh '''
            python3 -m venv env
            source env/bin/activate
            pip install -r requirements.txt
            pwd
            python server/tdd/unit_tests.py
            python server/tdd/quiz_integration_tests.py
            python server/tdd/question_integration_tests.py
            python server/tdd/enrolment_integration_tests.py
            python server/tdd/course_integration_tests.py
            python server/tdd/class_integration_tests.py
            '''
        }
    }
}
}