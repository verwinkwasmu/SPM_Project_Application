pipeline {
agent any
stages {
    stage('build') {
  steps {
    sh 'pip install -r requirements.txt'
  }
}
    stage ('Test'){
        steps {
            sh 'server/services/python unit-tests.py'
        }
    }
}
}