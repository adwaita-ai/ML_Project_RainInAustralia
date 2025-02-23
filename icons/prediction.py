import streamlit as st
import joblib
import numpy as np

def show():
    st.title("🔮 Prediction")
    st.write("Enter weather parameters to predict rainfall.")

    # Load Model
    model = joblib.load("picture_model/random_forest_model.pkl")

    # Input Fields
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1013.0)
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=50.0, value=5.0)

    # Prediction
    if st.button("Predict Rainfall"):
        input_data = np.array([[temperature, humidity, pressure, wind_speed]])
        prediction = model.predict(input_data)
        st.success(f"Predicted Rainfall: {prediction[0]:.2f} mm")