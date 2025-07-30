import streamlit as st
import numpy as np
from joblib import load

# Load the trained and compressed model
model = load('aqi_model_compressed.pkl')

# Function to categorize AQI value
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good 🟢"
    elif aqi <= 100:
        return "Satisfactory 🟢"
    elif aqi <= 200:
        return "Moderate 🟡"
    elif aqi <= 300:
        return "Poor 🟠"
    elif aqi <= 400:
        return "Very Poor 🔴"
    else:
        return "Severe 🟣"

# Streamlit App Title
st.title("🌫️ Air Quality Index (AQI) Predictor")
st.markdown("""
Enter pollutant concentrations to predict the **Air Quality Index (AQI)**  
and see the corresponding air quality category.
""")

st.subheader("📥 Input: Pollutant Concentrations")

# Input fields with explanations
pm10 = st.number_input(
    "PM10 (Particulate Matter ≤10μm)",
    min_value=0.0,
    value=100.0,
    help="Measured in μg/m³. High levels affect lungs and breathing."
)

no = st.number_input(
    "NO (Nitric Oxide)",
    min_value=0.0,
    value=40.0,
    help="Measured in μg/m³. Formed from combustion processes."
)

no2 = st.number_input(
    "NO₂ (Nitrogen Dioxide)",
    min_value=0.0,
    value=50.0,
    help="Measured in μg/m³. Can irritate airways and cause asthma."
)

nox = st.number_input(
    "NOₓ (Nitrogen Oxides)",
    min_value=0.0,
    value=80.0,
    help="Measured in μg/m³. Sum of NO and NO₂; impacts lungs."
)

nh3 = st.number_input(
    "NH₃ (Ammonia)",
    min_value=0.0,
    value=30.0,
    help="Measured in μg/m³. Comes from fertilizers and industry."
)

co = st.number_input(
    "CO (Carbon Monoxide)",
    min_value=0.0,
    value=1.5,
    help="Measured in mg/m³. A toxic gas from vehicles and burning fuel."
)

so2 = st.number_input(
    "SO₂ (Sulfur Dioxide)",
    min_value=0.0,
    value=25.0,
    help="Measured in μg/m³. Produced by burning coal and oil."
)

o3 = st.number_input(
    "O₃ (Ozone)",
    min_value=0.0,
    value=60.0,
    help="Measured in μg/m³. A key component of smog."
)

# Predict button
if st.button("🎯 Predict AQI"):
    # Prepare input array
    features = np.array([[pm10, no, no2, nox, nh3, co, so2, o3]])
    
    # Predict AQI
    prediction = model.predict(features)
    aqi_value = prediction[0]
    category = get_aqi_category(aqi_value)

    # Display results
    st.success(f"🌍 **Predicted AQI**: {aqi_value:.2f}")
    st.info(f"📊 **Air Quality Category**: {category}")
