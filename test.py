import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  optionx = st.selectbox('Your x-axis is?', (df.columns))
  x=optionx
  st.write('You selected:', x)

  optiony = st.selectbox('Your y-axis is?', (df.columns))
  y=optiony
  st.write('You selected:', y)

  df['Profit']=df['Profit'].sum()
  st.bar_chart(df,x=x,y=y)
