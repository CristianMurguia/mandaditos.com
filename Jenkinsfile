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
                 bat 'C:\\Users\\dimcg\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m pip install -r requeriments.txt'
    }
}

    stage('Verificar configuracion Django') {
        steps {
             bat 'C:\\Users\\dimcg\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe manage.py check'
    }
}

    stage('Aplicar migraciones') {
    steps {
        bat 'C:\\Users\\dimcg\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe manage.py migrate --noinput'
    }
}

|   stage('Ejecutar pruebas') {
    steps {
        bat 'C:\\Users\\dimcg\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe manage.py test pedidos --verbosity=2'
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