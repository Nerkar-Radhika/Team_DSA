# Team_DSA
Problem Statement - WaterWatch : AI powered ward-level water scarcity foecasting system for Indian muncipal cities , predicts shortage risks, surfcae root causes, and recommends tanker pre-allocation.

# 🚰 WaterWatch

> AI-Powered Ward-Level Water Scarcity Forecasting System for Indian Municipal Cities

![Python](https://img.shields.io/badge/Python-3.10-blue)
![XGBoost](https://img.shields.io/badge/ML-XGBoost-red)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-orange)


---

## 📌 Problem Statement

Municipal water supply in Indian cities is 
irregular, uneven, and untracked at ward level.
No AI-based early warning system exists for 
ward-level water shortage prediction.

- ❌ 600 million Indians face high water stress
- ❌ Tankers deployed reactively after crisis hits
- ❌ No ward-level forecasting system exists

---

## 💡 Our Solution

WaterWatch predicts which wards will face 
water shortage in the NEXT 7 DAYS using 
Machine Learning — before the crisis happens.

✅ Ward-level scarcity risk prediction  
✅ 7-day rolling trend features  
✅ Overfitting-controlled XGBoost model  
✅ Root cause indicators surfaced automatically  
✅ Tanker pre-allocation recommendation  
✅ Interactive Streamlit dashboard  

---

## 🏙️ Pilot City — Nagpur (NMC)

Built for Nagpur Municipal Corporation (NMC) 
wards as pilot. Fully scalable to any 
Indian city.

Wards covered:
- Dharampeth | Lakadganj | Ashi Nagar
- Mangalwari | Nehru Nagar | Gandhibagh
- Satranjipura | Hanuman Nagar | Wathoda
- Kalamna | Beltarodi | Nandanvan

---

## 🛠️ Tech Stack

| Component      | Technology         |
|----------------|--------------------|
| Language       | Python 3.10        |
| ML Model       | XGBoost Classifier |
| Dashboard      | Streamlit          |
| Data           | Pandas, NumPy      |
| Visualization  | Plotly, Seaborn    |
| Version Control| GitHub             |

---

## 📁 Project Structure
```
Team_DSA/
│
├── Hackathon_team_DSA (1).ipynb    # ML model notebook
├── app.py                           # Streamlit dashboard
├── feature_importance.csv           # Root cause indicators
├── ward_risk_predictions.csv        # Model output
├── waterwatch_dataset .csv          # Synthetic dataset
└── README.md                        # Project documentation
```

---

## 📊 Dataset Features

| Feature | Description |
|---|---|
| supply_hours | Daily water supply in hours |
| pressure | Water pressure in kPa |
| demand | Daily demand in MLD |
| supply | Actual supply in MLD |
| complaints | Complaints per 1000 people |
| pipe_breaks | Pipe break incidents |
| supply_hours_7day_avg | 7-day rolling avg of supply |
| complaints_7day_avg | 7-day rolling avg of complaints |
| pipe_breaks_7day_avg | 7-day rolling avg of pipe breaks |
| scarcity | Target label (0 = No, 1 = Yes) |

---

## 🤖 ML Model

- **Algorithm:** XGBoost Classifier
- **Dataset:** 1080 rows | 12 wards | 90 days
- **Target:** Scarcity prediction (Yes/No)

### Overfitting Prevention:
```python
XGBClassifier(
    n_estimators=200,
    max_depth=3,        # shallow trees
    learning_rate=0.05, # slow learning
    subsample=0.8,      # row sampling
    colsample_bytree=0.8, # feature sampling
    reg_alpha=0.5,      # L1 regularization
    reg_lambda=1        # L2 regularization
)
```

### Model Output per Ward:
```
Risk Score  → 0 to 100 (clipped 10-90)
Risk Level  → 🔴 High | 🟡 Medium | 🟢 Low
Tankers     → Pre-allocation count
```

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Nerkar-Radhika/Team_DSA.git
cd Team_DSA
```

### 2. Install dependencies
```bash
pip install pandas numpy xgboost scikit-learn 
           streamlit plotly seaborn matplotlib
```

### 3. Run dataset generation
```bash
cd data
jupyter notebook waterwatch_dataset.ipynb
```

### 4. Run ML model
```bash
cd model
jupyter notebook waterwatch_model.ipynb
```

### 5. Run dashboard
```bash
cd dashboard
streamlit run app.py
```

---

## 📈 Sample Output
```
📊 MODEL ACCURACY
Train Accuracy : 0.91
Test Accuracy  : 0.88
✅ Model generalization looks good

Ward-wise Risk Prediction:

Ward Name      Zone     Risk Score  Risk Level
Satranjipura   North    78.3        🔴 High
Mangalwari     Central  71.2        🔴 High
Dharampeth     West     65.4        🟡 Medium
Kalamna        North    38.2        🟢 Low

🚛 Tanker Pre-Allocation Plan generated!
✅ ward_risk_predictions.csv saved
✅ feature_importance.csv saved
```

---

## 🔍 Root Cause Indicators

Top features driving scarcity prediction:
- 📉 Supply hours drop (7-day trend)
- 📢 Rising complaint rate
- 🔧 Pipe break frequency
- 💧 Demand-supply gap
- ⚡ Low water pressure

---

## 🌍 Impact

- 🏙️ Covers 12 wards, 1.5M+ population
- 🚰 Predicts shortage 7 days in advance
- 🚛 Optimises tanker deployment
- 💰 Saves municipal resources
- 📊 Enables data-driven governance
- 🔁 Scalable to any Indian city

---

## 👥 Team DSA

| Member | Role |
|---|---|
| Radhika Nerkar | ML Model (XGBoost) |
| Prathamesh | Dataset Generation |
| Chaitanya | Presentation & PPT |
| Gunjan | Streamlit Dashboard |

---

## 🏆 Built At

> Hackathon 2026  
> Problem Statement: WaterWatch  
> Track: Data Science & AI  

---

## 📞 Contact

GitHub: [@Nerkar-Radhika](https://github.com/Nerkar-Radhika)  
Repo: [Team_DSA](https://github.com/Nerkar-Radhika/Team_DSA)

---

*🚰 WaterWatch | Predicting Water Scarcity. Preventing Water Crisis.*
```

---

## How to add to GitHub:

### Step 1
```
https://github.com/Nerkar-Radhika/Team_DSA
```

### Step 2
Click **"Add file"** → **"Create new file"**

### Step 3
Name it exactly:
```
README.md
