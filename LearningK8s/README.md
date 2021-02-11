## Kubernetes Learning

This repo is the part of the blog post [Deploy your first scaleable PHP/MySQL Web application in Kubernetes](http://blog.adnansiddiqi.me/deploy-your-first-scaleable-php-mysql-web-application-in-kubernetes/)


Docker Container Orchestration Using Kubernetes
In a Docker cluster environment, there are lot of task need to manage like scheduling, communication, and scalability and these tasks can be taken care by any of the orchestration tools available in market but some of the industry recognized tools are Docker Swarm which is a Docker native orchestration tool and "Kubernetes" which is one of the highest velocity projects in open source history.

Kubernetes is an open-source container management (orchestration) tool. It’s container management responsibilities include container deployment, scaling, and descaling of containers and container load balancing. There are Cloud-based Kubernetes services called as KaaS (Kubenetes as a Service ) also available namely AWS ECS, EKS, Azure AKS, and GCP GKE.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/kubernetes-figure3.jpg)

## Why you need containers?
Today's internet user never accept downtime. Therefore developers have to find a method to perform maintenance and update without interrupting their services.

Therefore container, which is isolated environments. It includes everything needed for application to run. It makes it easy for a developer to edit and deploying apps. Moreover, containerization has become a preferred method for packaging, deploying, and update web apps.

## What is Kubernetes?
Kubernetes is a container management system developed in the Google platform. It helps you to manage a containerized application in various types of Physical, virtual, and cloud environments.

Google Kubernetes is highly flexible container tool to deliver even complex applications, consistently. Applications 'run on clusters of hundreds to thousands of individual servers."

## Why use Kubernetes?

Kubernetes is an open source orchestration tool developed by Google for managing microservices or containerized applications across a distributed cluster of nodes. Kubernetes provides highly resilient infrastructure with zero downtime deployment capabilities, automatic rollback, scaling, and self-healing of containers (which consists of auto-placement, auto-restart, auto-replication , and scaling of containers on the basis of CPU usage).

The main objective of Kubernetes is to hide the complexity of managing a fleet of containers by providing REST APIs for the required functionalities. Kubernetes is portable in nature, meaning it can run on various public or private cloud platforms such as AWS, Azure, OpenStack, or Apache Mesos. It can also run on bare metal machines.


## Features of Kubernetes

* Autoscaling

* Automated Scheduling

* Self-Healing Capabilities

* Automated rollouts & rollback

* Horizontal Scaling & Load Balancing

* Offers environment consistency for development, testing, and production

* Infrastructure is loosely coupled to each component can act as a separate unit

* Provides a higher density of resource utilization

* Offers enterprise-ready features

* Application-centric management

* You can create predictable infrastructure

## Kubernetes Components and Architecture

Kubernetes follows a client-server architecture. It’s possible to have a multi-master setup (for high availability), but by default there is a single master server which acts as a controlling node and point of contact. The master server consists of various components including a kube-apiserver, an etcd storage, a kube-controller-manager, a cloud-controller-manager, a kube-scheduler, and a DNS server for Kubernetes services. Node components include kubelet and kube-proxy on top of Docker.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/cluster_architecture.jpeg)

OR

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/kubertes.png)


### Master Components

* etcd cluster - a simple, distributed key value storage which is used to store the Kubernetes cluster data (such as number of pods, their state, namespace, etc), API objects and service discovery details. It is only accessible from the API server for security reasons. etcd enables notifications to the cluster about configuration changes with the help of watchers. Notifications are API requests on each etcd cluster node to trigger the update of information in the node’s storage.

* kube-apiserver - Kubernetes API server is the central management entity that receives all REST requests for modifications (to pods, services, replication sets/controllers and others), serving as frontend to the cluster. Also, this is the only component that communicates with the etcd cluster, making sure data is stored in etcd and is in agreement with the service details of the deployed pods.

* kube-controller-manager - runs a number of distinct controller processes in the background (for example, replication controller controls number of replicas in a pod, endpoints controller populates endpoint objects like services and pods, and others) to regulate the shared state of the cluster and perform routine tasks. When a change in a service configuration occurs (for example, replacing the image from which the pods are running, or changing parameters in the configuration yaml file), the controller spots the change and starts working towards the new desired state.

