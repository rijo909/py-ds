import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import time

st.title("Student Performance Index Predictor")
st.subheader("Input the following inputs to predict your student score")

with open(r"C:\xampp816\htdocs\personal-dev\py-ds\ML\regression\linear_regression\student_performance\student_perf_model.pkl", 'rb') as obj2:
    var1=pickle.load(obj2)

banner_url = "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
st.image(banner_url)

hours_studied = st.slider(
    "Hours Studied (per day)",
    min_value=0,
    max_value=24,
    value=7
)
    
previous_scores = st.number_input(
    "Previous Scores (out of 100)", 
    min_value=0, 
    max_value=100, 
    value=40
)
    
extracurricular = st.selectbox(
    "Are you involved in Extracurricular Activities?",
    options=["Yes", "No"]
)
extracurricular = var1['label_encoder'].transform([extracurricular])[0]

sleep_hours = st.slider(
    "Sleep Hours (per night)",
    min_value=0,
    max_value=24,
    value=7
)

sample_papers_practiced = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    max_value=24,
    value=3
)

submitted = st.button("Predict")
if submitted:
    data=[[hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers_practiced]]
    scaled = var1['scaler'].transform(data)
    res = var1['model'].predict(scaled)[0]
    with st.spinner('Processing your performance score...'):
        time.sleep(3)
    if res<0:
        st.success("Performance score : 0")
        st.balloons()
    elif res<0:
        st.success("Performance score : 100")
        st.balloons()
    else:
        st.success(f"Performance score : { round(res, 2) }")
        st.balloons()