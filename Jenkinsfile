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
          sh 'apk add virtualenv'
          sh 'virtualenv applied'
          sh '. env/bin/activate'
          sh 'pip install -r requirements.txt'
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
