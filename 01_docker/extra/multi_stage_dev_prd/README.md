# Multi stage builds - environments

First take a look at the `Dockerfile` and notice the stages defined.

Let's build the dev stage:
```sh
docker build --target dev -t multi_stage_dev .
```

Run the image:
```sh
docker run --rm multi_stage_dev:latest
```

Notice that "debug mode" is set to "on"

If you now build and run the prd version:
```sh
docker build --target prd -t multi_stage_prd .
docker run --rm multi_stage_prd:latest
```

You should now see that "debug mode" is set to "off"

This is a simple example but there are some interesting applications of this functionality, namely:
- Debugging a specific build stage
- Using a debug stage with all debugging symbols or tools enabled, and a lean production stage
- Using a testing stage in which your app gets populated with test data, but building for production using a different stage which uses real data
