🏥 Insurance Claims Fraud ML Pipeline

An end-to-end machine learning pipeline for detecting potential fraud in insurance claims using engineered claim-level aggregation features.  
The project covers data understanding, feature engineering, model training, evaluation, and deployment using FastAPI for real-time fraud risk scoring.

---

🚀 Project Overview

Insurance fraud detection is a critical task in risk management.  
This project builds a fraud risk prediction system by:

- Aggregating inpatient and outpatient claim data
- Engineering domain-specific features
- Training and evaluating ML models
- Deploying the trained model via FastAPI for real-time inference

---

🧠 Machine Learning Pipeline

1️⃣ Data Understanding
- Exploratory Data Analysis (EDA)
- Missing value analysis
- Target distribution analysis
- Feature correlation analysis

2️⃣ Feature Engineering

Created aggregated fraud-indicative features such as:

- `total_inpatient_claims`
- `avg_inpatient_claim_amount`
- `unique_inpatient_patients`
- `total_outpatient_claims`
- `inpatient_ratio`
- `claims_per_patient`
- `avg_claim_amount`
- `log_total_claims`

These features capture abnormal claim patterns and behavioral signals.

3️⃣ Model Training

- Train-Test Split (Stratified)
- Random Forest Classifier
- ROC-AUC evaluation
- Model persistence using Joblib

4️⃣ Deployment
- FastAPI-based REST API
- Real-time fraud risk scoring
- Swagger UI for testing

---

📊 Model Output

The API returns:

![alt text](<WhatsApp Image 2026-02-14 at 12.06.41 PM.jpeg>)

![alt text](<WhatsApp Image 2026-02-14 at 12.07.01 PM.jpeg>)

![alt text](<WhatsApp Image 2026-02-14 at 12.07.01 PM-1.jpeg>)