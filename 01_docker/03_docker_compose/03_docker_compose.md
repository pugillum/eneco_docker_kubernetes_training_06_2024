# Docker Compose

## Shifting from CLI to Docker Compose

Open `simple_flask` in your terminal.  It contains a `Dockerfile`.  Think about how you would build and run it using `docker build` and `docker run`

In the same folder, create a file 'compose.yaml' containing the following:

```yaml
services:
  app:
    build: .
    container_name: my-app
    stop_signal: SIGINT
    ports:
      - 8000:5000
```

Now run the following:

```
docker compose up --build
```

Access http://localhost:8000 in your browser

Stop running with `Ctrl+C`

Check for exited containers with `docker ps -a`

Now run

```sh
docker compose down
```

Again check for exited containers.

## About `--build`

Now in `app.py` change "Hello World!" to "Hi World!" and save.

Now run 

```sh
docker compose up # so without --build
```

Access http://localhost:8000.  What do you notice?

Now try again with `--build` and check the browser.

## Env files

In `simple_flask` add a file `.env` containing:

```sh
NAME="<your name>"
```

Change the `app.py` code to the following:

```py
from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    name = os.environ.get("NAME", "John")
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

Change your `compose.yaml` to the following:

```yaml
services:
  app:
    build: .
    container_name: my-app
    stop_signal: SIGINT
    ports:
      - 8000:5000
    env_file:
      - .env
```

Run `docker compose up --build` and again access http://localhost:8000 to verify that it works.





## Multiple containers

For this you will require two terminals.

Open `multiple_containers` in your first terminal

Run

```sh
docker compose up
```

And then go to http://localhost:8000.  Refresh the page and note what is displayed.

In your second terminal, run `docker ps` to see what is running.

In your first terminal, stop by using `Ctrl+C`

Take a look at the `compose.yaml` file to see how this matches with what you observed.

## Developing with Docker Compose (and mounts)

Still in `multiple_containers`, edit the `compose.yaml` file and add the line:

```
		volumes:
      - .:/app
```

> `volumes:` should line up with `depends_on:`

Run

```
docker compose up --build
```

Go to http://localhost:8000 and observe the message being displayed.  

Now open `app.py` and adjust the "Hi" to "Hello" and save.

Return to http://localhost:8000 and refresh the page.  What you do see?

# Key learning points

- Using Docker Compose allows a declarative way of running containers that does build and run in one step
- When containers created by Docker Compose are stopped they are retained (this ensures faster startup) and can be removed with `docker compose down`
- To ensure recreation of containers use `--build`
- Docker Compose supports the use of an environment variable file
- Docker Compose supports the running of multiple containers from different images
- By using mounts with Docker Compose you can recreate a specific development environment using containers and have your file changes immediately picked up in that environment