pipeline {
    agent any

    environment {
        BACKEND_IMAGE = 'feedback-backend'
        FRONTEND_IMAGE = 'feedback-frontend'
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
                    sh 'docker build -t feedback-backend:latest .'
                }
            }
        }

        stage('Build Frontend') {
            steps {
                dir('frontend') {
                    sh 'docker build -t feedback-frontend:latest .'
                }
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh '''
                    docker stop feedback-backend || true
                    docker stop feedback-frontend || true
                    docker rm feedback-backend || true
                    docker rm feedback-frontend || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker run -d \
                        --name feedback-backend \
                        -p 5000:5000 \
                        feedback-backend:latest

                    docker run -d \
                        --name feedback-frontend \
                        -p 80:80 \
                        feedback-frontend:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 15
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
            echo 'Deployment failed! Showing logs...'
            sh '''
                docker logs feedback-backend || true
                docker logs feedback-frontend || true
            '''
        }
    }
}