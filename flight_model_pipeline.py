from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import joblib
from train_model import train_flight_model  # your train function

default_args = {
    'owner': 'akansha',
    'depends_on_past': False,
    'start_date': datetime(2026, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def ingest_data():
    df = pd.read_csv("flights.csv")
    df.to_csv("flights_ingested.csv", index=False)
    print("Data ingested")

def retrain_model():
    train_flight_model("flights_ingested.csv")  # your training function
    print("Model retrained and saved as flight_price_model.pkl")

with DAG('flight_model_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='ingest_data', python_callable=ingest_data)
    t2 = PythonOperator(task_id='retrain_model', python_callable=retrain_model)

    t1 >> t2  # t2 runs after t1