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
                // ติดตั้ง unittest-xml-reporting แทน xmlrunner
                bat 'python -m pip install unittest-xml-reporting'
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
