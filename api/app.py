from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import pickle
import json
import os
import re

app = FastAPI()

# -------------------------------------------------------
# PATHS & ARTIFACTS
# -------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load model, scaler, columns
model = pickle.load(open(os.path.join(MODEL_DIR, "best_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb"))
model_columns = json.load(open(os.path.join(MODEL_DIR, "model_columns.json"), "r"))

# Numeric columns are exactly these 8
numeric_cols = list(scaler.feature_names_in_)  # safer than trusting JSON

# Load location stats (generated in training)
location_stats = json.load(open(os.path.join(MODEL_DIR, "location_stats.json"), "r"))

# -------------------------------------------------------
# REQUEST BODY
# -------------------------------------------------------
class PredictRequest(BaseModel):
    total_sqft: float
    bath: float
    bhk: float
    location: str

# -------------------------------------------------------
# HELPERS
# -------------------------------------------------------
def clean_location(loc: str) -> str:
    loc = loc.strip().lower().replace("-", " ")
    loc = re.sub(r"\s+", " ", loc)
    return loc

@app.get("/")
def home():
    return {"message": "API is running!"}

# -------------------------------------------------------
# PREDICTION ENDPOINT
# -------------------------------------------------------
@app.post("/predict")
def predict_price(req: PredictRequest):

    data = req.model_dump()

    # 1) Clean location
    loc = clean_location(data["location"])

    # If location not in stats → treat as "other"
    if loc not in location_stats:
        loc = "other"

    loc_info = location_stats[loc]
    loc_mean_price = loc_info["mean_price"]
    loc_count = loc_info["count"]
    loc_category = loc_info["category"]

    # 2) Basic numeric features
    sqft = data["total_sqft"]
    bath = data["bath"]
    bhk = data["bhk"]

    sqft_per_bhk = sqft / max(bhk, 1)
    bath_per_bhk = bath / max(bhk, 1)

    # 3) Build feature row
    row = pd.DataFrame([{
        "total_sqft": sqft,
        "bath": bath,
        "bhk": bhk,
        "sqft_per_bhk": sqft_per_bhk,
        "bath_per_bhk": bath_per_bhk,
        "loc_mean_price": loc_mean_price,
        "loc_count": loc_count,
        "loc_category": loc_category
    }])

    # Ensure correct column order
    row = row[model_columns]

    # 4) Scale numeric features
    row[numeric_cols] = scaler.transform(row[numeric_cols])

    # 5) Predict
    pred = model.predict(row)[0]

    return {
        "location_used": loc,
        "predicted_price_lakhs": float(pred)
    }
