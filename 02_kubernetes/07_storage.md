# Storage

> 🚨 All exercises done below should be done in folder `07_storage`

Create a new namespace and set it as default:

```sh
kubectl create namespace my-storage
kubectl config set-context --current --namespace=my-storage
```

## PersistentVolumeClaim

In the file `pvc.yaml` add:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-demo
  namespace: my-storage
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: standard-rwo
```

Apply this and run the following:

```sh
kubectl get persistentvolumeclaims
```

*What do you notice about the value for `STATUS`?

Let's find out more with:

```sh
kubectl describe persistentvolumeclaims pvc-demo
```

What do you notice in Events?

Run the following:
```sh
kubectl get persistentvolume
```

*Notice the lack of a persistentvolume*

Let's have a Pod to use the PersistentVolumeClaim.

In `pod-pvc.yaml` add:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: pod-demo
  namespace: my-storage
spec:
  containers:
    - name: pod-demo
      image: nginx
      ports:
        - containerPort: 80
      volumeMounts:
        - mountPath: /data
          name: pvc-demo-vol
  volumes:
    - name: pvc-demo-vol
      persistentVolumeClaim:
       claimName: pvc-demo
```

Use `get pods` to ensure the pod is running

Let's see what's happening in our PersistentVolumeClaim:
```sh
kubectl describe persistentvolumeclaims pvc-demo
```

Now check the PersistentVolume with

```sh
kubectl get persistentvolumes
```

Note the size, access mode, status and claim values.

In the Google Cloud Platform - Kubernetes Engine page, select "Storage". What do you see?

# Key learning points

- PersistentVolumeClaims can be kept in a pending state until it is linked to the first consumer
- Once a pod is created linked to the PersistentVolumeClaim a PersistentVolume is automatically provisioned that is bound to the PersistentVolume and with a capacity matching the requested storage size
- In Google Cloud Platform, the PersistentVolume is linked to provisioned storage
- The RWO access mode is ReadWriteOnce and means that the PersistentVolume can be used exclusively by the pod created (other types are ReadOnlyMany and ReadWriteMany)

