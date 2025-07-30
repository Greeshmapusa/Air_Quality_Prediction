import streamlit as st
import numpy as np
from joblib import load

# Load trained compressed model
model = load('aqi_model_compressed.pkl')

# AQI Category Function
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

# Health Tip Function
def get_health_advice(aqi):
    if aqi <= 50:
        return "Air is clean. Ideal for outdoor activities. 🌳"
    elif aqi <= 100:
        return "Safe to go outside, but sensitive people should take care."
    elif aqi <= 200:
        return "Mild discomfort. People with lungs or heart issues should limit outdoor activity."
    elif aqi <= 300:
        return "Unhealthy. Avoid outdoor exertion. Wear masks if necessary."
    elif aqi <= 400:
        return "Very unhealthy. Stay indoors. Use air purifiers and masks."
    else:
        return "Hazardous! Everyone should stay indoors. Emergency conditions!"

# App Title
st.title("🌫️ Air Quality Index (AQI) Predictor")
st.markdown("Predict AQI using environmental data and get health safety advice based on your air!")

# Sample pollutant profiles
sample_inputs = {
    "Good 🟢": [40, 8, 10, 15, 5, 0.5, 5, 30],
    "Moderate 🟡": [120, 30, 50, 80, 20, 1.5, 25, 60],
    "Poor 🟠": [180, 70, 90, 130, 40, 2.5, 50, 90],
    "Severe 🟣": [280, 100, 150, 200, 70, 3.5, 80, 130],
}

# Select input method
selected_profile = st.selectbox("🧪 Choose a sample scenario or enter values manually", ["Manual Input"] + list(sample_inputs.keys()))

# Get input values
if selected_profile != "Manual Input":
    pm10, no, no2, nox, nh3, co, so2, o3 = sample_inputs[selected_profile]
    st.markdown("#### Auto-filled pollutant values:")
    st.write(f"**PM10**: {pm10} μg/m³")
    st.write(f"**NO**: {no} μg/m³")
    st.write(f"**NO₂**: {no2} μg/m³")
    st.write(f"**NOₓ**: {nox} μg/m³")
    st.write(f"**NH₃**: {nh3} μg/m³")
    st.write(f"**CO**: {co} mg/m³")
    st.write(f"**SO₂**: {so2} μg/m³")
    st.write(f"**O₃**: {o3} μg/m³")
else:
    st.subheader("📥 Manual Pollutant Input")
    pm10 = st.number_input("PM10 (Particulate Matter ≤10μm)", min_value=0.0, help="μg/m³")
    no = st.number_input("NO (Nitric Oxide)", min_value=0.0, help="μg/m³")
    no2 = st.number_input("NO₂ (Nitrogen Dioxide)", min_value=0.0, help="μg/m³")
    nox = st.number_input("NOₓ (Nitrogen Oxides)", min_value=0.0, help="μg/m³")
    nh3 = st.number_input("NH₃ (Ammonia)", min_value=0.0, help="μg/m³")
    co = st.number_input("CO (Carbon Monoxide)", min_value=0.0, help="mg/m³")
    so2 = st.number_input("SO₂ (Sulfur Dioxide)", min_value=0.0, help="μg/m³")
    o3 = st.number_input("O₃ (Ozone)", min_value=0.0, help="μg/m³")

# Prediction
if st.button("🎯 Predict AQI"):
    features = np.array([[pm10, no, no2, nox, nh3, co, so2, o3]])
    prediction = model.predict(features)
    aqi_value = prediction[0]
    category = get_aqi_category(aqi_value)
    advice = get_health_advice(aqi_value)

    st.success(f"🌍 **Predicted AQI:** {aqi_value:.2f}")
    st.info(f"📊 **Air Quality Category:** {category}")
    st.warning(f"💡 **Health Tip:** {advice}")

# Learn More Toggle
with st.expander("📘 Learn: What Do These Pollutants Mean?"):
    st.markdown("""
- **PM10**: Dust particles harmful to lungs  
- **NO / NO₂ / NOₓ**: Gases from vehicles & industry  
- **NH₃**: From fertilizers and sewage  
- **CO**: Toxic gas from cars and combustion  
- **SO₂**: From coal and oil burning  
- **O₃**: Ground-level ozone, part of smog  

**AQI Scale (India):**
- 0–50: Good 🟢  
- 51–100: Satisfactory 🟢  
- 101–200: Moderate 🟡  
- 201–300: Poor 🟠  
- 301–400: Very Poor 🔴  
- 401–500: Severe 🟣
""")
