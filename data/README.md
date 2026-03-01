# 📊 Student Burnout Behavioral Dataset Documentation

## Dataset Type: Synthetic

The dataset used in this project is synthetic.

Real student behavioural datasets containing LMS activity, attendance records, sentiment feedback, and burnout labels are not publicly available due to privacy, ethical, and institutional confidentiality restrictions. Therefore, synthetic data was generated to simulate realistic student behavioural patterns.

---

## Why No Real Behavioural Dataset Was Used

Real behavioural datasets from universities are protected under privacy regulations such as:

- FERPA (Family Educational Rights and Privacy Act)
- Institutional data protection policies
- Ethical research restrictions

Access to such datasets requires special institutional permissions and ethical review board approvals.

To overcome this limitation while still enabling behavioural modelling, a synthetic dataset was created based on:

- Academic behavioural research
- Observed student engagement patterns
- Realistic behavioural assumptions

This approach ensures privacy while preserving analytical realism.

---

## Dataset Generation Methodology

The dataset was generated using probabilistic modelling and behavioural rule-based logic.

Total Records: **2000 students**

The dataset size ensures:

- Sufficient variability
- Robust machine learning training
- Computational efficiency

---

## Distributions Used

The following statistical distributions were used to simulate realistic behavioural variation:

- **Login frequency:** Uniform distribution (0–7 logins per week)
- **Attendance percentage:** Uniform distribution (40–100%)
- **Assignment delay:** Uniform distribution (0–15 days)
- **Study hours:** Uniform distribution (0.5–6 hours per day)
- **Sentiment score:** Normal distribution (mean = 0, std = 0.5, clipped between -1 and 1)
- **Sleep hours:** Normal distribution (mean = 6.5 hours, std = 1.5 hours)
- **Stress level:** Discrete uniform distribution (1–10 scale)
- **Activity irregularity score:** Uniform distribution (0–1)

These distributions simulate diverse student behavioural profiles.

---

## Behavioural Modelling Assumptions

The following behavioural rules were embedded into the dataset:

- Lower attendance increases burnout risk
- Higher assignment delays increase burnout risk
- Lower LMS login frequency indicates disengagement
- Negative sentiment indicates emotional burnout risk
- High stress and low sleep increase burnout probability
- Engagement score is derived from weighted behavioural indicators
- Burnout risk score is calculated using weighted behavioural factors
- Dropout probability is derived from burnout risk score with stochastic noise
- Behavioural triggers are automatically identified based on threshold rules
- Burnout velocity represents risk progression intensity

These assumptions simulate realistic burnout progression patterns.

---

## Feature Description

| Feature | Description |
|----------|------------|
| student_id | Unique identifier for each student |
| login_frequency_per_week | Number of LMS logins per week |
| attendance_percentage | Student attendance percentage |
| assignment_delay_days | Average assignment submission delay |
| study_hours_per_day | Average daily study hours |
| sentiment_score | Sentiment score from feedback (-1 to 1) |
| sleep_hours_per_day | Average sleep duration |
| stress_level | Stress level score (1–10) |
| activity_trend | Behaviour trend (Improving, Stable, Declining) |
| social_interaction_score | Peer interaction level |
| extracurricular_participation | Participation in extracurricular activities |
| activity_irregularity_score | Behavioural irregularity metric |
| engagement_score | Derived student engagement score |
| burnout_velocity | Rate of burnout progression |
| burnout_risk_score | Burnout risk score (0–100) |
| burnout_risk_level | Burnout classification (Low, Medium, High) |
| dropout_probability | Probability of student dropout |
| behavioural_triggers | Factors contributing to burnout |
| recommended_intervention | Suggested intervention strategy |

---

## How the Dataset Supports Behavioural Analytics

This dataset enables:

- Behaviour pattern analysis
- Risk modelling
- Engagement analysis
- Emotional burnout detection
- Behavioural segmentation
- Intervention simulation
- Early warning system modelling

It is specifically engineered for behavioural analytics research and predictive modelling.

---

## Limitations

- Synthetic data may not capture all real-world behavioural complexities
- Longitudinal real-time behavioural shifts are simulated
- External socioeconomic factors are not included

Future work may integrate real institutional data (subject to approval).

---

## File Location

Dataset file:


data/student_burnout_dataset.csv


---

## Conclusion

This synthetic dataset provides a realistic, privacy-preserving foundation for:

- Behavioural analytics
- Burnout prediction
- Explainable AI modelling
- Intervention simulation
- Early warning systems

It is specifically structured to support behavioral intelligence research and decision-support systems.