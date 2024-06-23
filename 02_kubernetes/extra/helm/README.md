# Helm

You'll need to install helm - [Instructions](https://helm.sh/docs/intro/install/)

## Installing a shared chart

Retrieving a repo and searching in it
```sh
# add the bitnami repo
helm repo add bitnami https://charts.bitnami.com/bitnami

# search in local repo for postgres
helm search repo postgres
```

Let's install postgres
```sh
# install postgresql chart
helm install my-postgres bitnami/postgresql --create-namespace --namespace postgres

# check the release created
helm list -n postgres
```

Delete the install and reinstall but this time overriding the postgres password:
```sh
# delete
helm delete my-postgres -n postgres

# install
helm install my-postgres bitnami/postgresql -n postgres --set global.postgresql.auth.postgresPassword="Hellomyfriends"
```

## Helm create

Helm creates a project for you, try running:
```sh
helm create demo
```

Take a look through the various files created.

## A simple Helm chart

In `simple-helm` you can see a very basic Helm setup for a single pod

Let's install on our cluster:

```sh
cd simple-helm

helm install my-helm ./ --namespace simple-helm --create-namespace
```

Now check what was installed.

You can get the manifest that was compiled using:
```sh
# get the manifest (the yaml!)
helm get manifest my-helm -n simple-helm
```

List, see the revision

```sh
helm list
```



Update the `values.yaml` (the defaults) with a different name and upgrade

```
helm upgrade my-helm ./
```


Check history with:

```sh
helm history my-helm
```

Rollback with:

```
helm rollback my-helm 1
```

Upgrade with new version of image

```sh
helm upgrade my-helm ./ --set container.image=nginx:1.20.1 
```

Create a new values.yaml file with new values and use those! 

Call it `override.yaml`

```yaml
name: my-app-prd
container:
  name: nginx
  image: nginx:stable
  port: 80
```

```sh
helm upgrade my-helm ./ --values override.yaml
```

```sh
# output all the yaml
helm template my-helm ./ > all_the_yaml.yaml
```