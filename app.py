# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 21:51:35 2022

@author: 3460
"""

# In[1] import packages
import streamlit as st
import pandas as pd
from PIL import Image
import joblib


# In[2] webapp
# Title
img = Image.open("IAQ4EDU.png")
st. image(img)

# In[3] webapp

# Selectbox
selectboxexample = st.selectbox(label="Season", options=("Spring", "Summer", "Winter"))

# Input bar 1
volume = st.number_input(label="Classroom volume", min_value=0.00, format='%.2f')

# Input bar 2
students = st.number_input(label="Number of students", min_value=0, max_value=100, format='%g')

# Input bar 3
occtime = st.number_input(label="Occupancy duration", min_value=0, format='%g')

# Input bar 4
openwindow = st.number_input(label="Opening area of windows", min_value=0.00, format='%.2f')

# Input bar 5
windowtime = st.number_input(label="Window opening duration", min_value=0, format='%g')

# Input bar 6
opendoor = st.number_input(label="Opening area of door", min_value=0.00, format='%.2f')

# Input bar 7
doortime = st.number_input("Door opening duration", min_value=0, format='%g')

# Text area
st.text_area("Do you have any comments?")

# If button is pressed
if st.button("Know your IAQ!"):
    
    # Unpickle classifier
    clf = joblib.load("iaq.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[volume, students, occtime, openwindow, windowtime, opendoor, doortime]], 
                     columns = ["VOLUME", "TOTAL_STUDENTS", "OCCUPIED_TIME", "OPENING_SIZE_WINDOW",
                                "OPENINNG_WINDOW_TIME", "OPENING_SIZE_DOOR", 
                                "OPENING_DOOR_TIME"])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"Your IAQ level is {prediction}")
    
