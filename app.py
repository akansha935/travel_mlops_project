from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model safely
try:
    model = joblib.load("flight_price_model.pkl")
    print("Model loaded successfully")
except Exception as e:
    print("Model loading failed:", e)

@app.route("/")
def home():
    return "Flight Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = pd.DataFrame([{
        "from": data["from"],
        "to": data["to"],
        "flightType": data["flightType"],
        "agency": data["agency"],
        "time": data["time"],
        "distance": data["distance"],
        "Journey_Day": data["Journey_Day"],
        "Journey_Month": data["Journey_Month"]
    }])

    prediction = model.predict(input_data)[0]

    return jsonify({
        "predicted_price": float(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)