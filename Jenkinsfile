pipeline {
  agent any
  stages {
    stage('Clean Reports')
    {
        echo '*** Cleaning Workspace Stage ****'
    }
    stage('Build Stage') {
        echo '*** Build Stage  ****'
    }
    stage('Testing Stage') {
        echo '*** Test Stage ****' 
    }
    stage('Configure '){
          echo '*** Configure  Started ****'
    }
    stage('Deployment Stage'){
           echo '*** Deploy Stage Finished ***'
    }
  }
}
  post {
        always {
            echo 'We came to an end!'
            archiveArtifacts artifacts: 'dist/*.exe', fingerprint: true
            junit 'test-reports/*.xml'
          script{
            if(currentBuild.currentResult=='SUCCESS')
            {
              echo '*** Uploading is Started ****'
              echo '*** Uploading Finished ****'
            }
          }
          
            
            deleteDir()

         }
        success {
          echo 'Build Successfull!!'
    }
        failure {
        echo ' build is Failed :('
    }
        unstable {
            echo 'Run was marked as unstable'
        }
        changed {
            echo 'Hey look at this, Pipeline state is changed.'
        }
    }
