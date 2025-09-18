if helm ls -q | grep -q '^city-app$'; then
  helm upgrade city-app ./helm/city-app -f ./helm/city-app/values-minikube.yaml
else
  helm install city-app ./helm/city-app -f ./helm/city-app/values-minikube.yaml
fi
