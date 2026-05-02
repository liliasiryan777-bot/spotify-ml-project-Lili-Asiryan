import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pickle

X_train = np.load("data/X_train.npy")
X_test = np.load("data/X_test.npy")
y_train = np.load("data/y_train.npy")

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained successfully!")

y_pred = model.predict(X_test)
print(f"🎯 Predictions made: {len(y_pred)} songs predicted")

with open("data/model.pkl", "wb") as f:
    pickle.dump(model, f)
print("💾 Model saved!")

np.save("data/y_pred.npy", y_pred)
print("💾 Predictions saved!")