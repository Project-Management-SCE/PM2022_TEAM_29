pipeline {  
    agent none
    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages{
        stage('build') {
                agent {
                     docker 
                         { 
                          image 'python:3.8.0-alpine'
                         } 
                       }
            steps {
                sh 'python --version'
                echo "Database engine is ${DB_ENGINE}"
                echo "DISABLE_AUTH is ${DISABLE_AUTH}"
            }
       }
    }
}
