import joblib
import pandas as pd
import logging
import os

def predict_price():
    logging.info("Starting prediction process...")

    model_path = "flight_price_model.pkl"
    
    if not os.path.exists(model_path):
        logging.error(f"Model file not found at {model_path}")
        return None

    logging.info(f"Loading model from {model_path}")
    model = joblib.load(model_path)

    data = {
        "from": ["Delhi"],
        "to": ["Mumbai"],
        "flightType": ["economy"],
        "agency": ["MakeMyTrip"],
        "time": [10],
        "distance": [1400],
        "Journey_Day": [16],
        "Journey_Month": [3],
        "route": ["Delhi_Mumbai"]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)
    predicted_value = float(prediction[0])

    logging.info(f"SUCCESS: Predicted Flight Price: {predicted_value}")

    return predicted_value
