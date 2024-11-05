pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone repository จาก GitHub
                git 'https://github.com/limouzeen/UnitTestJenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // ติดตั้ง dependencies ถ้ามี
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // รัน Unit Test
                sh 'python -m unittest discover -s tests -p "test_my_function.py"'
            }
        }
    }

    post {
        always {
            // บันทึกผลการทดสอบให้ Jenkins แสดงผล
            junit 'test-results.xml'
        }
    }
}
