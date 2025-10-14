from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the model
MODEL_PATH = os.path.join("models", "sales_predictor.joblib")
model_data = joblib.load(MODEL_PATH)
model = model_data["model"]
FEATURES = model_data["features"]

@app.route("/")
def home():
    return render_template("index.html", features=FEATURES)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get numeric input from form
        data = {feature: float(request.form[feature]) for feature in FEATURES}
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({"prediction": round(float(prediction), 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
