'''
    node{
        stage ('checkout SCM'){
            git 'https://github.com/pknviki95/hello.git'
        }
        parallel{

        
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
'''
'''
pipeline{
        agent any
        stages{
                stage ('parallel_test'){
                       parallel{
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
}
}
'''
pipeline{
        agent any
        stages{
                stage('pipeline_steps_parallel_build'){
                        steps{
                                parallel(
                                        checkoutscm: {
                                                git 'https://github.com/pknviki95/hello.git'
                                              echo "SCM"
                                        },
                                        build: {
                                                echo "Build"
                                        },
                                        test : {
                                                echo "test"
                                        },
                                        deploy: {
                                                echo "Deploy"
                                        })
                        }
                }
            }
}                                 
              