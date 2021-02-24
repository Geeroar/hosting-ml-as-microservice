#!/bin/bash

kubectl create -f kubernetes
kubectl port-forward service/predict-sentiment-service 8000:80
