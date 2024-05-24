# Import python packages
import streamlit as st
import requests
import pandas as pd
from PIL import Image 
from pytesseract import pytesseract

# Write directly to the app
st.title(":apple: Hello Example Streamlit App :apple:")
st.write(
    """Choose the fruits you want in your custome smoothie!
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be', name_on_order)
image_path = r"C:\Users\Saad Aziz\Downloads\Data Source Python\sample.png"

# Opening the image & storing it in an image object 
img = Image.open(image_path) 
  
# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 
  
# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
text = pytesseract.image_to_string(img) 
  
# Displaying the extracted text 
print(text[:-1])
