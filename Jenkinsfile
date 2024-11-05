pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/limouzeen/UnitTestJenkins.git'
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



