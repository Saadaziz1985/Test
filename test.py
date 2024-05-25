import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from pytesseract import pytesseract

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
 
  #img = Image.open(image_path) 
  
# Providing the tesseract executable 
# location to pytesseract library 
  #pytesseract.tesseract_cmd = path_to_tesseract 
  
# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
  text = pytesseract.image_to_string(uploaded_file) 
  
# Displaying the extracted text 
  st.write(text)
