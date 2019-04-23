def label = "mypod"


podTemplate(label: label, containers: [
  containerTemplate(name: 'python-alpine', image: 'python:3-alpine', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'zip', image: 'kramos/alpine-zip', command: 'cat', ttyEnabled: true)
])
{

    node(label)
    {
        try {
            stage("run in one container"){
                container("python-alpine"){
		    sh 'mkdir -p creds'
		    sh "cp test ./creds/serviceaccount.json"
		    sh " export GOOGLE_APPLICATION_CREDENTIALS="./creds/serviceaccount.json"
                    sh "python3 test.py"
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
