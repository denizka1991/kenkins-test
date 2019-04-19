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
                    sh "python --version"
                }
            }

            stage("run in other container"){
              withCredentials([file(credentialsId: 'test', variable: 'SVC_ACCOUNT_KEY')]) {
                    //set SECRET with the credential content
                        sh 'ls -al $SVC_ACCOUNT_KEY'
}
                container('zip'){
                    sh "zip -v"
                  sh 'mkdir -p creds'
                  sh "cp \$SVC_ACCOUNT_KEY ./creds/serviceaccount.json"
                  sh "ls -alh ./creds/"
                }
            }
        }
        catch(err){
            currentBuild.result = 'Failure'
        }
    }
}
