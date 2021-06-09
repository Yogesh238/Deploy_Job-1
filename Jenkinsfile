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
                        sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 systemctl stop goweb.service'
                        sh 'scp ${input}.zip root@54.84.99.76:/root/go/go-web'
                        sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 unzip -o /root/go/go-web/${input}.zip -d /root/go/go-web/'
                        sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 systemctl start goweb.service'
                    }
                     else if ( params.environment=='stage') {                   
                         sh 'whoami'
                         sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 systemctl stop gostage.service'
                         sh 'scp ${input}.zip root@54.84.99.76:/root/go/go-stage'
                         sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 unzip -o /root/go/go-stage/${input}.zip -d /root/go/go-stage/'
                         sh 'ssh -o StrictHostKeyChecking=no root@54.84.99.76 systemctl start gostage.service'
                         
                                }
                            }
                        }
                    }
                }
      stage('Infra Sanity Check') {
          steps{
           script {
                     if ( params.environment=='prod') {
                        sh 'python3 /root/.jenkins/workspace/kupos_deployjob/infra_sanity_test.py http://54.84.99.76:9000/'
                    }
                     else if ( params.environment=='stage') {                   
                         sh 'python3 /root/.jenkins/workspace/kupos_deployjob/infra_sanity_test.py http://54.84.99.76:8200/'
                                }
                            }
            }
          }       
     }
}
