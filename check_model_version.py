import joblib
import sklearn
import numpy

print("Current sklearn version:", sklearn.__version__)
print("Current numpy version:", numpy.__version__)

model = joblib.load("flight_price_model.pkl")

print("\nModel loaded successfully!")
print("Model type:", type(model))