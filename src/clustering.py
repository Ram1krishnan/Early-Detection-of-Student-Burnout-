import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.cluster import KMeans

os.makedirs("../visualizations/clustering_plots", exist_ok=True)

df = pd.read_csv("../data/student_burnout_dataset.csv")

features = [
    "engagement_score",
    "stress_level",
    "activity_irregularity_score",
    "burnout_velocity"
]

X = df[features]

kmeans = KMeans(n_clusters=3)
df["cluster"] = kmeans.fit_predict(X)

plt.figure()
sns.scatterplot(
    x=df["engagement_score"],
    y=df["stress_level"],
    hue=df["cluster"]
)

plt.title("Behavior Clusters")
plt.savefig("../visualizations/clustering_plots/behavior_clusters.png")
plt.close()

print("Clustering complete")