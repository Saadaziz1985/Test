# Import python packages
import streamlit as st
import requests
import pandas as pd

# Write directly to the app
st.title("Hello Example Streamlit App")
st.write(
    """Choose the fruits you want in your custome smoothie!
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be', name_on_order)
