# Concrete Compressive Strength Prediction API

This repository provides a **FastAPI web service** that predicts the **compressive strength of concrete** (in MPa) based on its mix components.  
It wraps a pre-trained **Random Forest regression model** and exposes it as a lightweight REST API that can be run locally via Docker or deployed to the cloud.

---

## 🚀 Overview

The model was trained on the [Concrete Compressive Strength Dataset](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) from the UCI Machine Learning Repository.  
The API allows users to send material composition parameters and receive a predicted concrete strength.

The model used in this API was developed and optimized in the companion repository:  
👉 [Concrete Strength Prediction Model Training](https://github.com/ApostolosApostolou/concrete-strength-prediction-model-training)

---

## ⚙️ How to Use

### **Build the Docker image & Run a Container**

In the project root (where the `Dockerfile` is located), run:

```bash
docker build -t concrete-api:latest .
```

```bash
docker run - p 8000:8000 -e API_KEY="your_secret_key" concrete-api:latest
```

## API Key Authentication

This API includes an API key authentication mechanism to restrict access when deployed on the web (e.g., on Google Cloud Run).
This ensures that only authorized users with a valid API key can use the model.

- For local testing, the API Key is defined by the user during container initialization.
- For cloud deployment, set the environment variable in the platform's settings.

The API key must be included in the request header as follows:
```bash
x-api-key: YOUR_SECRET_KEY
```

If a request is made without the correct key, the API will return:

```bash
{"detail": "Unauthorized: Invalid or missing API key"}
```

### Example Authorized Request
Using curl:
```bash
curl -H "x-api-key: YOUR_SECRET_KEY" "http://localhost:8080/predict?cement=500&blast_furnace_slag=2&fly_ash=1&water=200&superplasticizer=3&coarse_aggregate=1000&fine_aggregate=700&age=25"
```

Using Python:

```bash
import requests

url = "http://localhost:8080/predict"
headers = {"x-api-key": "YOUR_SECRET_KEY"}
params = {
    "cement": 500,
    "blast_furnace_slag": 2,
    "fly_ash": 1,
    "water": 200,
    "superplasticizer": 3,
    "coarse_aggregate": 1000,
    "fine_aggregate": 700,
    "age": 25
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

## Model File and Reproducibility

The final trained model (`concrete_RandomForest.joblib`) is tracked using **[Git Large File Storage (Git LFS)](https://git-lfs.github.com/)** to handle its larger size efficiently.  
If you have Git LFS installed, the file will be downloaded automatically when you clone the repository:

```bash
git clone https://github.com/ApostolosApostolou/concrete-strength-prediction-api
```
