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
                retry(3){
                    sh "docker-compose down && docker-compose up -d"
                    sh 'echo "Falta agregar Sonarqube"'
                }
            }
        }
        stage("Test del inicio de la ejecucion de la aplicacion"){
            steps{
                sh "curl http://34.176.51.200:8000/"
            }
        }
        stage('Sonar Scanner') {
            def sonarqubeScannerHome = tool name: 'sonar', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
            withCredentials([string(credentialsId: 'sonar', variable: 'sonarLogin')]) {
                sh "${sonarqubeScannerHome}/bin/sonar-scanner -e -Dsonar.host.url=http://sonarqube:9000"
            }
        }
        post {
            always {
                sh 'echo "Eliminando contenedores!"'
                sh "docker-compose down"
            }
        }
    }
}