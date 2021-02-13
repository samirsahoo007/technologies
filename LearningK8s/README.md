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

![alt text](https://github.com/samirsahoo007/technologies/blob/master/LearningK8s/images/kubernetes_architecture.png)


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
Monitoring is one of the key component for managing large clusters. For this, we have a number of tools.

# Monitoring with Prometheus
It is a monitoring and alerting system. It was built at SoundCloud and was open sourced in 2012. It handles the multi-dimensional data very well.

Prometheus has multiple components to participate in monitoring −

Prometheus − It is the core component that scraps and stores data.

Prometheus node explore − Gets the host level matrices and exposes them to Prometheus.

Ranch-eye − is an haproxy and exposes cAdvisor stats to Prometheus.

Grafana − Visualization of data.

InfuxDB − Time series database specifically used to store data from rancher.

Prom-ranch-exporter − It is a simple node.js application, which helps in querying Rancher server for the status of stack of service.

Monitoring with Prometheus 
Sematext Docker Agent
It is a modern Docker-aware metrics, events, and log collection agent. It runs as a tiny container on every Docker host and collects logs, metrics, and events for all cluster node and containers. It discovers all containers (one pod might contain multiple containers) including containers for Kubernetes core services, if the core services are deployed in Docker containers. After its deployment, all logs and metrics are immediately available out of the box.

Deploying Agents to Nodes
Kubernetes provides DeamonSets which ensures pods are added to the cluster.

Configuring SemaText Docker Agent
It is configured via environment variables.

Get a free account at apps.sematext.com, if you don’t have one already.

Create an SPM App of type “Docker” to obtain the SPM App Token. SPM App will hold your Kubernetes performance metrics and event.

Create a Logsene App to obtain the Logsene App Token. Logsene App will hold your Kubernetes logs.

Edit values of LOGSENE_TOKEN and SPM_TOKEN in the DaemonSet definition as shown below.

Grab the latest sematext-agent-daemonset.yml (raw plain-text) template (also shown below).

Store it somewhere on the disk.

Replace the SPM_TOKEN and LOGSENE_TOKEN placeholders with your SPM and Logsene App tokens.

Create DaemonSet Object
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
   name: sematext-agent
spec:
   template:
      metadata:
         labels:
            app: sematext-agent
      spec:
         selector: {}
         dnsPolicy: "ClusterFirst"
         restartPolicy: "Always"
         containers:
         - name: sematext-agent
            image: sematext/sematext-agent-docker:latest
            imagePullPolicy: "Always"
            env:
            - name: SPM_TOKEN
               value: "REPLACE THIS WITH YOUR SPM TOKEN"
            - name: LOGSENE_TOKEN
               value: "REPLACE THIS WITH YOUR LOGSENE TOKEN"
            - name: KUBERNETES
               value: "1"
            volumeMounts:
               - mountPath: /var/run/docker.sock
                  name: docker-sock
               - mountPath: /etc/localtime
                  name: localtime
            volumes:
               - name: docker-sock
                  hostPath:
                     path: /var/run/docker.sock
               - name: localtime
                  hostPath:
                     path: /etc/localtime
Running the Sematext Agent Docker with kubectl
$ kubectl create -f sematext-agent-daemonset.yml
daemonset "sematext-agent-daemonset" created
Kubernetes Log
Kubernetes containers’ logs are not much different from Docker container logs. However, Kubernetes users need to view logs for the deployed pods. Hence, it is very useful to have Kubernetes-specific information available for log search, such as −

Kubernetes namespace
Kubernetes pod name
Kubernetes container name
Docker image name
Kubernetes UID
Using ELK Stack and LogSpout
ELK stack includes Elasticsearch, Logstash, and Kibana. To collect and forward the logs to the logging platform, we will use LogSpout (though there are other options such as FluentD).

The following code shows how to set up ELK cluster on Kubernetes and create service for ElasticSearch −

apiVersion: v1
kind: Service
metadata:
   name: elasticsearch
   namespace: elk
   labels:
      component: elasticsearch
spec:
   type: LoadBalancer
   selector:
      component: elasticsearch
   ports:
   - name: http
      port: 9200
      protocol: TCP
   - name: transport
      port: 9300
      protocol: TCP
Creating Replication Controller
apiVersion: v1
kind: ReplicationController
metadata:
   name: es
   namespace: elk
   labels:
      component: elasticsearch
spec:
   replicas: 1
   template:
      metadata:
         labels:
            component: elasticsearch
spec:
serviceAccount: elasticsearch
containers:
   - name: es
      securityContext:
      capabilities:
      add:
      - IPC_LOCK
   image: quay.io/pires/docker-elasticsearch-kubernetes:1.7.1-4
   env:
   - name: KUBERNETES_CA_CERTIFICATE_FILE
   value: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
   - name: NAMESPACE
   valueFrom:
      fieldRef:
         fieldPath: metadata.namespace
   - name: "CLUSTER_NAME"
      value: "myesdb"
   - name: "DISCOVERY_SERVICE"
      value: "elasticsearch"
   - name: NODE_MASTER
      value: "true"
   - name: NODE_DATA
      value: "true"
   - name: HTTP_ENABLE
      value: "true"
ports:
- containerPort: 9200
   name: http
   protocol: TCP
- containerPort: 9300
volumeMounts:
- mountPath: /data
   name: storage
volumes:
   - name: storage
      emptyDir: {}
Kibana URL
For Kibana, we provide the Elasticsearch URL as an environment variable.

- name: KIBANA_ES_URL
value: "http://elasticsearch.elk.svc.cluster.local:9200"
- name: KUBERNETES_TRUST_CERT
value: "true"
Kibana UI will be reachable at container port 5601 and corresponding host/Node Port combination. When you begin, there won’t be any data in Kibana (which is expected as you have not pushed any data).

* **Network Policy defines how the pods in the same namespace will communicate with each other and the network endpoint. It requires extensions/v1beta1/networkpolicies to be enabled in the runtime configuration in the API server. Its resources use labels to select the pods and define rules to allow traffic to a specific pod in addition to which is defined in the namespace.**
* **Secrets can be defined as Kubernetes objects used to store sensitive data such as user name and passwords with encryption. The files can be either in txt or yaml format**.
* **In Kubernetes, a volume can be thought of as a directory which is accessible to the containers in a pod. As soon as the life of a pod ended, the volume was also lost.**
* **Deployments are upgraded and higher version of replication controller. They manage the deployment of replica sets which is also an upgraded version of the replication controller. They have the capability to update the replica set and are also capable of rolling back to the previous version.**
```
$ kubectl create –f Deployment.yaml --record				# Create Deployment
$ kubectl get deployments						# Fetch the Deployment
NAME           DESIRED     CURRENT     UP-TO-DATE     AVILABLE    AGE
Deployment        3           3           3              3        20s

$ kubectl rollout status deployment/Deployment				# Check the Status of Deployment
$ kubectl set image deployment/Deployment tomcat=tomcat:6.0		# Updating the Deployment
$ kubectl rollout undo deployment/Deployment –to-revision=2		# Rolling Back to Previous Deployment

```
* **Replica Set ensures how many replica of pod should be running. It can be considered as a replacement of replication controller. The key difference between the replica set and the replication controller is, the replication controller only supports equality-based selector whereas the replica set supports set-based selector.**
* **Replication Controller is responsible for managing the pod lifecycle. It is responsible for making sure that the specified number of pod replicas(or atleast one) are running at any point of time. It has the capability to bring up or down the specified no of pod.

It is a best practice to use the replication controller to manage the pod life cycle rather than creating a pod again and again.**
```
apiVersion: v1
kind: ReplicationController --------------------------> 1
metadata:
   name: Tomcat-ReplicationController --------------------------> 2
spec:
   replicas: 3 ------------------------> 3
   template:
      metadata:
         name: Tomcat-ReplicationController
      labels:
         app: App
         component: neo4j
      spec:
         containers:
         - name: Tomcat- -----------------------> 4
         image: tomcat: 8.0
         ports:
            - containerPort: 7474 ------------------------> 5
```
* **A pod is a collection of single/multiple containers and its storage inside a node of a Kubernetes cluster.**

Multi container pods are created using yaml.
Create tomcat.yml with the following contenets
```
---
apiVersion: v1
kind: Pod
metadata:
  name: Tomcat
spec:
  containers:
    - name: Tomcat
      image: Tomcat 8.0
      ports:
        - containerPort: 7500
      imagePullPolicy: Always
    - name: Database
      image: mongoDB
      ports:
        - containerPort: 7501
      imagePullPolicy: Always
```
In the above code, we have created one pod with two containers inside it, one for tomcat and the other for MongoDB.

```
$ kubectl create –f tomcat.yml
```

You can create a single pod with the following command
$ kubectl run tomcat --image=tomcat:8.0			# kubectl run <name of pod> --image=<name of the image from registry>


* **A service can be defined as a logical set of pods. It can be defined as an abstraction on the top of the pod which provides a single IP address and DNS name by which pods can be accessed. With Service, it is very easy to manage load balancing configuration. It helps pods to scale very easily.

A service is a REST object in Kubernetes whose definition can be posted to Kubernetes apiServer on the Kubernetes master to create a new instance**.

```
apiVersion: v1
kind: Endpoints
metadata:
   name: Tutorial_point_service
subnets:
   address:
      "ip": "192.168.168.40" -------------------> (Selector)
   ports:
      - port: 8080
```
In the above code, we have created an endpoint which will route the traffic to the endpoint defined as “192.168.168.40:8080”.

*Multi-Port Service Creation*
```
apiVersion: v1
kind: Service
metadata:
   name: Tutorial_point_service
spec:
   selector:
      application: “My Application” -------------------> (Selector)
   ClusterIP: 10.3.0.12
   ports:
      -name: http
      protocol: TCP
      port: 80
      targetPort: 31999
   -name:https
      Protocol: TCP
      Port: 443
      targetPort: 31998
```
##### Types of Services
**ClusterIP** − This helps in restricting the service within the cluster. It exposes the service within the defined Kubernetes cluster.
**NodePort** − It will expose the service on a static port on the deployed node. A ClusterIP service, to which NodePort service will route, is automatically created. The service can be accessed from outside the cluster using the NodeIP:nodePort.
**Load Balancer** − It uses cloud providers’ load balancer. NodePort and ClusterIP services are created automatically to which the external load balancer will route.

```
spec:
   ports:
   - port: 8080
      nodePort: 31999
      name: NodeportService
      clusterIP: 10.20.30.40
```

A full service yaml file with service type as Node Port. Try to create one yourself.
```
apiVersion: v1
kind: Service
metadata:
   name: appname
   labels:
      k8s-app: appname
spec:
   type: NodePort
   ports:
   - port: 8080
      nodePort: 31999
      name: omninginx
   selector:
      k8s-app: appname
      component: nginx
      env: env_name
```

* **A node is a working machine in Kubernetes cluster which is also known as a minion. They are working units which can be physical, VM, or a cloud instance.

Each node has all the required configuration required to run a pod on it such as the proxy service and kubelet service along with the Docker, which is used to run the Docker containers on the pod created on the node.

They are not created by Kubernetes but they are created externally either by the cloud service provider or the Kubernetes cluster manager on physical or VM machines.

The key component of Kubernetes to handle multiple nodes is the controller manager, which runs multiple kind of controllers to manage nodes. To manage nodes, Kubernetes creates an object of kind node which will validate that the object which is created is a valid node.**

### Namespace provides an additional qualification to a resource name. This is helpful when multiple teams are using the same cluster and there is a potential of name collision. It can be as a virtual wall between multiple clusters.

    * Namespaces help pod-to-pod communication using the same namespace.

    * Namespaces are virtual clusters that can sit on top of the same physical cluster.

    * They provide logical separation between the teams and their environments.

#### Create a Namespace
```
apiVersion: v1
kind: Namespce
metadata
   name: elk
```

The following command is used to control the namespace.
```
$ kubectl create –f namespace.yml ---------> 1
$ kubectl get namespace -----------------> 2
$ kubectl get namespace <Namespace name> ------->3
$ kubectl describe namespace <Namespace name> ---->4
$ kubectl delete namespace <Namespace name>
```

* **Labels are key-value pairs which are attached to pods, replication controller and services. They are used as identifying attributes for objects such as pods and replication controller. They can be added to an object at creation time and can be added or modified at the run time.

Equality-based Selectors allow filtering by key and value. Matching objects should satisfy all the specified labels.
Set-based Selectors

Set-based selectors allow filtering of keys according to a set of values.**




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
ihttps://www.tutorialspoint.com/kubernetes/kubernetes_setup.htm


It is important to set up the Virtual Datacenter (vDC) before setting up Kubernetes. This can be considered as a set of machines where they can communicate with each other via the network. For hands-on approach, you can set up vDC on PROFITBRICKS if you do not have a physical or cloud infrastructure set up.

Once the IaaS setup on any cloud is complete, you need to configure the Master and the Node.

Note − The setup is shown for Ubuntu machines. The same can be set up on other Linux machines as well.
Prerequisites

Installing Docker − Docker is required on all the instances of Kubernetes. Following are the steps to install the Docker.

Step 1 − Log on to the machine with the root user account.

Step 2 − Update the package information. Make sure that the apt package is working.

Step 3 − Run the following commands.

$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates

Step 4 − Add the new GPG key.

$ sudo apt-key adv \
   --keyserver hkp://ha.pool.sks-keyservers.net:80 \
   --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
$ echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee
/etc/apt/sources.list.d/docker.list

Step 5 − Update the API package image.

$ sudo apt-get update

Once all the above tasks are complete, you can start with the actual installation of the Docker engine. However, before this you need to verify that the kernel version you are using is correct.
Install Docker Engine

Run the following commands to install the Docker engine.

Step 1 − Logon to the machine.

Step 2 − Update the package index.

$ sudo apt-get update

Step 3 − Install the Docker Engine using the following command.

$ sudo apt-get install docker-engine

Step 4 − Start the Docker daemon.

$ sudo apt-get install docker-engine

Step 5 − To very if the Docker is installed, use the following command.

$ sudo docker run hello-world

Install etcd 2.0

This needs to be installed on Kubernetes Master Machine. In order to install it, run the following commands.

$ curl -L https://github.com/coreos/etcd/releases/download/v2.0.0/etcd
-v2.0.0-linux-amd64.tar.gz -o etcd-v2.0.0-linux-amd64.tar.gz ->1
$ tar xzvf etcd-v2.0.0-linux-amd64.tar.gz ------>2
$ cd etcd-v2.0.0-linux-amd64 ------------>3
$ mkdir /opt/bin ------------->4
$ cp etcd* /opt/bin ----------->5

In the above set of command −

    First, we download the etcd. Save this with specified name.
    Then, we have to un-tar the tar package.
    We make a dir. inside the /opt named bin.
    Copy the extracted file to the target location.

Now we are ready to build Kubernetes. We need to install Kubernetes on all the machines on the cluster.

$ git clone https://github.com/GoogleCloudPlatform/kubernetes.git
$ cd kubernetes
$ make release

The above command will create a _output dir in the root of the kubernetes folder. Next, we can extract the directory into any of the directory of our choice /opt/bin, etc.

Next, comes the networking part wherein we need to actually start with the setup of Kubernetes master and node. In order to do this, we will make an entry in the host file which can be done on the node machine.

$ echo "<IP address of master machine> kube-master
< IP address of Node Machine>" >> /etc/hosts

Following will be the output of the above command.
Output

Now, we will start with the actual configuration on Kubernetes Master.

First, we will start copying all the configuration files to their correct location.

$ cp <Current dir. location>/kube-apiserver /opt/bin/
$ cp <Current dir. location>/kube-controller-manager /opt/bin/
$ cp <Current dir. location>/kube-kube-scheduler /opt/bin/
$ cp <Current dir. location>/kubecfg /opt/bin/
$ cp <Current dir. location>/kubectl /opt/bin/
$ cp <Current dir. location>/kubernetes /opt/bin/

The above command will copy all the configuration files to the required location. Now we will come back to the same directory where we have built the Kubernetes folder.

$ cp kubernetes/cluster/ubuntu/init_conf/kube-apiserver.conf /etc/init/
$ cp kubernetes/cluster/ubuntu/init_conf/kube-controller-manager.conf /etc/init/
$ cp kubernetes/cluster/ubuntu/init_conf/kube-kube-scheduler.conf /etc/init/

$ cp kubernetes/cluster/ubuntu/initd_scripts/kube-apiserver /etc/init.d/
$ cp kubernetes/cluster/ubuntu/initd_scripts/kube-controller-manager /etc/init.d/
$ cp kubernetes/cluster/ubuntu/initd_scripts/kube-kube-scheduler /etc/init.d/

$ cp kubernetes/cluster/ubuntu/default_scripts/kubelet /etc/default/
$ cp kubernetes/cluster/ubuntu/default_scripts/kube-proxy /etc/default/
$ cp kubernetes/cluster/ubuntu/default_scripts/kubelet /etc/default/

The next step is to update the copied configuration file under /etc. dir.

Configure etcd on master using the following command.

$ ETCD_OPTS = "-listen-client-urls = http://kube-master:4001"

Configure kube-apiserver

For this on the master, we need to edit the /etc/default/kube-apiserver file which we copied earlier.

$ KUBE_APISERVER_OPTS = "--address = 0.0.0.0 \
--port = 8080 \
--etcd_servers = <The path that is configured in ETCD_OPTS> \
--portal_net = 11.1.1.0/24 \
--allow_privileged = false \
--kubelet_port = < Port you want to configure> \
--v = 0"

Configure the kube Controller Manager

We need to add the following content in /etc/default/kube-controller-manager.

$ KUBE_CONTROLLER_MANAGER_OPTS = "--address = 0.0.0.0 \
--master = 127.0.0.1:8080 \
--machines = kube-minion \ -----> #this is the kubernatics node
--v = 0

Next, configure the kube scheduler in the corresponding file.

$ KUBE_SCHEDULER_OPTS = "--address = 0.0.0.0 \
--master = 127.0.0.1:8080 \
--v = 0"

Once all the above tasks are complete, we are good to go ahead by bring up the Kubernetes Master. In order to do this, we will restart the Docker.

$ service docker restart

Kubernetes Node Configuration

Kubernetes node will run two services the kubelet and the kube-proxy. Before moving ahead, we need to copy the binaries we downloaded to their required folders where we want to configure the kubernetes node.

Use the same method of copying the files that we did for kubernetes master. As it will only run the kubelet and the kube-proxy, we will configure them.

$ cp <Path of the extracted file>/kubelet /opt/bin/
$ cp <Path of the extracted file>/kube-proxy /opt/bin/
$ cp <Path of the extracted file>/kubecfg /opt/bin/
$ cp <Path of the extracted file>/kubectl /opt/bin/
$ cp <Path of the extracted file>/kubernetes /opt/bin/

Now, we will copy the content to the appropriate dir.

$ cp kubernetes/cluster/ubuntu/init_conf/kubelet.conf /etc/init/
$ cp kubernetes/cluster/ubuntu/init_conf/kube-proxy.conf /etc/init/
$ cp kubernetes/cluster/ubuntu/initd_scripts/kubelet /etc/init.d/
$ cp kubernetes/cluster/ubuntu/initd_scripts/kube-proxy /etc/init.d/
$ cp kubernetes/cluster/ubuntu/default_scripts/kubelet /etc/default/
$ cp kubernetes/cluster/ubuntu/default_scripts/kube-proxy /etc/default/

We will configure the kubelet and kube-proxy conf files.

We will configure the /etc/init/kubelet.conf.

$ KUBELET_OPTS = "--address = 0.0.0.0 \
--port = 10250 \
--hostname_override = kube-minion \
--etcd_servers = http://kube-master:4001 \
--enable_server = true
--v = 0"
/

For kube-proxy, we will configure using the following command.

$ KUBE_PROXY_OPTS = "--etcd_servers = http://kube-master:4001 \
--v = 0"
/etc/init/kube-proxy.conf

Finally, we will restart the Docker service.

$ service docker restart

Now we are done with the configuration. You can check by running the following commands.

$ /opt/bin/kubectl get minions


# Deploying Pods

    Start a bash shell inside the hypercube container:

docker exec -it hyperkube-installer /bin/bash

    Export the Kubernetes version and processor architecture inside the container:

export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt)
export ARCH=amd64

    Download the kubectl command line tool into /usr/bin/kubectl and make it executable:

curl -sSL "http://storage.googleapis.com/kubernetes-release/release/$K8S_VERSION/bin/linux/$ARCH/kubectl" > /usr/bin/kubectl
chmod +x /usr/bin/kubectl

    Now you can run kubectl commands to retrieve information on Kubernetes state:

kubectl get nodes
kubectl get pods
kubectl get namespaces

    Start deployment of a sample nginx pod and exit the container:

kubectl run nginx --image=nginx --port=80 ; exit

    Run the command docker ps to see the new nginx containers running on the host.
    Declare the nginx pod deployment as a service and map port 80 of the nginx service to port 8080 on the host:

docker exec -it hyperkube-installer /bin/bash
kubectl expose deployment nginx --port=8080 --target-port=80

    Check that the nginx service is ready and was assigned an IP, and store it in a variable:

kubectl get service nginx
ip=$(kubectl get svc nginx --template={{.spec.clusterIP}}

    Check the nginx welcome page is there via a browser or downloading it with curl:

curl "http://$ip:8080"

