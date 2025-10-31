from joblib import load
import pandas as pd
from pathlib import Path


model_path = Path(__file__).resolve().parent / "concrete_RandomForest.joblib"
model = load(model_path)

def predict_concrete_strength(features):
    new_data = pd.DataFrame([features], columns=['Cement', 'Blast Furnace Slag', 'Fly Ash', 'Water', 'Superplasticizer', 'Coarse Aggregate', 'Fine Aggregate', 'Age'])
    predicted_strength = model.predict(new_data)[0]
    return predicted_strength