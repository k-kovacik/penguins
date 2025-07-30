import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguin Species Prediction ML app")
st.info("This is an end-to-end Machine Learning App")

with st.expander("Data"):
  pass

with st.expander("Data Visualization"):
  pass
  
with st.expander("Input Data"):
  pass

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island', ["Torgersen","Biscoe","Dream"])
  bill_length = st.slider('Bill Length (mm)', 30.0,60.0,45.0)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.0,22.0,17.5)
  flipper_length = st.slider('Flipper Length (mm)', 172.0,231.0,201.0)
  body_mass = st.slider('Body Mass (g)', 2500,6500,4500)
  
  

