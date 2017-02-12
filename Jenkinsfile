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
	sh 'git config --global user.email "0851967@hr.nl"'
	sh 'git config --global user.name "LambdaNL"'
	sh 'git remote set-url origin git@github.com:Datastreamx/learn-english.git'	
	sh 'git checkout master'
	sh 'git pull origin master'
	sh 'git merge origin/development'
	sh 'git push origin master'
        }
        failure {
            sh 'echo Build failed!'
        }
    }
}
