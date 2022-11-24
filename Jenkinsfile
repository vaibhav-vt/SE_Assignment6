pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Shubhanshu1902/SE-Lab-Jenkins.git'
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
