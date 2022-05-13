 pipeline {
  stages{
        stage('Build') {
         agent {
              docker {
                 image 'python:3-alpine'
              }
          }
          steps {
               sh 'python -m py_compile app.py'
               stash(name: 'compiled-results', includes: 'app.py*')
                              stash(name: 'setUpPy', includes: 'setup.py*')
               stash(name: 'pypirc', includes: '.pypirc')
          }
       }

       stage('Unit Test') {
         agent {
              docker {
                 image 'qnib/pytest:latest'
              }
         }
       }
       stage('Cloning Git') {
      steps {
       git 'https://github.com/Project-Management-SCE/PM2022_TEAM_29.git'
      }
    }
  }
     post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults:'*/test_reports/.xml'
        }
        success {                   
            echo "Flask Application Up and running!!"
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
      }
}
