


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


