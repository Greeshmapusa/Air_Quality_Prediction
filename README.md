# Air Quality Index (AQI) Predictor

This is a mini machine learning project that predicts the Air Quality Index (AQI) using environmental pollutant data such as PM10, NO, NO2, CO, and more. The project includes a trained Random Forest model and a web interface built with Streamlit.


# Problem Statement

Air pollution is a serious health and environmental issue. The goal of this project is to build a machine learning model that can predict the AQI based on pollutant concentrations. This prediction can help in issuing early warnings and better air quality monitoring.


# Machine Learning Approach

- Model Used: Random Forest Regressor
- Features Used:
  - PM10
  - NO
  - NO2
  - NOx
  - NH3
  - CO
  - SO2
  - O3
- Target Variable: AQI

The trained model is compressed and saved as `aqi_model_compressed.pkl` using `joblib` for smaller size and faster loading.


# Model Performance

Model Evaluation Metrics:
Mean Absolute Error (MAE): 18.66
Root Mean Squared Error (RMSE): 30.47
R² Score: 0.89


