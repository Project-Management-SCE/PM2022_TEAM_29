pipeline {
agent {
		        docker {
		            image 'python:3.8'
		

		        }
		    }
		    stages {
		        stage('build') {
		            steps {
		                withEnv(["HOME=${env.WORKSPACE}"]) {
					
		                    sh "django-admin startproject Giving"
		                }
		            }
		        }
		        stage('test') {
		            steps {
		                withEnv(["HOME=${env.WORKSPACE}"]) {
		                    dir("PM2022_TEAM_29"){
		                        sh "python manage.py test"
		                    }
		                }
		            }
		        }
		     stage('coverage') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("PM2022_TEAM_29"){
                        sh "python -m coverage run --include='app/*' manage.py test"
                        sh "python -m coverage report"
                    }
                }
            }
        }
		    
			    stage('pylint') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("PM2022_TEAM_29/Giving"){
			sh "python -m pylint settings.py"
			sh "python -m pylint urls.py"
                        sh "python -m pylint _init_.py"
		    }
		    dir("PM2022_TEAM_29/app"){
                        sh "python -m pylint admin.py"
		    }
		}
	    }
			    }
			    
		    }
}
