import streamlit as st
import os
import pandas as pd
import joblib

# Set page title and layout
st.set_page_config(page_title="Rainfall Prediction", layout="wide")

# File paths
dataset_path = r"D:\ML_PROJECT\pictures_model\weatherAUS.csv"
model_path = r"D:\ML_PROJECT\pictures_model\random_forest_model.pkl"
image_path = r"D:\ML_PROJECT\pictures_model\rainfall-removebg-preview.png"

# --- Session State for Page Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "Home"  # Default page

# Function to change page
def set_page(page_name):
    st.session_state.page = page_name

# Sidebar: Show logo if available
if os.path.exists(image_path):
    st.sidebar.image(image_path, width=200)
else:
    st.sidebar.warning("⚠️ Image not found!")

# Sidebar: Equal-Sized Buttons
button_style = """
    <style>
        div.stButton > button {
            width: 100%;  /* Equal button width */
            height: 50px; /* Equal button height */
            margin-bottom: 10px; /* Space between buttons */
        }
    </style>
"""
st.sidebar.markdown(button_style, unsafe_allow_html=True)

# Sidebar Navigation Buttons
if st.sidebar.button("📂 Dataset"):
    set_page("Dataset")
if st.sidebar.button("📊 Dataframe"):
    set_page("Dataframe")
if st.sidebar.button("📈 Visualization"):
    set_page("Visualization")
if st.sidebar.button("🤖 Prediction"):
    set_page("Prediction")

# --- Page Content Based on Selection ---
if st.session_state.page == "Home":
    st.title("Rainfall Prediction Project 🌧️")
    st.write(
        """
        This project predicts rainfall using machine learning techniques. 
        We use a dataset containing weather data from different locations in Australia.
        
        **Key Features:**
        - 📂 View and analyze the dataset  
        - 📊 Explore data visualizations  
        - 🤖 Make predictions based on user input  
        """
    )

elif st.session_state.page == "Dataset":
    st.subheader("📂 Dataset View")

    if os.path.exists(dataset_path):
        try:
            df = pd.read_csv(dataset_path, encoding="ISO-8859-1")  # Handle encoding issues

            # Display dataset details
            st.write(f"Dataset Loaded Successfully! Shape: {df.shape}")

            # Display full dataset
            st.dataframe(df)  # Shows the entire dataset

        except Exception as e:
            st.error(f"❌ Error reading dataset: {e}")
    else:
        st.error("⚠️ Dataset file not found!")

elif st.session_state.page == "Dataframe":
    st.subheader("📊 Dataframe View")
    if os.path.exists(dataset_path):
        df = pd.read_csv(dataset_path)
        st.dataframe(df)
    else:
        st.error("⚠️ Dataset file not found!")

elif st.session_state.page == "Visualization":
    st.subheader("📈 Data Visualization")
    st.write("Here, you can view different plots and trends.")

elif st.session_state.page == "Prediction":
    st.subheader("🤖 Make a Prediction")
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        user_input = st.text_input("Enter feature values (comma-separated):")
        if user_input:
            try:
                features = list(map(float, user_input.split(",")))
                prediction = model.predict([features])
                st.success(f"🌦️ Predicted Rainfall: {prediction[0]}")
            except Exception as e:
                st.error(f"Error in prediction: {e}")
    else:
        st.error("⚠️ Model file not found!")