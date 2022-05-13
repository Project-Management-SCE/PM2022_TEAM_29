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
       stage('Get Source') {
      git (https://github.com/Project-Management-SCE/PM2022_TEAM_29/blob/main/Docker.git')
      if (!fileExists("Docker")) {
         error('Dockerfile missing.')
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