* cloud-controller-manager - is responsible for managing controller processes with dependencies on the underlying cloud provider (if applicable). For example, when a controller needs to check if a node was terminated or set up routes, load balancers or volumes in the cloud infrastructure, all that is handled by the cloud-controller-manager.

* kube-scheduler - helps schedule the pods (a co-located group of containers inside which our application processes are running) on the various nodes based on resource utilization. It reads the service’s operational requirements and schedules it on the best fit node. For example, if the application needs 1GB of memory and 2 CPU cores, then the pods for that application will be scheduled on a node with at least those resources. The scheduler runs each time there is a need to schedule pods. The scheduler must know the total resources available as well as resources allocated to existing workloads on each node.

### Node (worker) components

* kubelet - the main service on a node, regularly taking in new or modified pod specifications (primarily through the kube-apiserver) and ensuring that pods and their containers are healthy and running in the desired state. This component also reports to the master on the health of the host where it is running.

* kube-proxy - a proxy service that runs on each worker node to deal with individual host subnetting and expose services to the external world. It performs request forwarding to the correct pods/containers across the various isolated networks in a cluster.

### Kubectl
kubectl command is a line tool that interacts with kube-apiserver and send commands to the master node. Each command is converted into an API call.

## Kubernetes Concepts
Making use of Kubernetes requires understanding the different abstractions it uses to represent the state of the system, such as services, pods, volumes, namespaces, and deployments.

* Pod - generally refers to one or more containers that should be controlled as a single application. A pod encapsulates application containers, storage resources, a unique network ID and other configuration on how to run the containers.

* Service - pods are volatile, that is Kubernetes does not guarantee a given physical pod will be kept alive (for instance, the replication controller might kill and start a new set of pods). Instead, a service represents a logical set of pods and acts as a gateway, allowing (client) pods to send requests to the service without needing to keep track of which physical pods actually make up the service.

* Volume - similar to a container volume in Docker, but a Kubernetes volume applies to a whole pod and is mounted on all containers in the pod. Kubernetes guarantees data is preserved across container restarts. The volume will be removed only when the pod gets destroyed. Also, a pod can have multiple volumes (possibly of different types) associated.

* Namespace - a virtual cluster (a single physical cluster can run multiple virtual ones) intended for environments with many users spread across multiple teams or projects, for isolation of concerns. Resources inside a namespace must be unique and cannot access resources in a different namespace. Also, a namespace can be allocated a resource quota to avoid consuming more than its share of the physical cluster’s overall resources.

* Deployment - describes the desired state of a pod or a replica set, in a yaml file. The deployment controller then gradually updates the environment (for example, creating or deleting replicas) until the current state matches the desired state specified in the deployment file. For example, if the yaml file defines 2 replicas for a pod but only one is currently running, an extra one will get created. Note that replicas managed via a deployment should not be manipulated directly, only via new deployments.


## Other Key Terminologies
### Replication Controllers
A replication controller is an object which defines a pod template. It also controls parameters to scale identical replicas of Pod horizontally by increasing or decreasing the number of running copies.

### Replication sets
Replication sets are an interaction on the replication controller design with flexibility in how the controller recognizes the pods it is meant to manage. It replaces replication controllers because of their higher replicate selection capability.

### Deployments
Deployment is a common workload which can be directly created and manage. Deployment use replication set as a building block which adds the feature of life cycle management.

### Stateful Sets
It is a specialized pod control which offers ordering and uniqueness. It is mainly used to have fine-grained control, which you have a particular need regarding deployment order, stable networking, and persistent data.

### Daemon Sets
Daemon sets are another specialized form of pod controller that runs a copy of a pod on every node in the cluster. This type of pod controller is an effective method for deploying pods that allows you to perform maintenance and offers services for the nodes themselves.

