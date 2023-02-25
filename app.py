# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 01:38:31 2022

@author: 3460
"""
# In[1] import packages
import streamlit as st
import pandas as pd
from PIL import Image
import joblib

# In[2] webapp
# Title
img = Image.open("cow.png")
st. image(img)

# Input bar 1
height = st.number_input("请输入您的身高（厘米）")

# Input bar 2
weight = st.number_input("请输入您的体重（千克）")

# Dropdown input
eyes = st.selectbox("请选择您的眼睛大小", ("大", "小"))

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[height, weight, eyes]], 
                     columns = ["Height", "Weight", "Eyes"])
    X = X.replace(["大", "小"], [1, 0])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    if prediction == 'Cow':
        st.text(f"您的真是身份是：牛")
    if prediction == 'Horse':
        st.text(f"您的真是身份是：马")