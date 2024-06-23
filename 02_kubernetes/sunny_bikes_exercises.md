# Exercise 1
1. Create a YAML file with a namespace definition for `sunnybikes` and apply it
2. Create a YAML file with a pod definition for the sunnybikes application. For this, use the docker image `pugillum/sunnybikeslite:stable`. Apply this manifest.
3. Apply the configurations and check the logs of the pods with: `kubectl –n sunnybikes logs <podname>`
4. Port-forward using `kubectl port-forward pod/sunnybikes 8000:5000` and access http://localhost:8000 in your browser.  Now try http://localhost:8000/docs

# Exercise 2

1. Migrate the pod definitions for `sunnybikes` to a deployment (called `sunnybikes`).
2. The `sunnybikes` pods must be replicated at least 3 times.  
3. Make sure that when a new update of `sunnybikes` is deployed at least 1 pod is always available during upgrading and the number of pods can go up to a maximum of 6.

# Exercise 3

1. Add an additional deployment `postgres` based on the image `postgres:11-alpine`
2. Define an environment variable for the `sunnybikes` pods `PG_PORT` with value `"5432"`
3. Create a yaml file with a secret definition for the postgres password called `secret.yaml` and apply. 
4. Add the secret as environment variable to the sunny and postgres pods. SunnyBikes needs a `PG_PASSWORD` env variable and postgres needs a `POSTGRES_PASSWORD` env variable
5. Create a yaml file with a config map (`configmap.yaml`) for the postgres init schema. Mount the init script in the postgres container in the folder `docker-entrypoint-initdb.d` as file `init-schema.sql`. The schema is as follows:

```
CREATE TABLE public.bike_rides (
    uuid UUID PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    location VARCHAR(80) NOT NULL,
    created TIMESTAMPTZ NOT NULL
)
```

# Exercise 4

1. Make Postgres available to the `sunnybikes` pods from only within the cluster
1. `sunnybikes` should be adjusted to use a new image `sunnybikes:stable`
1. `sunnybikes` takes 2 environment variables to configure the postgres host and port, `PG_HOST` - `<service name>.<namespace>.svc.cluster.local` and `PG_PORT` - `"5432"` respectively. 
1. Make `sunnybikes` available on port 80 from the outside world

# Exercise 5

If the postgres pod dies,all the data is lost. 😭 Make sure all the postgres data is persistent even throughout pod restarts

Hint: Add data via the Swagger interface <br>
Hint: Postgres stores its data in `/var/lib/postgresql/data`

Verify the volume is working.

# Exercise 6

1. Add a liveness probe to check the `healthz` endpoint of the sunny bikes API.
1. Add a readiness probe to check that Postgres is ready by calling the command `pg_isready -U postgres` with a delay of 10 seconds, repeating at 10 second intervals.