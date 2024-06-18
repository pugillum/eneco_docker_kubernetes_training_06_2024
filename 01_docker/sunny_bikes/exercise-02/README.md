# Exercise 02

Use the Docker CLI to run a container that:
- retrieves the image `pugillum/sunny_bikes_flask`
- mounts the file `data.txt` in this folder to `/root/data`
- sets environment variable `DATA_PATH` to the file mounted in `/root/data`
- sets environment variable `FLASK_PORT` to `8080`
- allows access on `localhost:8080`
- removes container when done
