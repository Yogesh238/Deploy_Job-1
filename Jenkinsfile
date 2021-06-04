pipeline {
    agent any
    parameters {
        string(defaultValue: '', description: 'Enter Environment Name (Available Environments: dev & prod) :', name: 'environment', trim: false)
        string(defaultValue: 'latest', description: 'Enter BUILD NUMBER to deploy [Default Value: latest]:', name: 'input', trim: false)
    }
 stages {
     stage('Pull from Artifactory') {
            steps {
                sh 'aws s3 cp s3://kupos-at-project/${input}.zip .'
            }
        }      
     stage("Deploy"){
             steps{
                sshagent(credentials : ['appserver']) {
                     script {
                     if ( params.environment=='prod') {
                        sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 systemctl stop goweb.service'
                        sh 'scp ${input}.zip root@3.87.185.160:/root/go/go-web'
                        sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 unzip /root/go/go-web/${input}.zip -d /root/go/go-web/'
                        sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 systemctl start goweb.service'
                    }
                     else if ( params.environment=='stage') {                   
                         sh 'whoami'
                         sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 systemctl stop gostage.service'
                         sh 'scp ${input}.zip root@3.87.185.160:/root/go/go-stage'
                         sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 unzip /root/go/go-stage/${input}.zip -d /root/go/go-stage/'
                         sh 'ssh -o StrictHostKeyChecking=no root@3.87.185.160 systemctl start gostage.service'
                         
                                }
                            }
                        }
                    }
                }
      stage('Infra Sanity Check') {
            steps {
                sh '/root/.jenkins/workspace/Deploy_Job/infra_sanity_test.py'
            }
        }       
     }
}
