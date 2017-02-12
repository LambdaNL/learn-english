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
		sh 'git config --global user.email "0851967@hr.nl"'
 		sh 'git config --global user.name "HRO"'
    		sh 'git commit -m "Merged development branch to master"'
    	    sh 'git push origin master'
        }
        failure {
            sh 'echo Build failed!'
        }
    }
}
