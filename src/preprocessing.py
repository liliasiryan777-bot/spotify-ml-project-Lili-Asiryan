import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/spotify_global_trends.csv")

df = df.drop(columns=["track_name", "artist_name"])
print("🗑️ Removed unnecessary columns")

df = df.dropna()
print(f"✅ Missing values handled, shape: {df.shape}")

le = LabelEncoder()
text_columns = ["genre", "country", "popularity_category", "longevity"]
for col in text_columns:
    df[col] = le.fit_transform(df[col])
print("🔢 Text columns encoded")

df["trend"] = le.fit_transform(df["trend"])
print("🎯 Target column encoded (0=Falling, 1=Rising)")

X = df.drop(columns=["trend"])
y = df["trend"]
print(f"📐 Features shape: {X.shape}, Target shape: {y.shape}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("⚖️ Features scaled")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
print(f"✂️ Train size: {len(X_train)}, Test size: {len(X_test)}")

print(f"🎯 Unique target values: {np.unique(y)}")

print(f"📊 Feature means: {np.mean(X_scaled, axis=0).round(2)}")

np.save("data/X_train.npy", X_train)
np.save("data/X_test.npy", X_test)
np.save("data/y_train.npy", y_train)
np.save("data/y_test.npy", y_test)
print("💾 Preprocessed data saved!")