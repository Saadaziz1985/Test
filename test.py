import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

  option = st.selectbox(
...     'How would you like to be contacted?',
...     ('Email', 'Home phone', 'Mobile phone'))
  st.write('You selected:', option)

  df['Profit']=df['Profit'].sum()
  st.bar_chart(df,x="Country",y="Profit")