## Kubernetes vs. Docker Swarm
Parameters				Docker Swarm			Kubernetes
Scaling					No Autoscaling			Auto-scaling
Load balancing				Does auto load balancing	Manually configure your load balancing settings
Storage volume sharing			Shares storage volumes with any other container	Shares storage volumes between multiple containers inside the same Pod
Use of logining and monitoring tool	Use 3rd party tool like ELK	Provide an in-built tool for logging and monitoring.
Installation				Easy & fast	Complicated & time-consuming
GUI					GUI not available	GUI is available
Scalability				Scaling up is faster than K8S, but cluster strength not as robust	Scaling up is slow compared to Swarm, but guarantees stronger cluster state Load balancing requires manual service configuration
Load Balancing				Provides a built-in load balancing technique	Process scheduling to maintain services while updating
Updates & Rollbacks Data Volumes Logging & Monitoring	Progressive updates and service health monitoring.	Only shared with containers in same Pod Inbuilt logging & monitoring tools.

## Disadvantages of Kubernetes
Kubernetes is a little bit complicated and unnecessary in environments where all development is done locally.
Security is not very effective.
The biggest drawback of Kubenetes is that it's dashboard not very useful and effective

Ref: https://www.guru99.com/kubernetes-tutorial.html

Installing Kubernetes
1. Set the K8S_VERSION env variable to the latest stable Kubernetes release, for later retrieval:

export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt)
2. Assuming the host’s architecture is amd64, set the ARCH env variable:

export ARCH=amd64

3. Run the hypercube Docker container, which itself takes care of installing all the Kubernetes components. It requires special privileges, which are explained below.

docker run -d --volume=/:/rootfs:ro \
--volume=/sys:/sys:rw --volume=/var/lib/docker/:/var/lib/docker:rw \
--volume=/var/lib/kubelet/:/var/lib/kubelet:rw --volume=/var/run:/var/run:rw \
--net=host --pid=host --name=hyperkube-installer \
--privileged gcr.io/google_containers/hyperkube-${ARCH}:${K8S_VERSION}\   
/hyperkube kubelet --containerized \
--hostname-override=127.0.0.1 --api-servers=http://localhost:8080 \
--config=/etc/kubernetes/manifests --allow-privileged --v=2


4. Run the command docker ps to see all the running containers started by hypercube, for example a container created with the command "/hyperkube apiserver".

The volume parameters are required to mount and give access to the host’s /root , /sys , /var/run and /var/lib/docker filesystems inside the container instance. The --privileged option grants access to all devices of the host, namely to start new containers. Parameters --net=host and --pid=host allow access to the network and PID namespace of the host.

hypercube's Docker image is available from Google’s Container Registry (GCR), we use ARCH and K8S_VERSION env variables to construct the full path to the image that fits our environment: gcr.io/google_containers/hyperkube-${ARCH}:${K8S_VERSION}

Deploying Pods
1. Start a bash shell inside the hypercube container:

docker exec -it hyperkube-installer /bin/bash
2. Export the Kubernetes version and processor architecture inside the container:

export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt) 
export ARCH=amd64
3. Download the kubectl command line tool into /usr/bin/kubectl and make it executable:

curl -sSL "http://storage.googleapis.com/kubernetes-release/release/$K8S_VERSION/bin/linux/$ARCH/kubectl" > /usr/bin/kubectl 
chmod +x /usr/bin/kubectl
4. Now you can run kubectl commands to retrieve information on Kubernetes state:

kubectl get nodes
kubectl get pods
kubectl get namespaces
5. Start deployment of a sample nginx pod and exit the container:

kubectl run nginx --image=nginx --port=80 ; exit
6. Run the command docker ps to see the new nginx containers running on the host.

7. Declare the nginx pod deployment as a service and map port 80 of the nginx service to port 8080 on the host:

docker exec -it hyperkube-installer /bin/bash
kubectl expose deployment nginx --port=8080 --target-port=80
8. Check that the nginx service is ready and was assigned an IP, and store it in a variable:

kubectl get service nginx
ip=$(kubectl get svc nginx --template={{.spec.clusterIP}}
9. Check the nginx welcome page is there via a browser or downloading it with curl:

curl "http://$ip:8080"

## Operational and Governance Features
Kublr provides an intuitive UI that operations teams can use to deploy and manage clusters.  It enables users to see their status and health at a glance, and provides domain specific deployment screens.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/kublr1.png)

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/kublr2.png)





