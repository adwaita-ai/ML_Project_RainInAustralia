import streamlit as st
import pandas as pd

def show():
    st.title("📂 Dataset")
    st.write("This page displays the dataset.")

    # Example dataset loading (update with real dataset)
    df = pd.DataFrame({
        "Location": ["A", "B", "C"],
        "Rainfall (mm)": [120.4, 85.3, 95.0]
    })
    st.dataframe(df)