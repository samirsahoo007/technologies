# docker-compose scaling web service demo
A short demo on how to use docker-compose to create a Web Service connected to a load balancer and a Redis Database.


# Installation Notes

1. Latest "traefik" version has issues. So we're using a stable version: docker.io/library/traefik:v1.7

2. Make sure that ports 80 and 8080 are free otherwise it'll throw error.
   To free the ports
	i. Check which process/PID is bound to the port
	   sudo lsof -i :8080
	ii. kill -9 <PID>

3. In order to get started be sure to clone this project onto your Docker Host. Create a directory on your host. Please note that the demo webservices will inherit the name from the directory you create. If you create a folder named test. Then the services will all be named test-web, test-redis, test-lb. Also, when you scale your services it will then tack on a number to the end of the service you scale. 

    
# How to get up and running

    docker-compose up -d

The  docker-compose command will pull the images from Docker Hub and then link them together based on the information inside the docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes we can now view the status of our stack

    docker-compose ps

Verify our service is running by either curlng the IP from the command line or view the IP from a web browser. You will notice that the each time you run the command the number of times seen is stored in the Redis Database which increments. The hostname is also reported.

### Curling from the command line
    
    ```
    curl -H Host:whoami.docker.localhost http://127.0.0.1
    
    Hostname: 2e28ecacc04b
    IP: 127.0.0.1
    IP: 172.26.0.2
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.26.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: a00d29b3a536
    X-Real-Ip: 172.26.0.1
    ``` 
    
It is also possible to open a browser tab with the URL `http://whoami.docker.localhost/`

# Scaling
Now comes the fun part of compose which is scaling. Let's scale our web service from 1 instance to 5 instances. This will now scale our web service container. We now should run an update on our stack so the Loadbalancer is informed about the new web service containers.

    docker-compose scale whoami=5
    
Now run our curl command again on our web services and we will now see the hostname change. To get a deeper understanding tail the logs of the stack to watch what happens each time you access your web services.

    ```
    $ docker-compose logs whoami

    whoami_5         | Starting up on port 80
    whoami_4         | Starting up on port 80
    whoami_3         | Starting up on port 80
    whoami_2         | Starting up on port 80
    whoami_1         | Starting up on port 80
    ```

Here's the output from my docker-compose logs after I curled the `whoami` application  so it is clear that the round-robin is sent to all 5 web service containers.

```
$ docker-compose logs | tail -1
WARNING: Some networks were defined but are not used by any service: front-tier
reverse-proxy_1  | 192.168.48.1 - - [12/Sep/2020:19:28:19 +0000] "GET / HTTP/1.1" 200 375 "-" "curl/7.64.1" 21 "Host-whoami-docker-localhost-0" "http://192.168.48.2:80" 20ms
```

# How to scale Docker Containers with Docker-Compose

What we are building is a web service with three components that are built, configured, and deployed via docker-compose.

1. HAProxy which provides us with round-robin load balancing

2. Web Application based on Python

3. Redis Database

![alt text](https://github.com/samirsahoo007/system-design-primer/blob/master/images/LB_Webapp.gif)
