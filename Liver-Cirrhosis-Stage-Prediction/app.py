from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model and scaler
with open("training/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("training/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            features = [
                float(request.form["Age"]),
                int(request.form["Sex"]),
                int(request.form["Ascites"]),
                int(request.form["Hepatomegaly"]),
                int(request.form["Spiders"]),
                float(request.form["Edema"]),
                float(request.form["Bilirubin"]),
                float(request.form["Cholesterol"]),
                float(request.form["Albumin"]),
                float(request.form["Copper"]),
                float(request.form["Alk_Phos"]),
                float(request.form["SGOT"]),
                float(request.form["Tryglicerides"]),
                float(request.form["Platelets"]),
                float(request.form["Prothrombin"])
            ]

            features_scaled = scaler.transform([features])
            stage = int(model.predict(features_scaled)[0]) + 1  # Shift back to Stage 1–4

            stage_meaning = {
                1: "The person has a normal liver.",
                2: "The person has a fatty liver.",
                3: "The person is suffering from liver fibrosis.",
                4: "The person is suffering from liver cirrhosis."
            }

            prediction = f"Predicted Liver Cirrhosis Stage: Stage {stage} {stage_meaning.get(stage, '')}"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
