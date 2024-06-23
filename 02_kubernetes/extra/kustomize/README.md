# Kustomize

This folder contains an example use of Kustomize demonstrating:
- bases and overlays
- patching
- cross-cutting fields


Create two namespaces:
```sh
kubectl create namespace dev-env
kubectl create namspapce prd-env
```

To see the generated code for `dev` run:
```sh
kubectl kustomize ./overlays/dev
```


To deploy the dev environment, run:
```sh
kubectl apply -k ./overlays/dev
```

To deploy the prd environment, run:
```sh
kubectl apply -k ./overlays/prd
```

