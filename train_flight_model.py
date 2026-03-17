import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor


def train_model():

    print("Starting model training...")

    df = pd.read_csv("flights.csv")

    df["date"] = pd.to_datetime(df["date"])
    df["Journey_Day"] = df["date"].dt.day
    df["Journey_Month"] = df["date"].dt.month

    df["route"] = df["from"] + "_" + df["to"]

    features = [
        "from",
        "to",
        "flightType",
        "agency",
        "time",
        "distance",
        "Journey_Day",
        "Journey_Month",
        "route"
    ]

    X = df[features]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    categorical_cols = ["from", "to", "flightType", "agency", "route"]
    numeric_cols = ["time", "distance", "Journey_Day", "Journey_Month"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", StandardScaler(), numeric_cols)
        ]
    )

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
    ])

    model.fit(X_train, y_train)

    joblib.dump(model, "flight_price_model.pkl")

    print("Model trained successfully")
    print("Model saved as flight_price_model.pkl")


if __name__ == "__main__":
    train_model()