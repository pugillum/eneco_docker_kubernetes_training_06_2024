# Pods Advanced

>  🚨 All exercises done below should be done in folder `08_pods_advanced`

Create a new namespace and set it as default:

```sh
kubectl create namespace pods-advanced
kubectl config set-context --current --namespace=pods-advanced
```

## Liveness probe

In `liveness-pod.yaml` add:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-pod
  namespace: pods-advanced
spec:
  containers:
    - name: busybox
      image: busybox:stable
      command:
        [
          "sh",
          "-c",
          "touch /tmp/healthy; sleep 20; rm -f /tmp/healthy; sleep 600",
        ]
      livenessProbe:
        exec:
          command: ["cat", "/tmp/healthy"]
        initialDelaySeconds: 5
        periodSeconds: 5
```

And apply.

Watch the pod status with 

```
kubectl get pods -w
```

*What happens after 20 seconds?*

Use `kubectl describe liveness-pod` to see what is happening.

## Readiness probe

An example of `readinessProbe`, no need to apply

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: readiness-pod
  namespace: pods-advanced
spec:
  containers:
    - name: nginx
      image: nginx:1.20.1
      readinessProbe:
        httpGet:
          path: /
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 5
```

# Key learning points

- Liveness probes can be used to determine if a pod is broken and needs to be restarted.
- Liveness probes can have a delay before checking and can be configured to check at a certain frequency
- Readiness probes look a lot like liveness probes but are used to determine if traffic can be directed to a pod.