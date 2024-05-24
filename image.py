# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas as pd
import  tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename()

# Write directly to the app
st.title(":apple: Example Streamlit App :apple:")
st.write(
    """Choose the fruits you want in your custome smoothie!
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be', name_on_order)
