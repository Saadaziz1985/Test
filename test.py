import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
    # To read file as bytes:
bytes_data = uploaded_file.getvalue()
st.write(bytes_data)

