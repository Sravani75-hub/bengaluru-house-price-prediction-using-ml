import streamlit as st
import requests
import json
import os

st.title("🏠 Bengaluru House Price Prediction")

# -------------------------------------------------------
# LOAD LOCATION LIST FROM location_stats.json
# -------------------------------------------------------
MODEL_DIR = "../models"
loc_stats_path = os.path.join(MODEL_DIR, "location_stats.json")

with open(loc_stats_path, "r") as f:
    location_stats = json.load(f)

# All locations except "other"
locations = [loc for loc in location_stats.keys() if loc != "other"]

# Nice display labels (title case)
display_locations = [loc.title() for loc in locations]
loc_map = dict(zip(display_locations, locations))  # display → internal

# -------------------------------------------------------
# INPUTS
# -------------------------------------------------------
sqft = st.number_input("Total Area (sqft)", min_value=200.0, step=50.0)
bath = st.number_input("Number of Bathrooms", min_value=1.0, step=1.0)
bhk = st.number_input("Number of BHK", min_value=1.0, step=1.0)

selected_display_loc = st.selectbox("Location", display_locations)
selected_loc_internal = loc_map[selected_display_loc]

# -------------------------------------------------------
# PREDICT
# -------------------------------------------------------
if st.button("Predict"):
    payload = {
        "total_sqft": sqft,
        "bath": bath,
        "bhk": bhk,
        "location": selected_loc_internal  # send internal key; API cleans anyway
    }

    try:
        res = requests.post(
    "https://bengaluru-house-price-prediction-ml.onrender.com/predict",
    json=data,
    timeout=30
)



        if res.status_code == 200:
            data = res.json()
            price = data["predicted_price_lakhs"]
            loc_used = data["location_used"].title()

            st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")
            st.caption(f"Location used in model: {loc_used}")

        else:
            st.error(f"API Error: {res.status_code}")

    except Exception as e:
        st.error(f"Connection Error: {e}")
