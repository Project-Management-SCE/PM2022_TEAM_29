pipeline {
  agent { 
      docker { 
          image 'python:3.7.2' } }
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]){
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
 stage('Deploy to Heroku') {
            agent {
                docker {
                    image 'cimg/base:stable'
                    args '-u root'
                }
            }
            steps {
                sh '''
                    curl https://cli-assets.heroku.com/install.sh | sh;
                    heroku container:login
                    heroku container:push web --app sce-flask-template
                    heroku container:release web --app sce-flask-template
                '''
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
