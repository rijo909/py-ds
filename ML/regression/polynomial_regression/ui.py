import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import time

st.title("Manufacturing Quality Rating Predictor")
st.subheader("Input the following inputs to predict Manufacturing Quality Rating")

with open(r"C:\xampp816\htdocs\personal-dev\py-ds\ML\regression\polynomial_regression\manufacturing\manufacturing_model.pkl", 'rb') as obj2:
    var1=pickle.load(obj2)

# banner_url = "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
# st.image(banner_url)

temperature = st.slider(
    "Temperature (°C)",
    min_value=100.00,
    max_value=300.00,
    value=200.00
)

pressure = st.slider(
    "Pressure (kPa)",
    min_value=5.00,
    max_value=25.00,
    value=15.00
)
    
material_fusion_metric = st.number_input(
    "Material Fusion Metric", 
    min_value=10000.00, 
    max_value=110000.00, 
    value=50000.00
)

material_transformation_metric = st.number_input(
    "Material Transformation Metric", 
    min_value=3000.00, 
    max_value=27000000.00, 
    value=10000.00
)

submitted = st.button("Predict")
if submitted:
    data=[[temperature, pressure, material_fusion_metric, material_transformation_metric]]
    scaled = var1['scaler'].transform(data)
    poly_transformed = var1['degree'].transform(scaled)
    res = var1['model'].predict(poly_transformed)
    with st.spinner('Processing your performance score...'):
        time.sleep(1)
    st.success(f"Performance score : { res }")
    # if res<0:
    #     st.success("Performance score : 0")
    # elif res<0:
    #     st.success("Performance score : 100")
    # else:
    #     st.success(f"Performance score : { round(res, 2) }")
    # st.balloons()