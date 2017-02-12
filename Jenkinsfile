pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('Test') {
            steps {
                sh 'python3 ./learn_english/manage.py test'
		sh 'python3 ./learn_english/manage.py runserver'
            }
        }
    }
}
