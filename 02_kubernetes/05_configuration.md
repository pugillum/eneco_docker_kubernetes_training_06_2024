# Configuration

> 🚨 All exercises done below should be done in folder `05_configuration`

Create a new namespace `my-configuration` and select it instead of `default`. 

## Environment variables

Create a new pod using `my-pod-env.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-env
  namespace: my-configuration
spec:
  containers:
    - name: busybox
      image: busybox:stable
      command: ["sh", "-c", "while true; do echo $MESSAGE $NAME; sleep 5; done;"]
      env:
        - name: MESSAGE
          value: "Hello"
        - name: NAME
          value: "John"
```

Check the pod logs.

*If the values of `MESSAGE` and `NAME` were shared amongst multiple pods, what would that mean in terms of updating?*

## ConfigMap

Create the file `my-config-map.yaml` containing

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
  namespace: my-configuration
data:
  # key value style
  message: hello
  name: John

  # file style
  app.cfg: |
    message=howdy
    name=Mary

```

And apply.

Try out the following commands:

```sh
kubectl get configmap my-configmap -n my-configuration
kubectl describe configmap my-configmap -n my-configuration
```

Now let's use our ConfigMap

Create `my-pod-cf.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-cf
  namespace: my-configuration
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox:stable
      command: ["sh", "-c", "while true; do echo $MESSAGE $NAME; sleep 5; done;"]
      env:
        - name: MESSAGE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: message
        - name: NAME
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: name
```

Now check the pod logs with

```sh
kubectl logs my-pod-cf -f # this will follow the logs
```

Stop following the logs with `ctrl+c`

Change `hello` to `hi` in `my-config-map.yaml` and reapply (no delete necessary).  

*How does this affect the pod logs? What's going on here?*

Delete the pod `my-pod-cf`

### ConfigMap using volumes

Create the file `my-pod-cf-volumes.yaml` containing:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-cf-volumes
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox:stable
      command: ["sh", "-c", "while true; do cat /config/app.cfg; sleep 5; done;"]
      volumeMounts:
        - name: config
          mountPath: /config
          readOnly: true
  volumes:
    - name: config
      configMap:
        name: my-configmap
        items:
          - key: app.cfg
            path: app.cfg
```

Apply this and then check the logs of the new pod using `kubernetes logs my-pod-cf-volumes -f`

> Note: if you're not seeing the pod, check your namespace 😊

Now make changes to the message or name in `my-config-map.yaml` for `app.cfg` and re-apply this file (in a separate terminal instance)

*Observe the logs for the pod for a while, what do you notice?*

## Secrets 🤫

Add this to `my-secret.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: my-configuration
stringData:
  secret1: icollectrocks
data:
  secret2: aWJyaW5ndGhlc3VudXB3aXRobXltaW5kCg==
---
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-with-secrets
  namespace: my-configuration
spec:
  restartPolicy: Never
  containers:
    - name: busybox
      image: busybox:stable
      command:
        [
          "sh",
          "-c",
          "while true; do echo $SECRET1 and $SECRET2; sleep 5; done;",
        ]
      env:
        - name: SECRET1
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: secret1
        - name: SECRET2
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: secret2
```

Apply the manifest and check the logs of the pod `my-pod-with-secrets`

Retrieve the secret value as YAML using:
```sh
kubernetes get secret my-secret -o yaml
```

What do you notice about `secret1`.

Run the following on the value of `secret2`:
```sh
echo aWJyaW5ndGhlc3VudXB3aXRobXltaW5kCg== | base64 -d
```

*How secure do you think secrets really are? Is it a good idea to store secret values in the manifest?*

# Key learning points

- Environment variables are useful for values linked to a single pod definition
- For values that may be accessed across different pod contexts use configuration maps (for non-sensitive data)
- Configuration maps have two forms:
  - key-value style
  - file style
- Values mapped to environment variables are set on start of a pod (and require a new pod run for changes)
- Values mapped via volume mount will eventually be synced to the pod
- Secrets can be created separately, either in string format or base64 encoded and will be stored as base64 encoded
- Secrets are decoded when used in a pod
- 🚨 The base level functionality for secrets in Kubernetes is not very secure!
