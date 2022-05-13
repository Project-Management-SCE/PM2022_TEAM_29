pipeline{
   agent any
    stages{
        stage("Git SCM"){
            steps{
                git credentialsId: 'dockerid', url: 'https://github.com/Project-Management-SCE/PM2022_TEAM_29/blob/main/Jenkinsfile.git'
            }
        }
        stage("Build"){
            agent {
                docker {
                    image 'python:3.6-alpine' 
                }
            }
            steps{
                sh "python -m compileall ."
            }
            
        }
        stage("Test"){
         
    
        }
        stage("Build Docker Image"){
            steps{
                sh "docker build -t kowal20x7/flaskapi:latest ."
            }
        }
        stage ("Push dockerhub"){
            steps{
                withCredentials([string(credentialsId: 'dockerpassid', variable: 'password')]) {
                    sh "docker login -u kowal20x7 -p ${password}"
                }
        
                sh "docker push kowal20x7/flaskapi:latest"
            }
        }
        
        stage("Run Container"){
            steps{
                sh "docker run -d -p 5000:5000 --name flaskapi kowal20x7/flaskapi:latest"
            }
        }
    }

}
