## 🏠 Bengaluru House Price Prediction — ML Web App

A production-ready machine learning web application that predicts residential property prices in Bengaluru based on square footage, bathrooms, BHK, and location.

**Users can input:**

Total Square Feet

Number of Bathrooms

Number of BHK

Location

and receive an estimated price in Lakhs (₹).

## 🚀 Tech Stack
✅ Machine Learning

RandomForestRegressor

Scikit-learn

Feature Engineering & Preprocessing

✅ Backend

FastAPI

Uvicorn

✅ Frontend

Streamlit

✅ Deployment

Render (API hosting)

Streamlit Cloud / HuggingFace Spaces (UI hosting)

## 📂 Project Structure
```
Realestate_Price_Prediction/
│
├── api/
│   └── app.py
│
├── ui/
│   └── app.py
│
├── models/
│   ├── best_model.pkl          # excluded from repo (>100MB)
│   ├── scaler.pkl
│   └── model_columns.json
│
├── Notebook/
│   └── training.ipynb
│
├── data/                       # excluded from repo
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 Model Overview
✅ Data Processing

Cleaned inconsistent sqft formats

Extracted BHK from size text

Normalized & grouped rare locations

Removed outliers

✅ Feature Engineering

sqft_per_bhk

bath_per_bhk

One-hot encoded locations

## 📊 Performance

Train R² Score: ~0.82

Test R² Score: ~0.65

✅ No data leakage
✅ Generalizes well
✅ Reacts strongly to location differences

## ⚡ Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start FastAPI backend
uvicorn api.app:app --reload


Swagger docs →
http://127.0.0.1:8000/docs

3️⃣ Start Streamlit UI
cd ui
streamlit run app.py

🌍 API Usage
Endpoint
POST /predict

Request Example
{
  "total_sqft": 1200,
  "bath": 2,
  "bhk": 3,
  "location": "whitefield"
}

Response Example
{
  "predicted_price_lakhs": 85.42
}

## 📦 Requirements

All dependencies listed in:

requirements.txt

## 📍 Dataset Source

Bengaluru House Price Data
Originally available on Kaggle:
https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

⚠️ Dataset NOT included due to licensing & size restrictions.

## 📦 Deployment Strategy

✅ Deploy FastAPI — Render / Railway / Deta Space
✅ Deploy Streamlit UI — Streamlit Cloud / Render
✅ Update frontend API URL before deploying

## ⚠️ Important Notes

best_model.pkl excluded — >100MB, beyond GitHub limit

scaler.pkl & model_columns.json must remain for predictions

Retraining requires downloading dataset separately

## ✅ Future Enhancements

Feature importance visualization

Add XGBoost / CatBoost comparison

Docker containerization

CI/CD pipeline

## 🤝 Contributions

PRs, issues, improvements — welcome!

## 🧑‍💻 Author

Sravani
Machine Learning & Software Developer
GitHub: https://github.com/Sravani75-hub

## 📜 License

For educational, learning & portfolio purposes.