# Refresh Configs in Jnlp Nodes(JAVA NETWORK LAUNCH PROTOCOL)

### Install and Check the version

`$ brew install kubernetes-cli
 $ kubectl version --short
  Client Version: v1.13.5
  Server Version: v1.13.4
`

### Download config

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/rancher_kubeconfig_file_button_hu49a299f8b62fd5c71b6f3029b0190fcd_41766_1000x0_resize_box.gif)

Go to the Rancher-Managed Kubernetes Clusters and download a kubeconfig file through the web UI and use it to connect to your Kubernetes environment with kubectl.
Click on the button for a detailed look at your config file as well as directions to place in ~/.kube/config.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/rancher_kubeconfig_instructions_hu08acb4c74d33e686312cc8d80398586c_587079_1000x0_resize_box_2.png)

### Check the list of clusters; It should list something like below

`
# kubectl config get-contexts
CURRENT   NAME               CLUSTER            AUTHINFO                        NAMESPACE
*         xy02-dfddf        xy02-dfddf         sameer_sahoo@xy02-dfddf         
          pk95-adsfd        eu95-dragon        sameer_sahoo@eu95-dragon        
          hh17-bdgdgfg       pk95-adsfd      sameer_sahoo@pk95-adsfd      
          ss02-rewreww      ss02-rewreww     sameer_sahoo@ss02-rewreww     
          df11-cczcxcc     df11-cczcxcc       sameer_sahoo@df11-cczcxcc  
`

### Set the cluster and point to our namespace
`
    1. kubectl config use-context ss02-rewreww
    2. kubectl config set-context ss02-rewreww —namespace=abc-def-ghi-sdfdfs
`

### Verify whether the context got set or not

`
    # kubectl config current-context
      ss02-rewreww
`

### 1. Make sure  you can list pods to make sure its working

`
$ kubectl get pods
  NAME                   READY   STATUS    RESTARTS   AGE
  nginx-5c7588df-k5wks   1/1     Running   0          9s
`

### Find the JNLP servers
`
$ kubectl get pods | grep general-jnlp
$ kubectl get pods | grep general-jnlp
permanent-k8s-general-jnlp-01-567565767gh-hjhjjk                    1/1     Running            0          20d
permanent-k8s-general-jnlp-02-5867867878j-jljkkk                    1/1     Running            0          97d
permanent-k8s-general-jnlp-03-2534343444g-bnbnbn                    1/1     Running            0          98d
`

### Copy the config file from local to all jnlp nodes listed in Step 5

kubectl cp config permanent-k8s-general-jnlp-01-567565767gh-hjhjjk:/root/.kube/

### Login to each jnlp node and make sure we are able to get pods as mentioned in step 4

`
$ kubectl exec -it permanent-k8s-general-jnlp-01-567565767gh-hjhjjk /bin/bash
[root@permanent-k8s-general-jnlp-01-567565767gh-hjhjjk /]# kubectl get pods
        NAME                                                              READY     STATUS             RESTARTS   AGE
        glade-00ce8c9e-9b80-450c-8ff5-e5ef3f75ed95-435345435g-2898j       1/1       Running            0          4d
        glade-55103b67-3c4d-4a12-867a-20c966710234-123423432w-xbq56       1/1       Running            0          4d
        glade-9aab6a29-c19b-4a24-99d4-bbdcae7949cf-435435435f-qsfjd       1/1       Running            0          2d
        glade-bbe73872-cfa2-4dbf-ad79-70c5dbc0fd68-533454534m-kl5h9       1/1       Running            1          2d
        glade-bbee4503-1d1d-4dbf-b63a-1156eaf47af
        # exit
`

# App deployment
**Deployment is a method of converting images to containers and then allocating those images to pods in the Kubernetes cluster**.
This also helps in setting up the application cluster which includes 
	* deployment of service, 
	* pod, 
	* replication controller and 
	* replica set. 
The cluster can be set up in such a way that the applications deployed on the pod can communicate with each other.

In this setup, we can have a load balancer setting on top of one application diverting traffic to a set of pods and later they communicate to backend pods. The communication between pods happen via the service object built in Kubernetes.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/application_cluster_view.jpg)

