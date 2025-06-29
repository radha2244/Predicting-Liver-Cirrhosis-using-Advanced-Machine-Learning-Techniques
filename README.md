# 📊 Liver Cirrhosis Stage Prediction using Machine Learning

This project aims to predict the **stage of liver cirrhosis** using clinical input parameters and machine learning. A Flask-based web app allows users to input lab results and receive stage predictions in real time.

---

## 📽️ Demo

-🔊 [Watch Demo on YouTube](https://www.youtube.com/watch?v=pR4RzRVORrE)  
-📊 [Dataset on Kaggle](https://www.kaggle.com/datasets/bhavanipriya222/liver-cirrhosis-prediction)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [License](#license)

---

## 🧠 Overview

This project uses **XGBoost**, **Flask**, and a medical dataset to:

- Accept 15 clinical input features.
- Predict liver cirrhosis stage (1 to 4).
- Provide interpretation messages like:
  - **Stage 1**: Normal Liver
  - **Stage 2**: Fatty Liver
  - **Stage 3**: Liver Fibrosis
  - **Stage 4**: Liver Cirrhosis

---

## ⚙️ Tech Stack

| Layer     | Technologies                               |
|-----------|--------------------------------------------|
| Frontend  | HTML, CSS                                  |
| Backend   | Flask (Python)                             |
| ML Model  | XGBoost                                    |
| Libraries | Pandas, NumPy, scikit-learn, SMOTE, pickle |

---

## 🔧 Installation

1.Clone the repo
```bash
git clone https://github.com/your-username/liver-cirrhosis-predictor.git
cd liver-cirrhosis-predictor
```
2.Optional: Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
3.Install dependencies
```bash
pip install -r requirements.txt
```
3.Run the app
```bash
python app.py
```
## 🧪 Usage

1. Fill in the required medical input values on the homepage.
2. Click **Predict**.
3. View the **stage** and interpretation displayed on the same page.

---

## 📈 Model Performance

- Model: `XGBClassifier`
- Accuracy: ~48%
- SMOTE applied for class balancing
- Evaluation metrics:

```text
Before SMOTE: [ 15  74 127 113]  
After SMOTE:  [127 127 127 127]
```
## 📜 License

This project is submitted for academic purposes only. Licensing not applied.

