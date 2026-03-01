import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualization folders
os.makedirs("../visualizations/behavior_plots", exist_ok=True)
os.makedirs("../outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/student_burnout_dataset.csv")

# Behavioral Insights
insights = []

insights.append("Average engagement by risk level:")
insights.append(str(df.groupby("burnout_risk_level")["engagement_score"].mean()))

insights.append("\nAverage attendance by risk level:")
insights.append(str(df.groupby("burnout_risk_level")["attendance_percentage"].mean()))

insights.append("\nAverage stress level by risk level:")
insights.append(str(df.groupby("burnout_risk_level")["stress_level"].mean()))

# Save insights
with open("../outputs/behavioral_insights.txt", "w") as f:
    for i in insights:
        f.write(i + "\n\n")

# Visualization 1: Risk distribution
plt.figure()
sns.countplot(data=df, x="burnout_risk_level")
plt.title("Burnout Risk Distribution")
plt.savefig("../visualizations/behavior_plots/risk_distribution.png")
plt.close()

# Visualization 2: Engagement vs Risk
plt.figure()
sns.boxplot(data=df, x="burnout_risk_level", y="engagement_score")
plt.title("Engagement vs Risk Level")
plt.savefig("../visualizations/behavior_plots/engagement_vs_risk.png")
plt.close()

print("Behavior analysis complete")