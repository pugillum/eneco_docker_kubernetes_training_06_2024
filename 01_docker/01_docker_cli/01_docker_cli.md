# Docker CLI

> When doing these work-alongs make sure you are in the folder `01_docker_cli` in your terminal.

## pull, images and tag

Pull a new image  

```
docker pull nginx:latest
```

View your images

```sh
docker images
```

Remove the image

```
docker rmi nginx:latest
```

Check to see that the image has been removed.

Tag the `busybox` image (you should have this image already from the first exercise, if not, fetch it with `docker pull busybox`)

```sh
docker tag busybox:latest my-image:v1
```

Look at your list of images.  What do you notice about the image ID?

## run and ps

Ensure you have two terminals open

Run the following:

```sh
docker run busybox sh -c "while true; do $(echo date); sleep 1; done"
```

In the other terminal run

```
docker ps
```

What do you observe?

In the first terminal, stop the container run with "Ctrl+C" 

Run `docker ps` , followed by `docker ps -a` and observe the result

Repeat the `docker run ...` command above and in the other terminal run `docker ps`. Observe the name of the container and run

```
docker stop <name of container>
```

Again, run `docker ps` , followed by `docker ps -a` and observe the result.

### Automatic removal

Clear all exited containers with the following:

```sh
docker rm $(docker ps -aq)
```

Now run:

```sh
docker run --rm busybox sh -c "while true; do $(echo date); sleep 1; done"
```

Stop the container and check for exited containers (`docker ps -a`)

## Volumes (-v)

Run the following:

```sh
docker run --rm -ti -v vol_demo:/app busybox
```

You should now be in the container, the terminal should show something like `/ #`.

Still in the container, open the folder `app` with `cd app` and create a file with `touch bla.txt`.

Exit the container by typing `exit` or using `Ctrl+D`

Rerun the `docker run ...` from above and check in the `app` folder (run `ls app`).  What do you see?

Exit the container.

Now run

```sh
docker volume ls
```

Find your volume.  Inspect it with

```sh
docker volume inspect vol_demo
```

## Bind mounts (-v)

Access the folder containing this document in your terminal.

Now run

```sh
docker run --rm -ti -v $(pwd):/app busybox # Linux/MacOS
docker run --rm -ti -v ${PWD}:/app busybox # Windows
```

Access the `app` folder, you should see the file `some_text.txt`.  Edit it using `vi` and adjust the text ("i" to insert text, "Esc" followed by `:wq` to write and exit)

Exit the container and check the contents of `some_text.txt` on your machine.

## Port mapping

Run the following

```sh
docker run --rm -p 8000:5000 pugillum/simple_web_app
```

Open the link shown in the logs (http://127.0.0.1:5000).  What do you see? 

Now try the same URL using port 8000.

## Environment variables

Run the following

```
docker run -e FOO=bar --rm -it busybox sh
```

In the container shell, run

```sh
echo $FOO
```

Exit the shell.

Now run the following

```
docker run --env-file bla.env --rm -it busybox sh
```

And then run `printenv | grep BAR` and note the result.

## Detached mode, logs, named containers

Run

```sh
docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
```

Note the output in the terminal.

Now run

```
docker logs -f --until=2s test
```

Stop the container with

```
docker stop test
```

## Executing commands

> Note, this will not run in a PowerShell

Open two terminals, in the first run:

```sh
docker run --name test_exec --rm busybox sh -c "while true; do echo \$(date -u)'#This is log' >> file.log; sleep 3; done"
```

In the second run

```sh
docker exec -it test_exec sh
```

Output the `file.log` with

```sh
cat file.log
```

Exit (ctrl-D) and now try:

```sh
docker exec test_exec tail -f file.log
```

What power have you unlocked here? 🦸

## prune, inspect and history

Run the following commands and observe the results:

```sh
# prune your images
docker system prune

# inspect an image
docker inspect busybox:latest

# check history on an image
docker pull python:3.12-slim
docker history python:3.12-slim
```

# Key learning points
- Docker allows you to pull images to your local machine
- These images can be viewed and removed
- The same image can have multiple tags
- Running containers can be viewed with `docker ps`
- Once a container has stopped running, it remains as a stopped container and can be viewed with `docker ps -a`
- Each new container will be assigned a new name
- `--rm` flag can be used to remove containers once they have stopped
- Volumes allow persisting of data between containers
- Volumes can be listed and inspected
- Bind mounts allow linking of directories from the host machine to the container
- Port mapping maps a host port to a container port and allows external access to services running in the container
- Environment variables can be mapped to a container, individually or with a file
- It's possible to run a container detached without linking the terminal to its input and output.
- Docker provides the possibility to link to the container logs separately with `docker logs`
- Docker makes it possible to run separate commands in a container using `docker exec`
- You can clear out unused data and free up disk space with `docker prune`
- The metadata about an image can be viewed with `docker inspect`
- `docker history` allows one to see the layers that make up and image and the commands used to create those layers.

