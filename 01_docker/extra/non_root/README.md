# Using a non-privileged user

When defining a Docker image it's a best practice to ensure the use of a non-privilege user and ensure processes run for this user rather than `root`

## First as `root` user

In this folder run:
```sh
docker build -t hello_root -f Dockerfile_root .
```

Once the image is built, run the following to test that it works:
```sh
docker run --rm hello_root:latest
```

Now let's see what we could do if gaining access to the container as `root` user:

Run
```sh
docker run --rm -it --entrypoint /bin/bash hello_root:latest
```

You should now see a terminal prompt indicating your access as `root`.  Now let's install `curl`

Run the following lines:
```sh
echo "deb http://deb.debian.org/debian buster main" >> /etc/apt/sources.list
apt-get update
apt-get install curl
```

You have now managed to install `curl` which you could use to download all kinds of mischievous packages. 😈

## As a non-privileged user

Now let's build from the other Dockerfile:
```sh
docker build -t hello_non_root -f Dockerfile_non_root .
```

You can test if it works if you like but let's see what kind of access we have, first run the following:
```sh
docker run --rm -it --entrypoint /bin/bash hello_non_root:latest
```

Now try to fun that first command that adds the first command that appends the Debian Buster repository to the `sources.list` file:
```sh
echo "deb http://deb.debian.org/debian buster main" >> /etc/apt/sources.list
```

🤨 What do you see? 

