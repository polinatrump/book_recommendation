pipeline {
    agent {
        node {
            label ''
        }
    }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                pip install -r requirements.txt
                python3 dataset_preprocessing.py
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                python3
                pip install -r requirements.txt
                coverage run -m pytest ./
                '''

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh '''
                pyinstaller --onefile run.py
                '''
            }
        }
    }
}