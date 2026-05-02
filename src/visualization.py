import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

df=pd.read_csv("data/spotify_global_trends.csv")

os.makedirs("outputs/plots", exist_ok=True)

plt.figure(figsize=(8, 5))
df["trend"].value_counts().plot(kind="bar", color=["tomato", "skyblue"])
plt.title("🎵 Rising vs Falling Trends")
plt.xlabel("Trend")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/plots/plot_1_trend_counts.png")
plt.close()
print("✅ Plot 1 saved!")

plt.figure(figsize=(8, 5))
plt.hist(df["streams"], bins=20, color="mediumpurple", edgecolor="black")
plt.title("🎵 Distribution of Streams")
plt.xlabel("Streams")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/plots/plot_2_streams_histogram.png")
plt.close()
print("✅ Plot 2 saved!")

plt.figure(figsize=(8, 5))
colors = df["trend"].map({"Rising": "green", "Falling": "red"})
plt.scatter(df["streams"], df["viral_score"], c=colors, alpha=0.6)
plt.title("🎵 Streams vs Viral Score")
plt.xlabel("Streams")
plt.ylabel("Viral Score")
plt.tight_layout()
plt.savefig("outputs/plots/plot_3_streams_vs_viral.png")
plt.close()
print("✅ Plot 3 saved!")

fig1 = px.bar(df, x="genre", color="trend",
              title="🎵 Trends by Genre")
fig1.write_html("outputs/plots/plot_4_genre_trends.html")
print("✅ Plotly Plot 1 saved!")

fig2 = px.scatter(df, x="streams", y="viral_score",
                  color="trend", hover_data=["track_name", "artist_name"],
                  title="🎵 Streams vs Viral Score (Interactive)")
fig2.write_html("outputs/plots/plot_5_interactive_scatter.html")
print("✅ Plotly Plot 2 saved!")