pipeline {
    agent any
    environment {
        REPO_URL = 'https://github.com/sushanth2901/employees_fastapi.git'
        BRANCH = 'main'  
        VENV_DIR = 'venv'
        WORKSPACE_DIR = 'workspace_dir' 
    }
    stages {
        stage('git_clone'){
            steps {
                sh "git clone -b ${BRANCH} ${REPO_URL} ${WORKSPACE_DIR}"
            }
        }
    }
    stages {
        stage('deploy'){
            steps{
                cd workspacke_dir
                sh test.sh
            }
        }
    }
    
}
