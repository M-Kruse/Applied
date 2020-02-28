pipeline {
  agent {
    docker {
      args '-p 3000:3000 '
      image 'django-dev'
    }

  }
  stages {
    stage('Build') {
      steps {
        withEnv(overrides: ["HOME=${env.WORKSPACE}"]) {
          sh '''  virtualenv env
source env/bin/activate
pip install -r requirements.txt'''
        }

      }
    }

    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }

  }
  environment {
    PATH = "$PATH:/.local/bin"
  }
}