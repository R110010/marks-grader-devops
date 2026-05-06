pipeline {
    agent any

    environment {
        IMAGE_NAME = "marks-grader"
        TAG = "latest"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = "30"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/R110010/marks-grader-devops.git'
            }
        }

        stage('Create Env File') {
            steps {
                withCredentials([
                    string(credentialsId: 'db-url', variable: 'DATABASE_URL'),
                    string(credentialsId: 'secret-key', variable: 'SECRET_KEY')
                ]) {

                    sh '''
                    cat > .env <<EOF
DATABASE_URL=$DATABASE_URL
SECRET_KEY=$SECRET_KEY
ALGORITHM=$ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=$ACCESS_TOKEN_EXPIRE_MINUTES
EOF
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v
                '''
            }
        }

        stage('Trivy FS Scan') {
            steps {
                sh '''
                trivy fs --exit-code 0 --severity HIGH,CRITICAL .
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                trivy image --exit-code 0 --severity HIGH,CRITICAL $IMAGE_NAME:$TAG
                '''
            }
        }

        stage('Deploy (Docker Compose)') {
            steps {
                sh '''
                docker-compose down || true
                docker-compose up -d --build
                '''
            }
        }
    }

    post {

        always {
            echo 'Pipeline finished.'
        }

        success {
            echo 'Build successful'
        }

        failure {
            echo 'Build failed'
        }
    }
}