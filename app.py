# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:51:35 2022

@author: 3460
"""

# In[1] import packages
import streamlit as st
import pandas as pd
import joblib

# In[2] webapp
# Title
st.header("动物分类器")

# Input bar 1
height = st.number_input("请输入动物的身高")

# Input bar 2
weight = st.number_input("请输入动物的重量")

# Dropdown input
eyes = st.selectbox("请选择动物眼睛的颜色", ("Blue", "Brown"))

# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    clf = joblib.load("clf.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[height, weight, eyes]], 
                     columns = ["Height", "Weight", "Eyes"])
    X = X.replace(["Brown", "Blue"], [1, 0])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"你描述的动物是 {prediction}")
    
