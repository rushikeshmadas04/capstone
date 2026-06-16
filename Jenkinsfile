pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker compose.yml'
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
                    sh 'docker build -t feedback-backend:latest .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t feedback-frontend:${BUILD_NUMBER} .'
                    sh 'docker build -t feedback-frontend:latest .'
                }
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker compose -f ${DOCKER_COMPOSE_FILE} down --remove-orphans || true'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose -f ${DOCKER_COMPOSE_FILE} up -d --build'
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 10
                    curl -f http://localhost:5000/ || exit 1
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
            echo 'Deployment failed!'
            sh 'docker compose -f ${DOCKER_COMPOSE_FILE} logs'
        }
    }
}
