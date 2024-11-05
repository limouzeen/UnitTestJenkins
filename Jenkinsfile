pipeline {
    agent any
    environment {
        PYTHON_HOME = 'C:\\Users\\Acer\\AppData\\Local\\Programs\\Python\\Python312'
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/limouzeen/UnitTestJenkins.git'
            }
        }

        stage('Check Python Version') {
            steps {
                bat 'python --version' // ตรวจสอบ version เพื่อให้แน่ใจว่า Jenkins รู้จัก Python
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python test_my_function.py'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
