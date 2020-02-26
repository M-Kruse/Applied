pipeline {
  agent {
    docker {
      image 'python:3'
      args '-p 3000:3000 '
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
  environment {
    PATH = "$PATH:/.local/bin"
  }
}