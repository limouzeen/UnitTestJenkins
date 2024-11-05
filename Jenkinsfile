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
                // ติดตั้ง dependencies ด้วยคำสั่ง bat สำหรับ Windows
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // รัน Unit Test ด้วย pytest และสร้างไฟล์ XML
                bat 'pytest --junitxml=test-results.xml'
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
