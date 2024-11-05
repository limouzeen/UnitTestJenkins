// pipeline {
//     agent any

//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git 'https://github.com/limouzeen/UnitTestJenkins.git'
//             }
//         }

//         stage('Check Python and Pip') {
//             steps {
//                 bat 'python --version'
//                 bat 'pip --version'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 bat 'pip install -r requirements.txt'
//             }
//         }

//         stage('Run Unit Tests') {
//             steps {
//                 bat 'pytest --junitxml=test-results.xml'
//             }
//         }
//     }

//     post {
//         always {
//             junit 'test-results.xml'
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/limouzeen/UnitTestJenkins.git'
            }
        }

        stage('Check Python and Pip') {
            steps {
                bat 'C:\\Python39\\python --version' // แก้ไขที่อยู่ Python ให้ตรงกับที่คุณติดตั้ง
                bat 'C:\\Python39\\Scripts\\pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python39\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'C:\\Python39\\Scripts\\pytest --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}

