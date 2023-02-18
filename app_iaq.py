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

# Input bar 1
volume = st.number_input("Please type the volume of classroom")

# Input bar 2
students = st.number_input("Please type the number of students")

# Input bar 3
occtime = st.number_input("Please type the time of occupancy")

# Input bar 4
openwindow = st.number_input("Please type the opening area of windows")

# Input bar 5
windowtime = st.number_input("Please type the opening time of windows")

# Input bar 6
opendoor = st.number_input("Please type the opening area of door")

# Input bar 7
doortime = st.number_input("Please type the opening time of door")


# If button is pressed
if st.button("Submit"):
    
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
    
