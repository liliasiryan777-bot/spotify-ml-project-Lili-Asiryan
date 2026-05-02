import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score
import os

y_test = np.load("data/y_test.npy")
y_pred = np.load("data/y_pred.npy")

os.makedirs("outputs/results", exist_ok=True)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"✅ Accuracy: {accuracy:.2f}")
print(f"🎯 Precision: {precision:.2f}")
print(f"📊 Recall: {recall:.2f}")
print(f"🔢 Confusion Matrix:\n{cm}")

with open("outputs/results/metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.2f}\n")
    f.write(f"Precision: {precision:.2f}\n")
    f.write(f"Recall: {recall:.2f}\n")
    f.write(f"Confusion Matrix:\n{cm}\n")
print("💾 Metrics saved!")

import pandas as pd
df_results = pd.DataFrame({
    "Real": y_test,
    "Predicted": y_pred
})
df_results.to_csv("outputs/results/predictions.csv", index=False)
print("💾 Predictions CSV saved!")