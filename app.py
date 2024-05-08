import pandas as pd
import streamlit as st

data = pd.read_csv('vehicles_us.csv')

vehicle_types = data["type"].unique()

vehicle_type = st.selectbox(
    "Select vehicle type", 
    vehicle_types
)

data = data.query("type == @vehicle_type")
st.write(data.head())