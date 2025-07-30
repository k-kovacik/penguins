import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

st.title("Penguin Species Prediction ML app")
st.info("This is an end-to-end Machine Learning App")

with st.expander("Data"):
  st.write("**Raw Data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write("Input Variables")
  X_raw = df.drop('species',axis=1)
  X_raw 

  st.write("Target Variable")
  y_raw = df.species
  y_raw

  st.write("Descriptive Statistics")
  des = df.describe()
  des

  st.write("More information on the Data")
  info = df.info()
  info

with st.expander("Data Visualization"):
  st.scatter_chart(data=df,x="bill_length_mm",y="body_mass_g",color="species")

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island', ["Torgersen","Biscoe","Dream"])
  bill_length_mm = st.slider('Bill Length (mm)', 30.0,60.0,45.0)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.0,22.0,17.5)
  flipper_length = st.slider('Flipper Length (mm)', 172.0,231.0,201.0)
  body_mass = st.slider('Body Mass (g)', 2500,6500,4500)
  gender = st.selectbox('Gender', ['Male', 'Female'])

  data = {'island':island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'gender': gender
  }

  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df,X_raw], axis=0)

with st.expander("Input Data"):
  st.write("**Input Data**")
  input_df
  st.write("**Combined Data**")
  input_penguins
  

