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
  bill_length = st.slider('Bill Length (mm)', 30,60,45)

