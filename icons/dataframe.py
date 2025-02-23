import streamlit as st
import pandas as pd

def show():
    st.title("📝 Data Frame")
    st.write("This page allows you to manipulate data frames.")
    
    # Example DataFrame Operations
    df = pd.DataFrame({
        "Year": range(2010, 2023),
        "Rainfall (mm)": [100 + i * 5 for i in range(13)]
    })
    st.dataframe(df)
