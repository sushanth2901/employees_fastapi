pipeline {
    agent any
    environment {
        REPO_URL = 'https://github.com/sushanth2901/employees_fastapi.git'
        BRANCH = 'main'  
        VENV_DIR = 'venv'
        WORKSPACE_DIR = 'cpu_mem_dir1' 
    }
    stages {
        stage('git_clone'){
            steps {
                sh "git clone -b ${BRANCH} ${REPO_URL} ${WORKSPACE_DIR}"
            }
        }
        stage('deploy'){
            steps{
                sh ''' 
                cd ${WORKSPACE_DIR}
                bash test.sh
                '''
            }
        }
    }
}
