pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 manage.py test'
 		sh 'python3 manage.py runserver'
            }
        }
    }
    post {
        success {
            sh 'echo push to master'
        }
        failure {
            sh 'echo This will run only if failed'
        }
    }
}