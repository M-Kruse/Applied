pipeline {
  agent {
    dockerfile {
      filename 'Applied.Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        withEnv(overrides: ["HOME=${env.WORKSPACE}"]) {
          sh 'apt-get install virtualenv'
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