pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('Test') {
            steps {
		sh 'pip3 install -r ./requirements.txt'
		sh 'cd learn_english/'
		    sh 'pwd'
                sh 'python3 manage.py test'
		sh 'python3 manage.py check'
            }
        }
    }
}
