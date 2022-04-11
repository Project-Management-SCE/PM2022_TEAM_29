pipeline {
    agent { docker 
            { 
                image 'python:3.10.1-alpine'
            } 
          }
    
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                echo "Database engine is ${DB_ENGINE}"
                echo "DISABLE_AUTH is ${DISABLE_AUTH}"
            }
        }
        stage('Test') {
            
        }
      }
}

