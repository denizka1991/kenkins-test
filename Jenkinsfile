def label = "mypod"


podTemplate(label: label, containers: [
  containerTemplate(name: 'python', image: 'python:3', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'zip', image: 'kramos/alpine-zip', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'monitoring', image: 'lachlanevenson/k8s-helm', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.4.8', command: 'cat', ttyEnabled: true)
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
//		    sh 'mkdir -p creds'
//                    sh 'mv \$SVC_ACCOUNT_KEY test'
//		    sh "cp test ./creds/serviceaccount.json"
//              	    sh "cat ./creds/serviceaccount.json"
//		    sh "pip3 install -r ./app/requirements.txt"
//		    sh "./test.sh"
//                    sh "python3 test.py"
//                    sh "cd savedb"
//		    sh "python3 test.py"
//		    sh "cd .."
//		    sh "cd saveredis"
//                    sh "python3 test.py"
//                    sh "cd .."
//		    sh "cd getfromdb"
//                    sh "python3 test.py"
		     sh 'echo "0000000000000000000000000000"'
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

            stage("run in other container"){
              withCredentials([file(credentialsId: 'test', variable: 'SVC_ACCOUNT_KEY')]) {
                    //set SECRET with the credential content
                        sh 'mv \$SVC_ACCOUNT_KEY test'
		 }
		   container('monitoring'){
                    sh "helm version"
                    //sh "gcloud container clusters get-credentials devops-cluster --zone europe-west1-b --project dynamic-circle-235118"
		      sh 'helm init'
		      sh 'helm repo update'
		      sh 'helm dep update ./ita-monitoring'
                   // sh 'kubectl create clusterrolebinding tiller --clusterrole cluster-admin -serviceaccount=kube-system:default'
		      sh "helm upgrade --install --name monitoring --namespace monitoring ./ita-monitoring"
		  //    sh 'helm delete --purge monitoring'	
                }
	    }
            
 //             stage("run in other container"){
 //             withCredentials([file(credentialsId: 'test', variable: 'SVC_ACCOUNT_KEY')]) {
 //                   //set SECRET with the credential content
 //                       sh 'mv \$SVC_ACCOUNT_KEY test'
 //                }
 //                  container('kubectl'){
                   // sh "helm version"
//                    sh "gcloud container clusters get-credentials devops-cluster --zone europe-west1-b --project dynamic-circle-235118"
//                   // sh 'helm init'
//                    sh 'kubectl create -f sa.yaml'
                    //sh "helm install --name monitoring --namespace monitoring ./ita-monitoring"
//                }
//            }

        }
        catch(err){
            currentBuild.result = 'Failure'
        }
    }
}
