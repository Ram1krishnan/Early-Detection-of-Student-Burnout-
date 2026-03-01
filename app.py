import streamlit as st
import pandas as pd
import joblib
import shap
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ================================
# PAGE CONFIG
# ================================

st.set_page_config(
    page_title="Student Behavioral Analytics System",
    layout="wide"
)

# ================================
# LOAD DATA AND MODEL
# ================================

df = pd.read_csv("../data/student_burnout_dataset.csv")

model = joblib.load("../models/burnout_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

FEATURE_COLUMNS = [
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

st.title("🎓 Student Behavioral Analytics and Burnout Prediction System")

st.markdown("""
This system uses **Behavioral Analytics, Machine Learning, and Explainable AI**
to identify students at risk of burnout and recommend interventions.
""")

# ================================
# TABS
# ================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overall Behavioral Analytics",
    "👤 Individual Student Analysis",
    "📈 Student Risk Timeline",
    "🧠 Explainable AI",
    "📖 Behavioral Insights"
])

# =====================================================
# TAB 1: OVERALL ANALYTICS
# =====================================================

with tab1:

    st.header("Overall Behavioral Analytics Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", len(df))
    col2.metric("High Risk Students", len(df[df["burnout_risk_level"] == "High"]))
    col3.metric("Average Engagement", round(df["engagement_score"].mean(), 2))

    # Risk Distribution
    st.subheader("Burnout Risk Distribution")

    fig = px.histogram(
        df,
        x="burnout_risk_level",
        color="burnout_risk_level",
        title="Distribution of Burnout Risk Levels"
    )

    st.plotly_chart(fig, width="stretch")

    st.info("""
Interpretation:
Most students fall into the Medium risk category. High risk students require immediate intervention.
""")

    # Engagement vs Risk
    st.subheader("Engagement vs Burnout Risk")

    fig2 = px.box(
        df,
        x="burnout_risk_level",
        y="engagement_score",
        color="burnout_risk_level"
    )

    st.plotly_chart(fig2, width="stretch")

    st.info("""
Interpretation:
Students with lower engagement scores show significantly higher burnout risk.
""")

    # Stress vs Engagement
    st.subheader("Stress vs Engagement")

    fig3 = px.scatter(
        df,
        x="engagement_score",
        y="stress_level",
        color="burnout_risk_level"
    )

    st.plotly_chart(fig3, width="stretch")

    st.info("""
Interpretation:
High stress combined with low engagement strongly indicates burnout risk.
""")


# =====================================================
# TAB 2: INDIVIDUAL STUDENT ANALYSIS
# =====================================================

with tab2:

    st.header("Individual Student Behavioral Analysis")

    student_id = st.selectbox("Select Student ID", df["student_id"])

    student = df[df["student_id"] == student_id]

    col1, col2, col3 = st.columns(3)

    col1.metric("Attendance", f"{float(student['attendance_percentage'].iloc[0]):.1f}%")
    col2.metric("Engagement", float(student["engagement_score"].iloc[0]))
    col3.metric("Stress", float(student["stress_level"].iloc[0]))

    col4, col5, col6 = st.columns(3)

    col4.metric("Sleep Hours", float(student["sleep_hours_per_day"].iloc[0]))
    col5.metric("Burnout Velocity", float(student["burnout_velocity"].iloc[0]))
    col6.metric("Irregularity Score", float(student["activity_irregularity_score"].iloc[0]))

    # Prediction
    X = student[FEATURE_COLUMNS]
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]
    confidence = model.predict_proba(X_scaled).max()

    st.subheader("Prediction Result")

    st.metric("Burnout Risk Level", prediction)
    st.metric("Prediction Confidence", f"{confidence*100:.2f}%")

    st.success(student["recommended_intervention"].iloc[0])

    st.info("""
Interpretation:
This prediction is based on behavioral patterns including engagement, stress, and attendance.
""")


# =====================================================
# TAB 3: STUDENT BEHAVIORAL RISK TIMELINE
# =====================================================

with tab3:

    st.header("Behavioral Risk Timeline Simulation")

    student_id = st.selectbox("Select Student for Timeline", df["student_id"], key="timeline")

    student = df[df["student_id"] == student_id]

    # Simulate timeline
    timeline = pd.DataFrame()

    timeline["Week"] = ["Week 1", "Week 2", "Week 3", "Week 4"]

    base_risk = float(student["burnout_velocity"].iloc[0]) * 100

    timeline["Risk Score"] = [
        base_risk * 0.6,
        base_risk * 0.75,
        base_risk * 0.9,
        base_risk * 1.0
    ]

    fig = px.line(
        timeline,
        x="Week",
        y="Risk Score",
        markers=True,
        title="Behavioral Risk Progression"
    )

    st.plotly_chart(fig, width="stretch")

    st.info("""
Interpretation:
The timeline shows how behavioral patterns may increase burnout risk over time.
Early intervention can prevent further deterioration.
""")


# =====================================================
# TAB 4: SHAP EXPLAINABILITY
# =====================================================

with tab4:

    st.header("Explainable AI - Feature Importance")

    X = df[FEATURE_COLUMNS]
    X_scaled = scaler.transform(X)

    # SHAP explainer
    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_scaled)

    # Handle multiclass correctly
    if isinstance(shap_values, list):

        # shap_values is list of arrays (one per class)
        # shape: (classes, samples, features)

        shap_values_array = np.array(shap_values)

        # Take mean across classes and samples
        importance = np.mean(np.abs(shap_values_array), axis=(0,1))

    elif len(shap_values.shape) == 3:

        # 3D array case: (samples, features, classes)
        # Take mean across samples and classes
        importance = np.mean(np.abs(shap_values), axis=(0,2))

    else:

        # Single class case
        importance = np.mean(np.abs(shap_values), axis=0)


    # Create dataframe safely
    shap_df = pd.DataFrame({
        "Feature": FEATURE_COLUMNS,
        "Importance": importance.flatten()
    })

    shap_df = shap_df.sort_values("Importance", ascending=False)

    fig = px.bar(
        shap_df,
        x="Importance",
        y="Feature",
        orientation="h"
    )

    st.plotly_chart(fig, width="stretch")

    st.info("""
Interpretation:
Engagement, stress, and attendance are the most influential behavioral predictors of burnout.
""")


# =====================================================
# TAB 5: BEHAVIORAL INSIGHTS
# =====================================================

with tab5:

    st.header("Behavioral Insights and Interpretation")

    insights = open("../outputs/behavioral_insights.txt").read()

    st.text(insights)

    st.success("""
Key Behavioral Findings:

• Low engagement strongly correlates with burnout risk.

• High stress levels increase burnout probability.

• Attendance is a critical indicator of student well-being.

• Behavioral analytics enables early burnout detection.
""")

    st.info("""
System Impact:

This system enables proactive intervention to reduce student burnout and dropout rates.
""")