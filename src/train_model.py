import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

os.makedirs("../models", exist_ok=True)

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
y = df["burnout_risk_level"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))

joblib.dump(model, "../models/burnout_model.pkl")
joblib.dump(scaler, "../models/scaler.pkl")

print("Model saved")