from fastapi import FastAPI, Header, HTTPException, Depends
import os, hmac
from app.functions import predict_concrete_strength

# Create FastAPI instance
app = FastAPI()

# Load API Key from environment variable
# For local testing, you can set this variable during docker run. e.g., docker run - p 8000:8000 -e API_KEY="your_secret_key" concrete-api:latest
# For cloud deployment platforms, set the environment variable in the platform's settings.
API_KEY = os.environ.get("API_KEY")

def verify_api_key(x_api_key: str = Header(None)):
    """
    Check if the provided x-api-key header matches the API_KEY secret.
    """
    if not x_api_key or not API_KEY or not hmac.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid or missing API key")
    return True

# API Routes

@app.get("/")
def health_check():
    return {"status": "Concrete Strength API is running"}

@app.get("/info")
def info():
    return {"info": "This API predicts concrete strength based on input features."}

@app.get("/predict")
def predict_strength(
    cement: float,
    blast_furnace_slag: float,
    fly_ash: float,
    water: float,
    superplasticizer: float,
    coarse_aggregate: float,
    fine_aggregate: float,
    age: int,
    _: bool = Depends(verify_api_key)  # <-- Require API key for this route
):
    features = [cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]
    predicted_strength = predict_concrete_strength(features)
    return {"predicted_strength": predicted_strength}
