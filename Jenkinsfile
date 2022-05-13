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
             stage('test') {
            steps {
                sh 'python test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
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
