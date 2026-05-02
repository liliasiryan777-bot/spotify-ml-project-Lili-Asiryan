# 🎵 Spotify Trends ML Project

## 📌 Project Description
This project predicts whether a Spotify song trend is **Rising** or **Falling**
using a Decision Tree Classifier.

## 📂 Dataset
- **Source:** Kaggle - Spotify Global Trending Songs
- **Rows:** 177
- **Columns:** 13
- **Target Column:** `trend` (Rising or Falling)

### Important Columns
| Column | Description |
|---|---|
| `streams` | Number of streams |
| `viral_score` | Viral score of the song |
| `genre` | Music genre |
| `trend` | Rising or Falling (target) |
| `days` | Days on the chart |
| `popularity_category` | Trending or Average |

## 🤖 Machine Learning
- **Task:** Classification
- **Model:** Decision Tree Classifier
- **Train size:** 142 songs
- **Test size:** 36 songs

## 📊 Results
| Metric | Score |
|---|---|
| Accuracy | 1.00 |
| Precision | 1.00 |
| Recall | 1.00 |

## 📁 Project Structure
spotify-ml-project/
├── data/
│   └── spotify_global_trends.csv
├── src/
│   ├── data_exploration.py
│   ├── preprocessing.py
│   ├── visualization.py
│   ├── model.py
│   ├── evaluation.py
│   └── main.py
├── outputs/
│   ├── plots/
│   └── results/
└── requirements.txt

## ▶️ How to Run
```bash
python src/main.py
```

## 📦 Requirements