**Ngnix Load Balancer Yaml File**
`
apiVersion: v1
kind: Service
metadata:
   name: oppv-dev-nginx
      labels:
         k8s-app: omni-ppv-api
spec:
   type: NodePort
   ports:
   - port: 8080
      nodePort: 31999
      name: omninginx
   selector:
      k8s-app: appname
      component: nginx
      env: dev
`

**Ngnix Replication Controller Yaml**
`
apiVersion: v1
kind: ReplicationController
metadata:
   name: appname
spec:
   replicas: replica_count
   template:
      metadata:
         name: appname
         labels:
            k8s-app: appname
            component: nginx
               env: env_name
spec:
   nodeSelector:
      resource-group: oppv
   containers:
      - name: appname
      image: IMAGE_TEMPLATE
      imagePullPolicy: Always
      ports:
         - containerPort: 8080
         resources:
            requests:
               memory: "request_mem"
               cpu: "request_cpu"
            limits:
               memory: "limit_mem"
               cpu: "limit_cpu"
            env:
            - name: BACKEND_HOST
               value: oppv-env_name-node:3000
`

**Frontend Service Yaml File**
`
apiVersion: v1
kind: Service
metadata:
   name: appname
   labels:
      k8s-app: appname
spec:
   type: NodePort
   ports:
   - name: http
      port: 3000
      protocol: TCP
      targetPort: 3000
   selector:
      k8s-app: appname
      component: nodejs
      env: dev
`

**Frontend Replication Controller Yaml File**
`
apiVersion: v1
kind: ReplicationController
metadata:
   name: Frontend
spec:
   replicas: 3
   template:
      metadata:
         name: frontend
         labels:
            k8s-app: Frontend
            component: nodejs
            env: Dev
spec:
   nodeSelector:
      resource-group: oppv
   containers:
      - name: appname
         image: IMAGE_TEMPLATE
         imagePullPolicy: Always
         ports:
            - containerPort: 3000
            resources:
               requests:
                  memory: "request_mem"
                  cpu: "limit_cpu"
                  limits:
                  memory: "limit_mem"
                  cpu: "limit_cpu"
            env:
               - name: ENV
               valueFrom:
               configMapKeyRef:
               name: appname
               key: config-env
`

**Backend Service Yaml File**
`
apiVersion: v1
kind: Service
metadata:
   name: backend
   labels:
      k8s-app: backend
spec:
   type: NodePort
   ports:
   - name: http
      port: 9010
      protocol: TCP
      targetPort: 9000
   selector:
      k8s-app: appname
      component: play
      env: dev
`

**Backed Replication Controller Yaml File**
`
apiVersion: v1
kind: ReplicationController
metadata:
   name: backend
spec:
   replicas: 3
   template:
      metadata:
         name: backend
      labels:
         k8s-app: beckend
         component: play
         env: dev
spec:
   nodeSelector:
      resource-group: oppv
      containers:
         - name: appname
            image: IMAGE_TEMPLATE
            imagePullPolicy: Always
            ports:
            - containerPort: 9000
            command: [ "./docker-entrypoint.sh" ]
            resources:
               requests:
                  memory: "request_mem"
                  cpu: "request_cpu"
               limits:
                  memory: "limit_mem"
                  cpu: "limit_cpu"
            volumeMounts:
               - name: config-volume
               mountPath: /app/vipin/play/conf
         volumes:
            - name: config-volume
            configMap:
            name: appname
`

# Autoscaling
Autoscaling is one of the key features in Kubernetes cluster. It is a feature in which the cluster is capable of increasing the number of nodes as the demand for service response increases and decrease the number of nodes as the requirement decreases. This feature of auto scaling is currently supported in Google Cloud Engine (GCE) and Google Container Engine (GKE) and will start with AWS pretty soon.

In order to set up scalable infrastructure in GCE, we need to first have an active GCE project with features of Google cloud monitoring, google cloud logging, and stackdriver enabled.

First, we will set up the cluster with few nodes running in it. Once done, we need to set up the following environment variable.

