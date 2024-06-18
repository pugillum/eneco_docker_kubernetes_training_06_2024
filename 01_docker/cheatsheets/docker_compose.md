# Docker Compose

## Commands

Run in the folder containing the docker-compose.

```bash
# run
docker compose up

# run detached
docker compose up -d

# run with explicit build
docker compose up --build

# stop (and tear down)
docker compose stop
```

## A simple compose.yaml

```yml
services:
  app:
    build: .
    container_name: my-app
    ports:
      - 8000:5000
```

## 2 services

```yml
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_ENV: development
  redis:
    image: "redis:alpine"
```

## Multi-stage builds

```Dockerfile
FROM python:3.12-alpine as base
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

FROM base as dev
ENV FLASK_DEBUG=1
CMD ["flask", "run"]

FROM base as prd
COPY . .
CMD ["flask", "run"]
```