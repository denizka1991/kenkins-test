def label = "mypod"


podTemplate(label: label, containers: [
  containerTemplate(name: 'python', image: 'python:3', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'zip', image: 'kramos/alpine-zip', command: 'cat', ttyEnabled: true)
])
{

    node(label)
    {
        try {
            stage('Clone repo'){
                //git url: 'https://github.com/Yuriy6735/Demo3.git'
                checkout([$class: 'GitSCM', branches: [[name: '*/master']],
                userRemoteConfigs: [[url: 'https://github.com/denizka1991/kenkins-test.git']]])
                }
            stage("run in one container"){
              withCredentials([file(credentialsId: 'test', variable: 'SVC_ACCOUNT_KEY')]) {
                container("python"){
		    sh 'mkdir -p creds'
                    sh 'mv \$SVC_ACCOUNT_KEY test'
		    sh "cp test ./creds/serviceaccount.json"
		    sh "export GOOGLE_APPLICATION_CREDENTIALS='/home/jenkins/workspace/kenkins-test_master/creds/serviceaccount.json'"
		    sh "pip3 install -r ./app/requirements.txt"
		    sh "pwd"
                    sh "python3 test.py"
                }
            }
        }
            stage("run in other container"){
              withCredentials([file(credentialsId: 'test', variable: 'SVC_ACCOUNT_KEY')]) {
                    //set SECRET with the credential content
                        sh 'mv \$SVC_ACCOUNT_KEY test'
                        sh 'ls -a'
}
                container('zip'){
                    sh "zip -v"
                  sh 'mkdir -p creds'
                  sh "cp test ./creds/serviceaccount.json"
                  sh "cat ./creds/serviceaccount.json"
                }
            }
        }
        catch(err){
            currentBuild.result = 'Failure'
        }
    }
}
