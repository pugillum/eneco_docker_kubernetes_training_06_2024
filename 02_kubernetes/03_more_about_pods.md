# More about pods

>  🚨 All exercises done below should be done in folder `03_more_about_pods`

Create a new namespace and set it as default:

```sh
kubectl create namespace more-about-pods
kubectl config set-context --current --namespace=more-about-pods
```

## Labels

Create the file `label-pods.yaml` and apply:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-production-label-pod
  namespace: more-about-pods
  labels:
    app: my-app
    environment: production
spec:
  containers:
    - name: nginx
      image: nginx
---
apiVersion: v1
kind: Pod
metadata:
  name: my-development-label-pod
  namespace: more-about-pods
  labels:
    app: my-app
    environment: development
spec:
  containers:
    - name: nginx
      image: nginx
```

Use `describe` for one of the pods and look for the labels.

Try out a few of these commands:

```sh
kubectl get pods -l app=my-app
kubectl get pods -l environment=production
kubectl get pods -l environment=development
kubectl get pods -l environment!=production
kubectl get pods -l 'environment in (development,production)'
kubectl get pods -l app=my-app,environment=production
```

Can you see how labels could be useful when dealing with hundreds of pods? 

## Annotations

An example of Annotations, no need to apply

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-annotation-pod
  namespace: more-about-pods
  annotations:
    owner: myaccount@k8sisgr8.com
    git-commit: bdab0c6
    release-notes: |
      Version 1.2.3
      - Added feature X
      - Fixed issue Y
spec:
  containers:
  - name: nginx
    image: nginx
```

Note: Annotations **cannot** be used like labels when querying

# Debugging

Deploy the following pod by creating `broken-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: broken-pod
  namespace: more-about-pods
spec:
  containers:
    - name: busybox-container
      image: busybox:latest
      command:
        - "/bin/sh"
        - "-c"
        - "if [ $var -eq 1 ]; then echo 'Variable is equal to 1'; fi"
```

Apply the pod.  Using the following commands see if you can figure out what's wrong with the pod:

```sh
kubectl logs broken-pod
kubectl describe pod broken-pod
kubectl get pods
```

## Metrics

Create the following pod, file name `my-resource-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-resource-pod
  namespace: more-about-pods
spec:
  containers:
    - name: nginx
      image: nginx:stable

```

Try out the following:

```sh
# see CPU and memory per pod
kubectl top pods

# specific pod
kubectl top pod my-resource-pod

# kube-system
kubectl top pods -n kube-system

# the nodes
kubectl top nodes
```

> Note: you might have to wait a bit for metric server to collect metrics about your pod.


# Key learning points

- Using labels allows for easy filtering when dealing with a large number of pods
- Annotations make it possible to attach more extensive and descriptive metadata about pods
- Using `kubectl get/describe/logs` can be useful for debugging a broken pod (the issue was two things: a missing environment variable and using the default `restartPolicy`)
- Metric Server can be used with `kubectl top *` and allows one to see resource consumption for pods and nodes