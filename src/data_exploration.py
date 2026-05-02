import pandas as pd
import numpy as np

df=pd.read_csv("data/spotify_global_trends.csv")

print("🎵 First 5 rows of Spotify data:")
print(df.head())

print("📋 Dataset Info:")
print(df.info())

print("📊 Summary Statistics:")
print(df.describe())

print("❓ Missing Values:")
print(df.isnull().sum())

print(f"📐 Dataset Shape: Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("🗂️ Columns:")
print(df.columns.tolist())

print("🎯 Target Column (trend) Value Counts:")
print(df["trend"].value_counts())

print("🏆 Top 5 most streamed songs:")
print(df.sort_values("streams", ascending=False).head())

avg = np.mean(df['streams'])
print(f"📈 Average streams: {avg:.0f}")

print(f"⬆️ Max streams: {np.max(df['streams'])}")
print(f"⬇️ Min streams: {np.min(df['streams'])}")