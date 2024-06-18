# Multi-stage optimization

Take a look at `Dockerfile_small` and compare it to `Dockerfile_big` - what are the differences?

Now let's build images for both, run the following commands in the terminal in this folder:
```sh
docker build -t fastapi_small -f Dockerfile_small .
docker build -t fastapi_big -f Dockerfile_big .
```

Now run `docker images` and compare the image size.
