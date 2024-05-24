# Import python packages
import streamlit as st
import requests
import pandas as pd
from PIL import Image 
from pytesseract import pytesseract
import tkinter as tk
from tkinter import filedialog

# Write directly to the app
st.title(":apple: Hello Example Streamlit App :apple:")
st.write(
    """Choose the fruits you want in your custome smoothie!
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be', name_on_order)
