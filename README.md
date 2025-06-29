# Predicting-Liver-Cirrhosis-using-Advanced-Machine-Learning-Techniques
📊liver Cirrhosis Stage Prediction using Machine Learning
This project aims to predict the stage of liver cirrhosis using clinical input parameters and machine learning. A Flask-based web app allows users to input lab results and receive stage predictions in real time.
________________________________________
📽️ Demo
🔊 Watch Demo on YouTube
📊 Dataset on Kaggle
________________________________________
📌 Table of Contents
•	Overview
•	Tech Stack
•	Installation
•	Usage
•	Model Performance
•	License
________________________________________
🧠 Overview
This project uses XGBoost, Flask, and a medical dataset to:
•	Accept 15 clinical input features.
•	Predict liver cirrhosis stage (1 to 4).
•	Provide interpretation messages like:
o	Stage 1: Normal Liver
o	Stage 2: Fatty Liver
o	Stage 3: Liver Fibrosis
o	Stage 4: Liver Cirrhosis
________________________________________
⚙️ Tech Stack
Layer	Technologies
Frontend	HTML, CSS
Backend	Flask (Python)
ML Model	XGBoost
Libraries	Pandas, NumPy, scikit-learn, SMOTE, pickle
________________________________________
🔧 Installation
# Clone the repo
git clone https://github.com/your-username/liver-cirrhosis-predictor.git
cd liver-cirrhosis-predictor

# Optional: Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Then open your browser at: http://127.0.0.1:5000/
________________________________________
🧪 Usage
1.	Fill in the required medical input values on the homepage.
2.	Click Predict.
3.	View the stage and interpretation displayed on the same page.
________________________________________
📈 Model Performance
•	Model: XGBClassifier
•	Accuracy: ~48%
•	SMOTE applied for class balancing
•	Evaluation metrics :
Before SMOTE: [ 15  74 127 113]
After SMOTE:  [127 127 127 127]________________________________________
📜 License
This project is submitted for academic purposes only. Licensing not applied.
