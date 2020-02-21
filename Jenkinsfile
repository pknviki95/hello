pipeline
{
   agent any
   satges{
        stage ('checkout SCM'){
            git 'https://github.com/pknviki95/hello.git'
        }
         stage ('build'){
            fileExists '/home/pknviki95/Desktop/Python'
            sh 'ls'
        }
        stage ('test'){
            echo 'test success'    
        }
        stage ('Deploy'){
            echo 'Deploy to Docker'
        }
   }
}

