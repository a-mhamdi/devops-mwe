pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                dir('backend') {
                    docker.build("backend")
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
