pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend') {
            steps {
                dir('backend') {
                    sh 'docker build -t feedback-backend:${BUILD_NUMBER} .'
                    sh 'docker tag feedback-backend:${BUILD_NUMBER} feedback-backend:latest'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t feedback-frontend:${BUILD_NUMBER} .'
                    sh 'docker tag feedback-frontend:${BUILD_NUMBER} feedback-frontend:latest'
                }
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker compose down --remove-orphans || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d --build'
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 15
                    curl -f http://localhost:5000/health || exit 1
                    curl -f http://localhost:80/ || exit 1
                '''
            }
        }
    }

    post {

        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed! Showing logs...'
            sh 'docker compose logs'
        }
    }
}