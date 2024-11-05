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

        stage('Install Dependencies') {
            steps {
                // ติดตั้ง xmlrunner ก่อน
                bat 'python -m pip install xmlrunner'
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

