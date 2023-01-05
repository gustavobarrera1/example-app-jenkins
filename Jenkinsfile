pipeline {
    agent any
    stages {
        stage("Verificar versiones de docker"){
            steps {
                sh '''
                docker-compose version
                curl --version
                '''
            }
        }
        stage("Iniciar contenedor"){
            steps {
                sh "docker-compose up -d"
            }
        }
        stage("Test del inicio de la ejecucion de la aplicacion"){
            steps{
                sh "curl http://34.176.51.200:8000/"
            }
        }
    }
}