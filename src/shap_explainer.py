import pandas as pd
import shap
import joblib
import os
import matplotlib.pyplot as plt

os.makedirs("../visualizations/shap_plots", exist_ok=True)

model = joblib.load("../models/burnout_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

df = pd.read_csv("../data/student_burnout_dataset.csv")

features = [
    "login_frequency_per_week",
    "attendance_percentage",
    "assignment_delay_days",
    "study_hours_per_day",
    "sentiment_score",
    "sleep_hours_per_day",
    "stress_level",
    "activity_irregularity_score",
    "engagement_score",
    "burnout_velocity"
]

X = df[features]
X_scaled = scaler.transform(X)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_scaled)

shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.savefig("../visualizations/shap_plots/shap_summary.png")
plt.close()

print("SHAP explanation saved")