City Population App

This folder contains a simple FastAPI backend, a React frontend, and a Helm chart under `helm/city-app`.

Quick steps:
- Lint the chart: `helm lint helm/city-app`
- Render templates: `helm template myrelease helm/city-app --values helm/city-app/values.yaml`
- Run backend locally: `uvicorn app:app --reload --port 8000` (from `src/backend`)
- Run frontend locally: `npm install` then `npm start` (from `src/frontend`)

Edit `helm/city-app/values.yaml` to update image names, tags and service types before deploying.
