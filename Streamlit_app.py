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

# Streamlit App Title and Description
st.title("🌫️ Air Quality Index (AQI) Predictor")
st.markdown("""
Predict the **Air Quality Index (AQI)** by entering pollutant concentrations  
or by selecting a predefined sample scenario.
""")

# Sample pollutant profiles (in the same order as input fields)
sample_inputs = {
    "Good 🟢": [40, 8, 10, 15, 5, 0.5, 5, 30],
    "Moderate 🟡": [120, 30, 50, 80, 20, 1.5, 25, 60],
    "Poor 🟠": [180, 70, 90, 130, 40, 2.5, 50, 90],
    "Severe 🟣": [280, 100, 150, 200, 70, 3.5, 80, 130],
}

# Dropdown for input selection
selected_profile = st.selectbox(
    "🧪 Choose a sample scenario or enter values manually",
    options=["Manual Input"] + list(sample_inputs.keys())
)

# If user selects a predefined profile
if selected_profile != "Manual Input":
    values = sample_inputs[selected_profile]
    pm10, no, no2, nox, nh3, co, so2, o3 = values

    # Display selected values as read-only
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
    # Manual input with help and defaults
    st.subheader("📥 Enter Pollutant Concentrations Manually")
    pm10 = st.number_input("PM10 (Particulate Matter ≤10μm)", min_value=0.0, help="μg/m³")
    no = st.number_input("NO (Nitric Oxide)", min_value=0.0, help="μg/m³")
    no2 = st.number_input("NO₂ (Nitrogen Dioxide)", min_value=0.0, help="μg/m³")
    nox = st.number_input("NOₓ (Nitrogen Oxides)", min_value=0.0, help="μg/m³")
    nh3 = st.number_input("NH₃ (Ammonia)", min_value=0.0, help="μg/m³")
    co = st.number_input("CO (Carbon Monoxide)", min_value=0.0, help="mg/m³")
    so2 = st.number_input("SO₂ (Sulfur Dioxide)", min_value=0.0, help="μg/m³")
    o3 = st.number_input("O₃ (Ozone)", min_value=0.0, help="μg/m³")

# Prediction button
if st.button("🎯 Predict AQI"):
    features = np.array([[pm10, no, no2, nox, nh3, co, so2, o3]])
    prediction = model.predict(features)
    aqi_value = prediction[0]
    category = get_aqi_category(aqi_value)

    # Output results
    st.success(f"🌍 **Predicted AQI**: {aqi_value:.2f}")
    st.info(f"📊 **Air Quality Category**: {category}")
