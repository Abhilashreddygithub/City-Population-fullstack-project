City Population App

This folder contains a simple FastAPI backend, a React frontend, and a Helm chart under `helm/city-app`.

Quick steps:
- Lint the chart: `helm lint helm/city-app`
- Render templates: `helm template myrelease helm/city-app --values helm/city-app/values.yaml`
- Run backend locally: `uvicorn app:app --reload --port 8000` (from `src/backend`)
- Run frontend locally: `npm install` then `npm start` (from `src/frontend`)

Edit `helm/city-app/values.yaml` to update image names, tags and service types before deploying.

Minikube deployment (quick guide)
1. Start Minikube and enable Docker env:

```bash
minikube start --driver=docker
eval "$(minikube -p minikube docker-env)"
```

2. Build backend and frontend images (from repo root):

```bash
# backend
docker build -t city-backend:latest -f src/backend/Dockerfile src/backend
# frontend
docker build -t city-frontend:latest -f src/frontend/Dockerfile src/frontend
```

3. Install Helm chart with minikube overrides:

```bash
helm upgrade --install city-app helm/city-app -f helm/city-app/values-minikube.yaml
```

4. Check pods and services:

```bash
kubectl get pods -n default
kubectl get svc -n default
```

5. Access frontend on NodePort (example port 30080):

```bash
minikube service --url city-app-frontend
# or open http://$(minikube ip):30080
```

