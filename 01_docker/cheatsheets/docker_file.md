# Dockerfile Sample

```Dockerfile
# The base image
FROM python:3.12-slim

# Defines an input with a default
ARG user1=someuser

# Add some metadata
LABEL "creator"="Some Dude"
LABEL "project"="Amazing Containers"

# Copy single file from host to image
COPY requirements.txt .

# Execute shell statements
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy files from host to image
COPY . /app

# Let image users know that the container listens on the given port
EXPOSE 8080

# The main process
ENTRYPOINT ["python"]

# Argument to pass to main process
CMD ["app.py"]
```