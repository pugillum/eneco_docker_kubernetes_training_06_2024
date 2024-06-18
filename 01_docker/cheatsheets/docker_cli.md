# Docker CLI

Here's a list of commands demonstrated during part 2 of the course:
```bash
# See all commands
docker

# run
docker run --rm -ti python:3.12

# list all docker images
docker images

# push image to a registry
docker push IMAGE

# pull from a registry
docker pull IMAGE

# remove image
docker rmi IMAGE

# list running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Volume
docker run --rm -ti -v vol_demo:/app busybox

# View volumes
docker volume ls

# Inspect volumes
docker volume inspect [name]

# Remove a volume
docker volume rm [name]

# bind mounts
docker run --rm -ti -v $(pwd):/app busybox

# launch into a running container
docker exec -ti CONTAINER sh

# ports
docker run -p HOST_PORT:CONTAINER_PORT IMAGE

# ports demo
docker run -p 8000:5000 training/webapp python app.py

# run environment variables
docker run -e VARIABLE=VALUE IMAGE
docker run -e PASSWORD=supersecret123! webserver

# detached mode and logs
docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
docker logs -f --until=2s test

# give it a name
docker run --name postgres postgres

# stop container
docker stop CONTAINER

# hard stop container
docker kill CONTAINER

# stop and remove container
docker rm CONTAINER

# docker logs
docker logs -f CONTAINER

# inspect an image
docker inspect IMAGE

# see full command history
docker history --no-trunc IMAGE

# to tag an image
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
docker tag busybox:latest mybusybox:v1
```