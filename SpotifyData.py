#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral
from bokeh.palettes import Spectral6, Magma, Inferno
from bokeh.themes import built_in_themes
from bokeh.io import curdoc

from datetime import date, timedelta
from PIL import Image
from streamlit import caching


# In[2]:


st.title('Spotify Data')


# In[3]:


## Side Bar Information
image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort V</h1>", unsafe_allow_html=True)


add_selectbox = st.sidebar.radio(
    "",
    ("Introduction and Problem Statement", "List of Tools", "Data Set", "Data Cleaning", 
     "Exploratory Data Analysis", "Possible Business Strategies", "Recommender Engine", 
     "Possible Business Strategies", "Contributors")
)


# In[ ]:


if add_selectbox == 'Introduction and Problem Statement':
    st.write('')
    st.subheader('Introduction')
    st.write('-----------------------------------------------------------------------') 
    st.write('<b>BUSINESS OBJECTIVE:</b>', unsafe_allow_html=True)
    st.write('Provide unique and actionable insights and strategies on how to boost streams of the artists they handle in the market')
    
    st.write('<b>MARKET:</b>', unsafe_allow_html=True)
    st.markdown("<ul>"                "<li>What are the current trends in the music stream market?</li>"                "<li>What qualities are common among top-streamed music?</li>"                "<li>How has the client artist/target genre performed in the past years?</li>"                "</ul>", unsafe_allow_html=True)
                
    st.write('<b>CLIENT:</b>', unsafe_allow_html=True)
    st.markdown("<ul>"                "<li><i>Artist</i>: Based on listener data, which artist should client collaborate with in their next release?</li>"                "<li><i>Production:</i> Based on the listener data, which genre should client focus on their next release? </li>"                "<li><i>Promotions:</i> Based on the listener data, which artists should we market together in featured playlists/events? </li>"                "</ul>", unsafe_allow_html=True)


# In[ ]:


elif add_selectbox == 'Outline':
    st.subheader('Outline')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'List of Tools':
    st.subheader('List of Tools')
    st.write('-----------------------------')
    st.write('-----------------------------------------------------------------------') 
    image = Image.open('logo/spotify.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/jupyter.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/pandas.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/heroku.jpg').convert('RGB')
    st.image(image, caption='', width=150, height=50)
    image = Image.open('logo/streamlit.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/bokeh.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/github.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/regex.jpeg').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/scipy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/seaborn.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/matplotlib.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/numpy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)


# In[ ]:


elif add_selectbox == 'Data Set':
    st.subheader('Data Set')
    st.write('-----------------------------')
    
    st.write('<b>Daily Charts:</b>', unsafe_allow_html=True)
    st.markdown('<b>Sample Data Set:</b>', unsafe_allow_html=True)
    dataset_sample = {
                      'date': ['2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01'], 
                      'position': ['1', '2', '3', '4', '5'],
                      'track_id': ['0ofbQMrRDsUaVKq2mGLEAb', '0tgVpDi06FyKpA1z0VMD4v', '3hBBKuWJfxlIlnd9QFoC8k', 
                                   '1mXVgsBdtIVeCLJnSnmtdV', '2ekn2ttSfGqwhhate0LSR0'],
                      'track_name': ['Havana', 'Perfect', 'What Lovers Do (feat. SZA)', 'Too Good At Goodbyes', 'New Rules'],
                      'artist': ['Camila Cabello', 'Ed Sheeran', 'Maroon 5', 'Sam Smith', 'Dua Lipa'],
                      'streams': ['155633', '134756', '130898', '130798', '125472']
                     }
    
    st.table(dataset_sample)
    
    st.markdown('<b>Data Dimensions:</b> Rows: 541909 Columns: 8', unsafe_allow_html=True)
    st.markdown('<b>Data Description:</b>', unsafe_allow_html=True)
    
    data_details = {
        'columns': ['date', 'position', 'track_id', 'track_name', 'artist', 'streams'],
        'Description': ['Current Date of the Chart', 'Place in the Chart', 'Unique Identifier for the Song', 'Song Name', 'Name of the Singer', 'Total Number of Streams'],
        'Data Types': ['int64', 'object', 'object', 'object', 'object', 'int64']
    }
        
    st.table(pd.DataFrame(data_details).set_index('columns'))


# In[ ]:


elif add_selectbox == 'Data Cleaning':
    st.subheader('Data Cleaning')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'Exploratory Data Analysis':
    st.subheader('Exploratory Data Analysis')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'Client Track Classification':
    st.subheader('Client Track Classification')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'Recommender Engine':
    st.subheader('Recommender Engine')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'Possible Business Strategies':
    st.subheader('Possible Business Strategies')
    st.write('-----------------------------')


# In[ ]:


else:
    st.subheader('Contributors')
    st.write('-----------------------------')
    st.markdown("<ul>"                "<li>Danilo Jr. Gubaton</li>"                "<li>Fili Emerson Chua</li>"
                "<li>John Barrion</li>"\
                "<li>Justine Brian Santoalla </li>"\
                "<li>Rhey Ann Magcalas</li>"\
                 "</ul>", unsafe_allow_html=True)