Environment Variable
`
export NUM_NODES = 2
export KUBE_AUTOSCALER_MIN_NODES = 2
export KUBE_AUTOSCALER_MAX_NODES = 5
export KUBE_ENABLE_CLUSTER_AUTOSCALER = true
`
Once done, we will start the cluster by running kube-up.sh. This will create a cluster together with cluster auto-scalar add on.
`
./cluster/kube-up.sh
`
On creation of the cluster, we can check our cluster using the following kubectl command.

`
$ kubectl get nodes
NAME                             STATUS                       AGE
kubernetes-master                Ready,SchedulingDisabled     10m
kubernetes-minion-group-de5q     Ready                        10m
kubernetes-minion-group-yhdx     Ready                        8m
`
Now, we can deploy an application on the cluster and then enable the horizontal pod autoscaler. This can be done using the following command.

`
$ kubectl autoscale deployment <Application Name> --cpu-percent = 50 --min = 1 --
max = 10
`
The above command shows that we will maintain at least one and maximum 10 replica of the POD as the load on the application increases.

We can check the status of autoscaler by running the $kubclt get hpa command. We will increase the load on the pods using the following command.

`
$ kubectl run -i --tty load-generator --image = busybox /bin/sh
$ while true; do wget -q -O- http://php-apache.default.svc.cluster.local; done
`
We can check the hpa by running $ kubectl get hpa command.

`
$ kubectl get hpa
NAME         REFERENCE                     TARGET CURRENT
php-apache   Deployment/php-apache/scale    50%    310%

MINPODS  MAXPODS   AGE
  1        20      2m
  
$ kubectl get deployment php-apache
NAME         DESIRED    CURRENT    UP-TO-DATE    AVAILABLE   AGE
php-apache      7          7           7            3        4m
We can check the number of pods running using the following command.

jsz@jsz-desk2:~/k8s-src$ kubectl get pods
php-apache-2046965998-3ewo6 0/1        Pending 0         1m
php-apache-2046965998-8m03k 1/1        Running 0         1m
php-apache-2046965998-ddpgp 1/1        Running 0         5m
php-apache-2046965998-lrik6 1/1        Running 0         1m
php-apache-2046965998-nj465 0/1        Pending 0         1m
php-apache-2046965998-tmwg1 1/1        Running 0         1m
php-apache-2046965998-xkbw1 0/1        Pending 0         1m
And finally, we can get the node status.

$ kubectl get nodes
NAME                             STATUS                        AGE
kubernetes-master                Ready,SchedulingDisabled      9m
kubernetes-minion-group-6z5i     Ready                         43s
kubernetes-minion-group-de5q     Ready                         9m
kubernetes-minion-group-yhdx     Ready                         9m
`


# Setting Kubectl
`
$ curl -O https://storage.googleapis.com/kubernetesrelease/release/v1.5.2/bin/darwin/amd64/kubectl
$ chmod +x kubectl
$ mv kubectl /usr/local/bin/kubectl
`

## Configuring Kubectl
Following are the steps to perform the configuration operation.
`
$ kubectl config set-cluster default-cluster --server = https://${MASTER_HOST} --
certificate-authority = ${CA_CERT}

$ kubectl config set-credentials default-admin --certificateauthority = ${
CA_CERT} --client-key = ${ADMIN_KEY} --clientcertificate = ${
ADMIN_CERT}

$ kubectl config set-context default-system --cluster = default-cluster --
user = default-admin
$ kubectl config use-context default-system
Replace ${MASTER_HOST} with the master node address or name used in the previous steps.
`
Replace ${CA_CERT} with the absolute path to the ca.pem created in the previous steps.

Replace ${ADMIN_KEY} with the absolute path to the admin-key.pem created in the previous steps.

Replace ${ADMIN_CERT} with the absolute path to the admin.pem created in the previous steps.

## Verifying the Setup
To verify if the kubectl is working fine or not, check if the Kubernetes client is set up correctly.
`
$ kubectl get nodes

NAME       LABELS                                     STATUS
Vipin.com  Kubernetes.io/hostname = vipin.mishra.com    Ready
`







https://www.tutorialspoint.com/kubernetes/kubernetes_kubectl_commands.htm

