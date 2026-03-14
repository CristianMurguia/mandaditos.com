pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                echo 'Clonando repositorio...'
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requeriments.txt'
            }
        }

        stage('Verificar configuracion Django') {
            steps {
                bat 'python manage.py check'
            }
        }

        stage('Aplicar migraciones') {
            steps {
                bat 'python manage.py migrate --noinput'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'python manage.py test pedidos --verbosity=2'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline fallo. Revisar logs.'
        }
    }
}