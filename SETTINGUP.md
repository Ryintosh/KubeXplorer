# Requirements

We will be utilizing kind to set up a local cluster to demonstrate how this application works.

Follow the directions from [kind](https://kind.sigs.k8s.io/) or test in a development enviornment to see the changes this codebase will introduce.
Once you have the kubernetes cluster you want make sure you have the following:
- kubectl
- desired kubernetes objects

# Kubernetes Components


# Kubernetes Objects

For the database we will set up a ClusterIP, deployment, pv, and a pvc. To set up the database we used a postgres image from docker. We also need to set up secrets for the database, in our case we will utilize kubectl:

```
kubectl create secret generic postgres-creds \
  --from-literal=POSTGRES_USER=myuser \
  --from-literal=POSTGRES_PASSWORD=mypassword \
  --from-literal=POSTGRES_DB=mydatabase
```


Since we are using Kind, we will port-forward our database for looking at it

```
kubectl port-forward <pod-name> 5433:5432
```
