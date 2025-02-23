import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 Visualization")
    st.write("This page contains rainfall visualizations.")

    # Example Plotly Chart
    data = pd.DataFrame({
        "Year": range(2007, 2023),
        "Rainfall": np.random.uniform(50, 300, 16)
    })
    fig = px.line(data, x="Year", y="Rainfall", title="Yearly Rainfall Trends")
    st.plotly_chart(fig)
