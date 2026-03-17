 Travel MLOps – Flight & Hotel Price Prediction Platform

 Project Overview

`travel_mlops` is an end-to-end MLOps project for predicting **flight prices** and recommending **hotels**, with automated workflows, APIs, dashboards, and deployment pipelines. It integrates:

- **Apache Airflow** for automated retraining and prediction  
- **Streamlit** for interactive dashboards  
- **Flask API** for programmatic access  
- **Docker & Kubernetes** for containerized deployment  
- **Jenkins CI/CD** for automated build, test, and deployment  


 Objectives

- Predict flight prices automatically and daily.  
- Recommend hotels based on flight routes, prices, and ratings.  
- Provide interactive visual dashboards and programmatic API access.  
- Deploy the application with Docker and Kubernetes.  
- Integrate CI/CD pipelines using Jenkins.  


 Features

- **Automated ML Pipeline (Airflow):**  
  - Retrains flight price models automatically.  
  - Generates predictions and hotel recommendations.  

- **Flight & Hotel Dashboard (Streamlit):**  
  - Filter flights by origin, destination, airline, flight type, and date.  
  - Display recommended hotels with top ratings and proximity to airport.  
  - Interactive charts for price trends, route insights, and cheapest options.  

- **Flask API:**  
  - Endpoint `/predict` for flight price predictions.  
  - Endpoint `/recommend_hotels` to fetch hotel recommendations programmatically.  

- **Deployment:**  
  - Docker image generation for containerized app.  
  - Kubernetes deployment for scalable production use.  
  - CI/CD pipeline with Jenkins for automatic builds and deployments.

- **Extensible:**  
  - Add new airlines, datasets, features, or ML models.  
  - Can integrate additional APIs or services in the pipeline.  



 Tasks Performed

- **Data Collection & Preprocessing:**  
  - Loaded `flights.csv` and `hotels.csv`.  
  - Cleaned data and engineered features for travel date, route, and flight type.  

- **Model Training:**  
  - Trained ML model (`train_flight_model.py`) and saved it for predictions.  

- **Prediction & Recommendation:**  
  - Generated flight price predictions (`predict_flight_price.py`).  
  - Integrated hotel dataset to provide recommendations per flight route.  

- **Workflow Automation (Airflow):**  
  - DAG `predict_flight_price_dag.py` handles training, prediction, and recommendations automatically.  

- **Dashboard Development (Streamlit):**  
  - Filters, summary statistics, price trends, cheapest flight + hotel suggestions.  

- **API Development (Flask):**  
  - `/predict` → returns predicted flight prices.  
  - `/recommend_hotels` → returns hotel recommendations.  

- **Deployment & DevOps:**  
  - Docker image generation (`Dockerfile`).  
  - Kubernetes deployment (YAML manifests) for scalable deployment.  
  - Jenkins pipeline automates build, test, Docker image generation, and deployment.

- **Insights & Analytics:**  
  - Cheapest flight routes and hotel combinations.  
  - Average flight/hotel prices per city.  
  - Price trends and travel insights over time.


 Dataset Information

 Flight Dataset (`flights.csv`)
| Column Name   | Description                                |
|---------------|-------------------------------------------|
| from          | Flight origin city                         |
| to            | Flight destination city                    |
| flightType    | Type of flight (economy, business, etc.)  |
| airline       | Airline name                               |
| date          | Flight date                                |
| price         | Flight price                               |
| distance      | Flight distance                 |
| travelTime    | Flight duration                 |

 Hotel Dataset (`hotels.csv`)
| Column Name   | Description                                |
|---------------|-------------------------------------------|
| hotelName     | Hotel name                                 |
| city          | City where hotel is located                |
| price         | Hotel price per night                      |
| rating        | Hotel rating (1-5)                         |
| distanceToAirport | Distance from airport (km)             |


 Airflow DAG Explanation

The Airflow DAG automates ML workflows:

1. `retrain_model` → trains/updates ML model  
2. `predict_flight_price` → predicts flight prices  
3. `recommend_hotels` → merges predictions with hotel data  

**Task dependency:**  
`retrain_model` → `predict_flight_price` → `recommend_hotels`  

---

Streamlit Dashboard

- Filter flights by origin, destination, airline, flight type, and date.  
- View interactive charts and insights.  
- Display top cheapest flight + hotel combinations.  

---

 Flask API

- **`/predict`** → GET or POST flight data; returns predicted price  
- **`/recommend_hotels`** → GET recommended hotels for flight route  
- Can be used in CI/CD pipelines or external apps for real-time predictions.

Project Structure

travel_mlops/
│
├─ venv/ # Python virtual environment
├─ flights.csv # Flight dataset
├─ hotels.csv # Hotel dataset
├─ flight_dashboard.py # Streamlit dashboard
├─ predict_flight_price.py # Flight prediction script
├─ train_flight_model.py # Flight model training
├─ predict_flight_price_dag.py # Airflow DAG
├─ app.py # Flask API
├─ Dockerfile # Docker image
├─ k8s/ # Kubernetes manifests
│ ├─ deployment.yaml
│ ├─ service.yaml
├─ Jenkinsfile # CI/CD pipeline configuration
├─ requirements.txt # Dependencies
└─ README.md # Project documentation
