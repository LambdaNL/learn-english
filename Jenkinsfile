pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('Test') {
            steps {
		sh 'pip3 install -r ./requirements.txt'
                sh 'python3 ./learn_english/manage.py test'
		sh 'python3 ./learn_english/manage.py check'
            }
        }
    }
post {
        success {
            sh 'git merge origin/development'
	    sh 'git commit -am "Merged development branch to master"'
    	    sh 'git push origin master'
        }
        failure {
            sh 'echo Build failed!'
        }
    }
}
