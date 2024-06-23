# Deployments

>  🚨 All exercises done below should be done in folder `04_deployments`

Create a new namespace and set it as default:

```sh
kubectl create namespace my-deployments
kubectl config set-context --current --namespace=my-deployments
```

## Deployments 

Create the file `single-pod.yaml` and apply:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: single-pod
  namespace: my-deployments
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
       - containerPort: 80
```

Now create the file `nginx-deployment.yaml` containing:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: my-deployments
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
```

Compare the deployment YAML with that of the pod.  What stands out?

Apply `nginx-deployment.yaml` and then `get` the pods.  What do you notice about the names?

Now open another terminal and run 

```sh
kubectl get pods -w
```
> This will watch for changes.  You can eventually stop watching using `ctrl+c`

In your first terminal, delete one of the pods with `kubectl delete pod <the pod name>`

What happens? (for extra insight: stop the watch and run `kubectl get pods` and look at the pod age)

Now run the following commands and observe what is returned:

```sh
# view the deployment
kubectl describe deploy nginx-deployment

# look at some replicasets
kubectl get replicaset

# show automatically generated labels with
kubectl get pods --show-labels
```

## Quick deployment creation

Now run the following command:
```sh
kubectl create deployment quick-deploy --image=nginx:stable --replicas=3
```

Check the deployment YAML with:
```sh
kubectl get deploy quick-deploy -o yaml
```

Why might it be a bad practice to create deployments this way?

## Rolling updates

Add the following to `rolling-deploy.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rolling-deployment
  namespace: my-deployments
spec:
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 2
  replicas: 3
  selector:
    matchLabels:
      app: rolling
  template:
    metadata:
      labels:
        app: rolling
    spec:
      containers:
        - name: nginx
          image: nginx:1.7.1
          ports:
            - containerPort: 80
```

Apply the deployment manifest.

Open a second terminal.  Run:

```sh
kubectl get pods -l app=rolling -w
```

In your original terminal, run the following to change the image version

```sh
kubectl set image deployment/rolling-deployment nginx=nginx:1.7.9
```

Observe the second terminal and what happens.  Look at what point and how many pods are terminated.

Take a look at the events in the deployment using `kubectl describe deploy rolling-deployment`

> ⚠️ Note adjusting image versions using the CLI is a bad practice.  Why do you think that might be?

### Rollouts and Rollbacks

View the rollout history by running

```sh
kubectl rollout history deployment/rolling-deployment
```

View the details of revision 2
```sh
kubectl rollout history deployment/rolling-deployment --revision=2
```

Roll back to revision 1:

```sh
kubectl rollout undo deployment/rolling-deployment
```

Check the nginx image version by using `kubectl describe deploy rolling-deployment`

Note that you can rollback to a specific version by appending `--to-revision=<number>`

Check the rollout history again.  What do you see?

# Key learning points

- With Deployments, pod names are assigned a random string
- Deployments can be created imperatively but this means having no manifest to record the origin of the deployment
- Deployments maintain a Replicaset which maintains a set number of pods.  If a pod is removed it will automatically spin up another one to achieve the set number
- Deployments support a rollout using a new replicaset for a new pod definition
- The values of `maxSurge` and `maxUnavailable` determine the timing of removal of pods and addition of new pods.
- It's possible to view a history of deployment rollouts and to revert to a previous revision