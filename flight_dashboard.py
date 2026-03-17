# flight_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Flight Price Dashboard", layout="wide")
st.title("Flight Price Dashboard")

# Load your CSV
csv_path = "flights.csv"  # make sure it's in the same folder or give full path
df = pd.read_csv(csv_path)

st.write("### Raw Flight Data")
st.dataframe(df)

# Filters
origins = df['from'].unique()
destinations = df['to'].unique()
flight_types = df['flightType'].unique()

col1, col2, col3 = st.columns(3)
with col1:
    selected_origin = st.selectbox("Origin", origins)
with col2:
    selected_destination = st.selectbox("Destination", destinations)
with col3:
    selected_type = st.selectbox("Flight Type", flight_types)

filtered_df = df[
    (df['from'] == selected_origin) &
    (df['to'] == selected_destination) &
    (df['flightType'] == selected_type)
]

st.write(f"Flights: {selected_origin} → {selected_destination} ({selected_type})")
st.dataframe(filtered_df)

# Price visualization
if not filtered_df.empty:
    fig = px.line(filtered_df, x="date", y="price", markers=True,
                  title="Flight Prices Over Time")
    st.plotly_chart(fig)
else:
    st.write("No data available for selected filters.")

# Optional: Summary statistics
st.write("### Summary Statistics")
st.write(filtered_df.describe())