#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/abhireddy/local-codebase/City-Population-fullstack-project/city-population-app"

# create directories
mkdir -p "$ROOT/helm/city-app/templates"
mkdir -p "$ROOT/src/backend"
mkdir -p "$ROOT/src/frontend/public"
mkdir -p "$ROOT/src/frontend/src/components"
mkdir -p "$ROOT/tests/jmeter"
mkdir -p "$ROOT/tests/k6"
mkdir -p "$ROOT/tests/locust"

# helm files
touch "$ROOT/helm/city-app/Chart.yaml" "$ROOT/helm/city-app/values.yaml"
for f in backend-deployment.yaml backend-service.yaml backend-hpa.yaml frontend-deployment.yaml frontend-service.yaml elastic-deployment.yaml elastic-service.yaml; do
  touch "$ROOT/helm/city-app/templates/$f"
done

# backend files
touch "$ROOT/src/backend/app.py" "$ROOT/src/backend/db.py" "$ROOT/src/backend/requirements.txt" "$ROOT/src/backend/Dockerfile"

# frontend files
touch "$ROOT/src/frontend/package.json"
touch "$ROOT/src/frontend/public/index.html"
touch "$ROOT/src/frontend/src/App.js" "$ROOT/src/frontend/src/api.js" "$ROOT/src/frontend/src/components/CityTable.js"
touch "$ROOT/src/frontend/Dockerfile"

# tests
touch "$ROOT/tests/jmeter/city-population-test.jmx" "$ROOT/tests/jmeter/run-test.sh"
chmod +x "$ROOT/tests/jmeter/run-test.sh"
touch "$ROOT/tests/k6/test.js" "$ROOT/tests/locust/locustfile.py"

# top-level README
touch "$ROOT/README.md"

echo "Created folder structure"
