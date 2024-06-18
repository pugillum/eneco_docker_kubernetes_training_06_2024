# Exercise 04

Sunny bikes now wants to productionize their API. 
This includes persistent storage and the possibility to scale out.

Update the compose.yaml to run the following images:
- postgres:13-alpine
- Image built from supplied Dockerfile

Expected result:
- Insert data on 127.0.0.1:8080/rent?name=bob&location=texas
- Browse to url:8080 and see the inserted data
- Database is secured with password “long-distance-ice-skating”
- Database is initialized with init.sql script


Use the Dockerfile you developed in Exercise 03</br>
Fill in the compose.yaml file

Run with `docker compose up --build`

You can browse in the Postgres container with:
```bash
docker exec -ti postgres psql -U postgres
```


