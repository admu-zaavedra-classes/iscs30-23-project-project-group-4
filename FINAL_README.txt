READ ME

PART I. Building Docker Image

a. We first created a dockerfile in our project repository. In this docker file, we added the necessary details. Please see the github for more information. 
b. Next, we ran docker build -t app to build the docker image.
c. Going to Google Cloud, we downloaded Cloud SDK / Cloud CLI. This is needed for us to later tag our docker image.
d. We then pushed the docker image to google cloud. The image is now in our container registry
e. Now for the Cloud Run, we created a service, setting the necessary parameters such as the container image url and the port. For Ingress we allowed traffic and allowed unauthenticated invocations. 
f. We configured the settings.py specifically the ALLOWED HOST, so that we can open the app url
g. This is what we got: https://django-app-2r3ksmt46q-uc.a.run.app/dashboard/
h. Watch this video for a step-by-step process: https://www.youtube.com/watch?v=_ZMGp-bSQhg&ab_channel=ScalableScripts


PART II. Pushing image to dockerhub

a. We then pushed our image to dockerhub.  Here is our repository: https://hub.docker.com/r/lancedamalerio/widgetapp 
b. Watch this video for the specific steps that were followed:  https://www.youtube.com/watch?v=f2sDOaOzKPM&ab_channel=ProgrammingKnowledge


PART III.  Manifests
 
a. We created Kubernetes manifests for our application.
b. We first created a Google Kubernetes Engine (GKE) Cluster. We named ours django-cluster-1 with zone us-central1-c. 
c. We then created a folder called kubernetes-manifests where we would create our Deployment YAML, ingress YAML, HPA YAML, PVC YAML and service YAML. 


PART IV.  Application of Manifests

a. Following this we ran kubectl apply commands for all the YAML files. 
	kubectl apply -f django-deployment.yaml
	kubectl apply -f django-service.yaml
	kubectl apply -f django-ingress.yaml
	kubectl apply -f django-hpa.yaml
	kubectl apply -f django-pvc.yaml


PART V. Verification of Deployment

a. kubectl get pods
b. kubectl get services
c. kubectl get ingress
d. kubectl get deployments
