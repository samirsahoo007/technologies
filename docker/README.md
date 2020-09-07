
Try It Out

Enter this command:

docker run -it ubuntu

After a bit of spinning, you'll see a prompt like this:

root@719059da250d:/# 

Try out a few commands and then exit the container:

root@719059da250d:/# lsb_release -a

No LSB modules are available.

Distributor ID:	Ubuntu

Description:	Ubuntu 14.04.4 LTS

Release:	14.04

Codename:	trusty

root@719059da250d:/# exit

This doesn't look like much, but a lot has happened!

What you are seeing is the bash shell of an isolated container running Ubuntu, on your machine. It's yours to place with - you can install things on it, run software, whatever you want.

The above diagram is a breakdown of what just happened (the digram is from the 'Understanding the Architecture' Docker Documentation, which is great):


    We issue a docker command:

    docker: run the docker client
    run: the command to run a new container
    -it: option to give the container an interactive terminal
    ubuntu: the image to base the container on

    The docker service running on the host (our machine) checks to see if we have a copy of the requested image locally- which there isn't.
    The docker service checks the public registry (the docker hub) to see if there's an image named ubuntu available- which there is.
    The docker service downloads the image and stores it in its local cache of images (ready for next time).
    The docker service creates a new container, based on the ubuntu image.

Try any of these:

docker run -it haskell

docker run -it java

docker run -it python
