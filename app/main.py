from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(title="Healthcare Claims Risk Intelligence API")

# Load model and feature list
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "notebooks", "models", "claims_risk_model.pkl")
features_path = os.path.join(BASE_DIR, "notebooks", "models", "feature_columns.pkl")

model = joblib.load(model_path)
feature_columns = joblib.load(features_path)


@app.get("/")
def home():
    return {"message": "Healthcare Claims Risk Intelligence API Running 🚀"}


@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input dictionary to DataFrame
        df = pd.DataFrame([data])

        # Ensure correct column order
        df = df[feature_columns]

        # Predict fraud probability
        risk_score = model.predict_proba(df)[0][1]

        return {
            "risk_score": float(risk_score),
            "risk_category": "High" if risk_score > 0.5 else "Low"
        }

    except Exception as e:
        return {"error": str(e)}
