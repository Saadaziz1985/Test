import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
    # Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)
