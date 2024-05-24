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
