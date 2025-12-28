pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                dir('backend') {
                    sh 'docker build -t backend .'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
