pipeline {
  agent {
    docker {
      args '-p 3000:3000 '
      image 'python:3'
    }

  }
  stages {
    stage('Build') {
      steps {
        withEnv(overrides: ["HOME=${env.WORKSPACE}"]) {
          sh '''pip install -r requirements.txt
 python manage.py collectstatic'''
        }

      }
    }

  }
}