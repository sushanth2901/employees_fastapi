pipeline {
    agent any
    environment {
        REPO_URL = 'https://github.com/sushanth2901/employees_fastapi.git'
        BRANCH = 'main'  
        VENV_DIR = 'venv'
        WORKSPACE_DIR = 'jenkins_dir' 
    }
    stages {
        stage('git_clone'){
            steps {
                sh "git clone -b ${BRANCH} ${REPO_URL} ${jenkins_dir}"
            }
        }
        stage('deploy'){
            steps{
                sh ''' 
                cd ${jenkins_dir}
                sh test.sh
                '''
            }
        }
    
    }
}
