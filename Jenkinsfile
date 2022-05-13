pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'echo "building the repo"'
          }
        }
      }
    }
     stage('Build Docker') {
         sh "sudo docker build -t flask-app ."
   }
     stage("run docker container"){
        sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app "
    }
     stage('test') {
         steps {
                sh 'python test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
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
