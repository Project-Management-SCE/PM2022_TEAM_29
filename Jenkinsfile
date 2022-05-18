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
            stage('test'){
              sh 'echo "testing the repo"'
    }
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
