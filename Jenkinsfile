
pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
		               sh 'pip install -r requirements.txt'
		               sh 'pip install --user flask'
                        sh 'pip install --user pyrebase'
                        sh 'pip install --user Flask-WTF'
                        sh 'pip install --user email_validator'
                        sh 'pip install --user --upgrade firebase-admin'
                        sh 'pip install --user json-e'
                        sh 'pip install --user requests --upgrade'
                        sh 'pip install --user Flask-JSGlue'
                        sh 'pip install --user pyflakes'
					}
			}
        }
        stage(' unit_tests') {
            agent {
                docker {
                    image 'python:3.7'
                }
            }
            steps {
		            withEnv(["HOME=${env.WORKSPACE}"]) {
                sh ' python -m test'
		      }
			}
        }
        stage('test coverage') {
        agent {
                docker {
                    image 'python:3.7'
                }
            }
			steps {

					withEnv(["HOME=${env.WORKSPACE}"]) {

						sh "python -m coverage report forms.py"

					}


			}
		}
		        stage(' bug and quality checker') {
        agent {
                docker {
                    image 'python:3.7'
                }
            }
			steps {

					withEnv(["HOME=${env.WORKSPACE}"]) {

						sh "python -m pylint App.py"
					}

			}
		}
	}
}
