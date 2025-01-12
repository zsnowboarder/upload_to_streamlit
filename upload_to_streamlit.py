#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd

# Title of the app
st.title('Upload and Display Excel File')

# File uploader
uploaded_file = st.file_uploader('Upload Excel file', type='xlsx')

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Display the DataFrame
    st.write(df)


# In[ ]:




