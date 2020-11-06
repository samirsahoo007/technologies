# Kubernetes vs Docker: Comparing The Two Container Orchestration Giants!

Docker Swarm is a container orchestration platform, the same as Kubernetes.

| Features  |  Kubernetes |  Docker Swarm |
|---|---|---|
|  Auto-Scaling | Yes  |  No |
| Load Balancing  | Manual |  Automatic |
| Rolling Updates & Rollbacks  | Does Rolling Update & Automatic Rollbacks	   | Does Rolling Updates but No automatic Rollbacks  |
|  Data Volumes | Can share storage volumes only with other containers in same Pod  | Can share storage volumes with any other container  |
|  Logging & Monitoring | In-built tools for logging & monitoring  | 3rd party tools like ELK should be used for logging & monitoring  |
|  Scalability | Fast | 5x faster than Kubernetes  |
|  GUI | Yes | No |
|  Installation & Cluster Configuration | Complex | Easy |
|  Developed by | Google | Docker Swarm |
|  Community | Large | Small |
|  Cost | Expensive | Cheaper |



## Explain Docker Architecture?

Docker Architecture consists of a Docker Engine which is a client-server application with three major components:

A server which is a type of long-running program called a daemon process (the docker command).
A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
A command line interface (CLI) client (the docker command).
The CLI uses the Docker REST API to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI.

### How to build a Dockerfile? 

Once you’ve written a Dockerfile, you need to build it to create an image with those specifications. Use the following command to build a Dockerfile:

```
$ docker build <path to docker file>
```

## Do you know why "docker system prune" is used? What does it do?

$ docker system prune

is used to remove all the stopped containers, all the networks that are not used, all dangling images and all build caches. It’s one of the most useful docker commands.

## How To Commit Changes To A Docker Image / Modifying an Existing Docker Image

To install a custom package or modify an existing docker image we need to

Modify the Dockerfile

OR

1. Deploy the Container
2. modify the container
3. exit out of the container
4. commit the changes to the SAME container as a NEW docker image
```
sudo docker commit [CONTAINER_ID] [new_image_name]
```

## Example
```
docker run -it yhat/scienceops-python:0.0.2 /bin/bash
root@5c1ac3a4d2f2: e8f0671518a2 #
```

```
# sudo apt-get install vim
# export AWS_SECRET_KEY=mysecretkey123
# export AWS_ACCESS_KEY=fooKey
```

`# exit`

```
docker commit e8f0671518a2 yhat/scienceops-python:0.0.3
```

Test it.
```
$ docker run -it yhat/scienceops-python:0.0.3 echo $AWS_SECRET_KEY
```

Now push it

```
docker login
docker push <username/image name>
```

# docker-compose:

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a Compose file to configure your application's services. Then, using a single command, you create and start all the services from your configuration.

Using Compose is basically a three-step process.

1. Define your app's environment with a Dockerfile so it can be reproduced anywhere.

2. Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.

3. Lastly, run docker-compose up and Compose will start and run your entire app.

A docker-compose.yml looks like this:

```
version: '2'

services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: redis
```

# How to Merge Two Docker Images

image1 --
            \
             ---> merged_image_12
            /
image2 --


It can be possible when you have Dockerfile.

## But how is it possible when you do not have Dockerfile?
e.g. if you spend most of the time using ready images from Docker Hub, you do not have their source Dockerfile. Then how to merge them?

Here is the trick to achieve this...

```
docker pull image1
docker pull image2
```

Then, use docker history to get the commands that were used to build them.

```
docker history --no-trunc=true image1 > image1-dockerfile
docker history --no-trunc=true image2 > image2-dockerfile
```

Then, open these two files. You can then see the command stack of each image. This holds true because of the fact that Docker images are structured into layers (read more at http://www.centurylinklabs.com/optimizing-docker-images/). That is, each command you type in the Dockerfile builds a new image on top of previous images from previous commands. Therefore, you can reverse-engineer images.

### Restrictions

The only scenario when you will not be able to reverse-engineer an image is when the maintainer of the image has used ADD or COPY commands in his Dockerfile. You will see a line like:

```
ADD file:1ac56373f7983caf22
or 
ADD dir:cf6fe659e9d21535844
```

This is because you cannot get what local files the maintainer used on his machine to include in this image.

# Basics

## What is Docker?

| Criteria  |  Docker |  Virtual Machines  |
|---|---|---|
|  Use of OS | All containers share the host OS  |  Each VM runs on its own OS |
| Startup time  | Very fast  |  Slow |
| Isolation  |Process-level isolation	   | Full isolation  |
|  Security | Low  | High  |


We can define Docker as a containerization platform that combines all our applications in a package so that we have all the dependencies to run our applications in any environment. This means, our application will run seamlessly on any environment, and this makes it easy for having a product-ready application. What Docker does is wrap the software needed in a file system that has everything for running the code, providing the runtime and all the necessary libraries and system tools. Containerization technology like Docker will share the same operating system kernel with the machine, and due to this it is extremely fast. This means that we have to run Docker only at the beginning and after that, since our OS is already running, we will have a smooth and seamless process.

## What is a Docker Namespace?
A namespace is one of the Linux features and an important concept of containers. Namespace adds a layer of isolation in containers. Docker provides various namespaces in order to stay portable and not affect the underlying host system. Few namespace types supported by Docker – PID, Mount, IPC, User, Network

## What is Docker Machine?

Docker machine is a tool that lets you install Docker Engine on virtual hosts. These hosts can now be managed using the docker-machine commands. Docker machine also lets you provision Docker Swarm Clusters.

## What changes are expected in your docker compose file while moving it to production?
These are the following changes you need make to your compose file before migrating your application to the production environment:

Remove volume bindings, so the code stays inside the container and cannot be changed from outside the container.
Binding to different ports on the host.
Specify a restart policy
Add extra services like log aggregator

## How do you scale your Docker containers?

Docker containers can be scaled to any level, starting from a few hundreds to even thousands or millions of containers. The only condition is that the containers need the memory and the OS all the time, and there should not be a constraint on these when the Docker is getting scaled.

## Will you lose your data, when a docker container exists?

No, you won’t lose any data when Docker container exits. Any data that your application writes to the container gets preserved on the disk until you explicitly delete the container. The file system for the container persists even after the container halts.

## Is it possible to use JSON instead of YAML for Docker Compose?

We can use JSON instead of YAML for a Docker Compose file.

docker-compose -f docker-compose.json up

## What is the use of a Dockerfile?

A Dockerfile is a set of specific instructions that we need to pass on to Docker so that the images can be built. We can think of the Dockerfile as a text document which has all the commands that are needed for creating a Docker image. We can create an automated build that lets us execute multiple command lines one after the other.

## What is a Docker Swarm?

We can think of a Docker Swarm as the way of orchestrating the Docker containers. We will be able to implement Dockers in a cluster. We can convert our Docker pools into a single Docker Swarm for easy management and monitoring. Also you can use kubernetes for orchestration.

## Have you used Kubernetes? If you have, which one would you prefer amongst Docker and Kubernetes?

Be very honest in such questions. If you have used Kubernetes, talk about your experience with Kubernetes and Docker Swarm. Point out the key areas where you thought docker swarm was more efficient and vice versa. Have a look at this blog for understanding differences between Docker and Kubernetes.

You Docker interview questions are not just limited to the workarounds of docker but also other similar tools. Hence be prepared with tools/technologies that give Docker competition. One such example is Kubernetes.


## What, in your opinion, is the most exciting potential use for Docker?

The most exciting potential use of Docker that I can think of is its build pipeline. Most of the Docker professionals are seen using hyper-scaling with containers, and indeed get a lot of containers on the host that it actually runs on. These are also known to be blatantly fast. Most of the development – test build pipeline is completely automated using the Docker framework.

## What’s the difference between up, run, and start?

Using the command UP, you can start or restart all the services that are defined in a docker-compose.yml file. In the "attached" mode, which is also the default mode – we will be able to see all the log files from all the containers. In the "detached" mode, it exits after starting all the containers, which continue to run in the background showing nothing over in the foreground.

Using docker-compose run command, we will be able to run the one-off or the ad-hoc tasks that are required to be run as per the Business needs and requirements. This requires the service name to be provided which you would want to run and based on that, it will only start those containers for the services that the running service depends on.

Using the docker-compose start command, you can only restart the containers that were previously created and were stopped. This command never creates any new Docker containers on its own.

## Is there a possibility to include specific code with COPY/ADD or a volume?

This can be easily achieved by adding either the COPY or the ADD directives in your dockerfile. This will count to be useful if you want to move your code along with any of your Docker images, example, sending your code an environment up the ladder – Development environment to the Staging environment or from the Staging environment to the Production environment. 

Having said that, you might come across situations where you’ll need to use both the approaches. You can have the image include the code using a COPY, and use a volume in your Compose file to include the code from the host during development. The volume overrides the directory contents of the image.

## What’s the benefit of “Dockerizing?”

Dockerizing enterprise environments helps teams to leverage over the Docker containers to form a service platform as like a CaaS (Container as a Service). It gives teams that necessary agility, portability and also lets them control staying within their own network / environment.

Most of the developers opt to use Docker and Docker alone because of the flexibility and also the ability that it provides to quickly build and ship applications to the rest of the world. Docker containers are portable and these can run on any environment without making any additional changes when the application developers have to move between Developer, Staging and Production environments. This whole process is seamlessly implemented without the need of performing any recoding activities for any of the environments. These not only helps reduce the time between these lifecycle states, but also ensures that the whole process is performed with utmost efficiency. There is every possibility for the Developers to debug any certain issue, fix it and also update the application with it and propagate this fix to the higher environments with utmost ease.

The operations teams can handle the security of the environments while also allowing the developers build and ship the applications in an independent manner. The CaaS platform that is provided by Docker framework can deploy on-premise and is also loaded with full of enterprise level security features such as role-based access control, integration with LDAP or any Active Directory, image signing and etc. Operations teams have heavily rely on the scalability provided by Docker and can also leverage over the Dockerized applications across any environments.

Docker containers are so portable that it allows teams to migrate workloads that run on an Amazon’s AWS environment to Microsoft Azure without even having to change its code and also with no downtime at all. Docker allows teams to migrate these workloads from their cloud environments to their physical datacenters and vice versa. This also enables the Organizations to focus on the infrastructure from the gained advantages both monetarily and also the self-reliability over Docker. The lightweight nature of Docker containers compared to traditional tools like virtualization, combined with the ability for Docker containers to run within VMs, allowing teams to optimize their infrastructure by 20X, and save money in the process.

## Will cloud automation overtake containerization any sooner?

Docker containers are gaining the popularity each passing day and definitely will be a quintessential part of any professional Continuous Integration / Continuous Development pipelines. Having said that there is equal responsibility on all the key stakeholders at each Organization to take up the challenge of weighing the risks and gains on adopting technologies that are budding up on a daily basis. In my humble opinion, Docker will be extremely effective in Organizations that appreciate the consequences of Containerization.

## What are the differences between the ‘docker run’ and the ‘docker create’?

‘docker create’ command we can create a Docker container in the Stopped state. 

We can also provide it with an ID that can be stored for later usages as well.
This can be achieved by using the command ‘docker run’ with the option –cidfile FILE_NAME as like this:
‘docker run –cidfile FILE_NAME’

## Can you remove a paused container from Docker?

No, first STOP then RM

## Is there a possibility that a container can restart all by itself in Docker?

No, it is not possible. The default –restart flag is set to never restart on its own. If you want to tweak this, then you may give it a try.

## What platforms does docker run on?

This is a very straightforward question but can get tricky. Do some company research before going for the interview and find out how the company is using Docker. Make sure you mention the platform company is using in this answer.

Docker runs on various Linux administration:

Ubuntu 12.04, 13.04 et al
Fedora 19/20+
RHEL 6.5+
CentOS 6+
Gentoo
ArchLinux
openSUSE 12.3+
CRUX 3.0+
It can also be used in production with Cloud platforms with the following services:

Amazon EC2
Amazon ECS
Google Compute Engine
Microsoft Azure
Rackspace

# Is it a good practice to run stateful applications on Docker?

The concept behind stateful applications is that they store their data onto the local file system. You need to decide to move the application to another machine, retrieving data becomes painful. I honestly would not prefer running stateful applications on Docker.

## Suppose you have an application that has many dependant services. Will docker compose wait for the current container to be ready to move to the running of the next service?

The answer is yes. Docker compose always runs in the dependency order. These dependencies are specifications like depends_on, links, volumes_from, etc.

## How will you monitor Docker in production?

Docker provides functionalities like docker stats and docker events to monitor docker in production. Docker stats provides CPU and memory usage of the container. Docker events provide information about the activities taking place in the docker daemon.

## Is it a good practice to run Docker compose in production?

Yes, using docker compose in production is the best practical application of docker compose. When you define applications with compose, you can use this compose definition in various production stages like CI, staging, testing, etc.

## Are you aware of load balancing across containers and hosts? How does it work?

While using docker service with multiple containers across different hosts, you come across the need to load balance the incoming traffic. Load balancing and HAProxy is basically used to balance the incoming traffic across different available(healthy) containers. If one container crashes, another container should automatically start running and the traffic should be re-routed to this new running container. Load balancing and HAProxy works around this concept.
