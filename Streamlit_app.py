import streamlit as st
import numpy as np
from joblib import load

# Load the compressed model
model = load('aqi_model_compressed.pkl')

# App Title
st.title("🌫️ Air Quality Index (AQI) Predictor")
st.markdown("Enter pollutant concentrations to predict the **Air Quality Index (AQI)**.")

# Input fields
pm10 = st.number_input("PM10 (μg/m³)", min_value=0.0)
no = st.number_input("NO (μg/m³)", min_value=0.0)
no2 = st.number_input("NO2 (μg/m³)", min_value=0.0)
nox = st.number_input("NOx (μg/m³)", min_value=0.0)
nh3 = st.number_input("NH3 (μg/m³)", min_value=0.0)
co = st.number_input("CO (mg/m³)", min_value=0.0)
so2 = st.number_input("SO2 (μg/m³)", min_value=0.0)
o3 = st.number_input("O3 (μg/m³)", min_value=0.0)

# Prediction button
if st.button("Predict AQI"):
    # Prepare input as a NumPy array
    features = np.array([[pm10, no, no2, nox, nh3, co, so2, o3]])

    # Make prediction
    prediction = model.predict(features)

    # Display result
    st.success(f"🌍 Predicted AQI: **{prediction[0]:.2f}**")
