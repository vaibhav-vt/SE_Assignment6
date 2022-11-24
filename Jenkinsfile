pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vaibhav-vt/SE_Assignment6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x program.py"
                sh "python program.py"
            }
        }
        stage('To pass tests') {
            steps {
                sh "chmod u+x test.py"
                sh "python test.py"
            }
        }

        stage('To fail tests') {
            steps {
                sh "chmod u+x test2.py"
                sh "python test2.py"
            }
        }
        
    } 
}
