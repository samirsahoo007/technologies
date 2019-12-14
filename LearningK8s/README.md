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

