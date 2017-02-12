pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('Test') {
            steps {
		sh 'cd learn_english/'
                sh 'python3 manage.py test'
		sh 'python3 manage.py runserver'
            }
        }
    }
}