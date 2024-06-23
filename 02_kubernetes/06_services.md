# Services

> 🚨 All exercises done below should be done in folder `07_services`

Create a new namespace and set it as default:

```sh
kubectl create namespace my-services
kubectl config set-context --current --namespace=my-services
```

# ClusterIP Service

Create `service.yaml` and add

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  namespace: my-services
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
  namespace: my-services
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.20.1
          ports:
            - containerPort: 80

```

Notice how the Deployment is similar to the one handled in the Pod Design section.  How do you think the Service connects to the Pods?  Compare the `port` and `targetPort` values

Apply the manifest file.

Run `kubectl get service` and observe the values for the created service.  Which one is missing?  Take note of the value for "CLUSTER-IP"

Let's try to connect to the service from another Pod.  Run the following:

```sh
kubectl run -it --rm debug --image=curlimages/curl --restart=Never -- sh
```

This will start up a separate pod from which you can run [curl](https://curl.se/) a tool for connecting to URLs.

Now run:

```sh
curl <the CLUSTER-IP value>:8080
```

What do you see?

Now try this:

```sh
curl nginx-service.my-services.svc.cluster.local:8080
```
> Notice how the DNS name is of the format `<service name><namespace>.svc.cluster.local`

Exit the session with `exit` or `ctrl+D`

### Port forwarding

You can link to the service using port-forwarding.  To run it type the command:

```sh
kubectl port-forward service/nginx-service 8800:8080
```

And then access the URL http://localhost:8800 in your browser.

You can stop the port-forward with `ctrl+c`

## Load balancer

Let's apply similar code as for `ClusterIP` but now as `LoadBalancer`.  

Create the file `load-balancer.yaml` containing:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: loadbalancer-service
  namespace: my-services
spec:
  type: LoadBalancer # No longer ClusterIP
  selector:
    app: nginx-lb
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-service-lb
  namespace: my-services
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-lb
  template:
    metadata:
      labels:
        app: nginx-lb
    spec:
      containers:
        - name: nginx
          image: nginx:1.20.1
          ports:
            - containerPort: 80
```

Apply the manifest and run 

```sh
kubectl get service -w
```

Wait until an IP is displayed for "EXTERNAL-IP" (this can take a while ⏱️)

Now, in a browser go to `http:<external ip value>:8080`

You should now be able to access the `nginx` default page.

🚨 A few things to note

- Exposing a service like this is not recommended due to security, the endpoint has no authentication and has no TLS enabled (so encryption of network traffic with this endpoint)
- Services and networking should always be configured/provisioned in collaboration with the infrastructure team (or even better, configured/provisioned by them 🏆)

# Key learning points

- The `selector` field in a Service definition determine which label pods need to have in order to be included in the service
- For a `ClusterIP` service there is no External IP defined but there is an IP defined for access within the cluster
- The service can be accessed within the cluster using a specific IP or via the service's DNS name
- Port-forwarding can be used to access a service from a developer machine
- A LoadBalancer service can be configured to expose an external IP for access to a service