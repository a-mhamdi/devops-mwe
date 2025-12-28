pipeline {
    agent any
    stages {
        stage('Build Backend') {
            steps {
                echo 'Building Backend...'
                dir('backend') {
                    sh 'docker build -t backend .'
                }
            }
        }
        stage('Build Frontend') {
            steps {
                echo 'Building Frontend...'
                dir('frontend') {
                    sh 'docker build -t frontend .'
                }
            }
        }
    }
}
