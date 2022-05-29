
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

						sh "python -m coverage run App.py test"

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


// pipeline {
//   agent {
//       docker {
//           image 'python:3.7.2' } }
//   stages {
//     stage('Build') {
//       steps {
//         withEnv(["HOME=${env.WORKSPACE}"]){
//             sh 'pip install --user flask'
//             sh 'pip install --user pyrebase'
//             sh 'pip install --user Flask-WTF'
//             sh 'pip install --user email_validator'
//             sh 'pip install --user --upgrade firebase-admin'
//             sh 'pip install --user json-e'
//             sh 'pip install --user requests --upgrade'
//             sh 'pip install --user Flask-JSGlue'
//             sh 'pip install --user pyflakes'
//         }
//       }
//     }
//     stage('Cloning Git') {
//       steps {
//        git 'https://github.com/Project-Management-SCE/PM2022_TEAM_29.git'
//       }
//     }
//     stage('test') {
//       steps {
//         withEnv(["HOME=${env.WORKSPACE}"]){
//             sh 'python test2.py'
//             sh 'python -m pyflakes templates/'
//         }
//       }
//     }
//   }
// stage('coverage') {
//             steps {
//                 withEnv(["HOME=${env.WORKSPACE}"]) {
//                     dir("PM2022_TEAM_29"){
//                         sh "python -m coverage run App.py test"
//                         sh "python -m coverage report"
//                     }
//                 }
//             }
//         }
//
// 	    stage('pylint') {
//             steps {
//                 withEnv(["HOME=${env.WORKSPACE}"]) {
//
// 		   dir("PM2022_TEAM_29"){
//                         sh "python -m pylint App.py"
// 		    }
//
// 	    }
// 			    }
//
// }
