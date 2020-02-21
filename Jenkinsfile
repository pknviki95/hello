pipeline
{
   agent any
   stages{
        stage ('checkout SCM'){
           steps{
            git 'https://github.com/pknviki95/hello.git'
        }
        }
         stage ('build'){
            steps{
            fileExists '/home/pknviki95/Desktop/Python'
            sh 'ls'
            }
         }
        stage ('test'){
           steps{
            echo 'test success'    
           }
        }
        stage ('Deploy'){
           steps{
            echo 'Deploy to Docker'
           }
        }
   }
}

