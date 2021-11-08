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
            python server/services/unit_tests.py
            '''
        }
    }
}
}