# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
st.write(spectra_df)
