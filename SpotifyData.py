#!/usr/bin/env python
# coding: utf-8

# In[25]:


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
from IPython import get_ipython
from PIL import Image
from streamlit import caching


# ### Setting Title of the Web

# In[11]:


st.title('Spotify Data')


# ### Side Bar Information

# In[18]:


image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort V</h1>", unsafe_allow_html=True)


add_selectbox = st.sidebar.radio(
    "",
    ("Introduction and Problem Statement", "Client", "List of Tools", "Process Flow", "Data Sourcing", "Data Set", 
     "Data Cleaning", "Exploratory Data Analysis", "Track Genre Classification", "Recommender Engine", 
     "Possible Business Strategies", "Contributors")
)


# In[23]:


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


elif add_selectbox == 'Client':
    st.subheader('Client')
    st.write('-----------------------------')
    image = Image.open('logo/client.png').convert('RGB')
    st.image(image, caption='', width=800, height=200)
    
    st.write('<h3><b>Manila Grey</b></h3> Musical duo <br><br>', unsafe_allow_html=True)

    st.write('Filipino-Canadian group MANILA GREY is here to help bridge the East and West. The R&B duo '             'is comprised of childhood friends Neeko and Soliven, who grew up in Vancouver at a time when there were '             'few Asian personalities to serve as influences.')
    
    st.write('<b>Albums</b>', unsafe_allow_html=True)
    
    data_details = {
        'album_name': ['No Saints Loading', 'No Saints Under Palm Shade'],
        'Total Tracks': ['10', '6'],
        'Release Date': ['2019-11-27', '2017-10-13']
    }
     
    st.write('<table>'             '<tr>'                 '<td><b>Title</b></td> <td><b>Total Tracks</b></td> <td><b>Release Date</b></td> <td><b>Spotify Link</b></td>'             '</tr>'             '<tr>'                 '<td>No Saints Loading</td><td>10</td><td>2019-11-27</td>'                 '<td><a href="https://open.spotify.com/album/2wNYSXK9UBfBj5sGYOJpfT" target="_blank">Listen</a></td>'             '</tr>'
             '<tr>'\
                 '<td>No Saints Under Palm Shade</td><td>6</td><td>2017-10-13</td>'\
                 '<td><a href="https://open.spotify.com/album/58ToNt6xB7YugO9rhC7rEo" target="_blank">Listen</a></td>'\
             '</tr>'
             
             '</table>', unsafe_allow_html=True)  
    
    st.write('<br><br><b>Singles</b>', unsafe_allow_html=True)
    st.write('<table>'             '<tr>'                 '<td><b>Title</b></td><td><b>Release Date</b></td> <td><b>Spotify Link</b></td>'             '</tr>'             '<tr>'                 '<td>Shibuya</td><td>2020-08-26</td>'                 '<td><a href="https://open.spotify.com/album/0C3NEeNrQGx9i189EuWglz" target="_blank">Listen</a></td>'             '</tr>'             '<tr>'                 '<td>Blue Vegata</td><td>2020-07-29</td>'                 '<td><a href="https://open.spotify.com/album/3pbG0i2bdjZVFuzd89adGd" target="_blank">Listen</a></td>'             '</tr>'             '<tr>'                 '<td>Youth Water</td><td>2017-05-15</td>'                 '<td><a href="https://open.spotify.com/album/32MOJzuCDZsviw1hfBDOfk" target="_blank">Listen</a></td>'             '</tr>'             '<tr>'                 '<td>Friends of Friends</td><td>2018-02-23</td>'                 '<td><a href="https://open.spotify.com/album/4NzqaQYVb0SbPaKlAH0UCE" target="_blank">Listen</a></td>'             '</tr>'             '<tr>'                 '<td>Midnight</td><td>2017-12-08</td>'                 '<td><a href="https://open.spotify.com/album/7n9LerpieN1jsQLDV0NSe7" target="_blank">Listen</a></td>'             '</tr>'             '</table>', unsafe_allow_html=True) 
    #st.table(pd.DataFrame(data_details).set_index('album_name'))
    
    
#     st.write('<b>Singles</b>', unsafe_allow_html=True)
    
#     data_details = {
#         'single_name': ['No Saints Loading Under Palm Shade', 'Shibuya', 'Blue Vegata', 'Youth Water', 
#                         'Friends of Friends', 'Midnight'],
#         'Release Date': ['2017-10-13', '2020-08-26', '2020-07-29', '2017-05-15', '2018-02-23',  '2017-12-08']
#     }
    
#     st.table(pd.DataFrame(data_details).set_index('single_name'))
    
    st.write('<br><br>More Info:<a href="https://www.manilagrey.com/" target="_blank">Website</a>,   '             '<a href="https://open.spotify.com/artist/7KC9q5wx0bxMD5ABgLCoEd" target="_blank">Spotify</a>,     '             '<a href="https://www.youtube.com/channel/UCUNC9hmB6I7MvY2w2LF5fUQ" target="_blank">Youtube</a>     '             '<a href="https://www.instagram.com/manilagrey/?hl=en" target="_blank">Instagram</a>'
             , unsafe_allow_html=True)


# In[ ]:


elif add_selectbox == 'List of Tools':
    st.subheader('List of Tools')
    st.write('-----------------------------')
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


elif add_selectbox == 'Data Process':
    st.subheader('Data Process')
    st.write('-----------------------------')
    st.markdown("<ul>"                "<li>Data Sourcing</li>"                "<li>Data Cleaning</li>"                "<li>Creation of Market Data Science Questions</li>"                "<li>Exploratory Data Analysis</li>"                "<li>Track Genre Classification</li>"                "<li>Recommendation Engine</li>"                "<li>Deployment</li>"                 "</ul>", unsafe_allow_html=True)


# In[ ]:


elif add_selectbox == 'Data Sourcing':
    st.subheader('Data Sourcing')
    st.write('-----------------------------')
    st.write('1. Web scraping from https://spotifycharts.com/regional', unsafe_allow_html=True)
    st.write("&nbsp;<span style='font-size:14px;'>Parameters:</span>", unsafe_allow_html=True)
    st.code("start_date = first target date in YYYY-mm-dd format", language='python')
    st.code("end_date = second target date in YYYY-mm-dd format", language='python')
    st.code('regions = ["global", "us", "gb", "ad", "ar", "at", "au", "be", "bg", "bo", "br", "ca", "ch", "cl", "co", "cr", "cy", "cz", "de","dk", "do", "ec", "ee", "es", "fi", "fr", "gr", "gt", "hk", "hn", "hu", "id", "ie", "is", "it", "jp", "lt", "lu", "lv", "mc", "mt", "mx", "my", "ni", "nl", "no", "nz", "pa", "pe","ph", "pl", "pt", "py", "se", "sg", "sk", "sv", "tr", "tw", "uy"]', language='python')
    
    st.write('2. <a href="https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/" target="_blank"> '             'Get Audio Features for a Track</a>', unsafe_allow_html=True)
    st.code("GET https://api.spotify.com/v1/audio-features/{id}", language='python')
    st.write("&nbsp;<span style='font-size:14px;'>Parameter:</span>", unsafe_allow_html=True)
    st.code("id = The Spotify ID for the playlist.", language='python')
    
    st.write('3. <a href="https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/" target="_blank"> '             'Get Artist Details</a>', unsafe_allow_html=True)
    st.code("GET https://api.spotify.com/v1/artists/{id}", language='python')
    st.write("&nbsp;<span style='font-size:14px;'>Parameter:</span>", unsafe_allow_html=True)
    st.code("id = The Spotify ID for the artist.", language='python')
    
    
    st.write('4. <a href="https://developer.spotify.com/documentation/web-api/reference/search/search/" target="_blank"> '             'Get Sample Playlist Details</a>', unsafe_allow_html=True)
    
    st.write("&nbsp;<span style='font-size:14px;'>Parameters:</span>", unsafe_allow_html=True)
    st.code("q = Search query keywords", language='python')
    st.code("type = A comma-separated list of item types to search across.", language='python')
    st.code("market = An ISO 3166-1 alpha-2 country code", language='python')
    
    st.write('5. <a href="https://pypi.org/project/wikipedia/" target="_blank"> '             'Checking if an artist is a Filipino</a>', unsafe_allow_html=True)
    


# In[ ]:


elif add_selectbox == 'Data Set':
    st.subheader('Data Set')
    st.write('-----------------------------')
    
    st.markdown('<b>Data Dimensions:</b> Rows: 197800 Columns: 27', unsafe_allow_html=True)
    
    st.write('<b> Top 200 Daily Charts:</b>', unsafe_allow_html=True)
    st.markdown('Sample Data Set:', unsafe_allow_html=True)
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
    
    
    st.markdown('Data Description:', unsafe_allow_html=True)
    
    data_details = {
        'columns': ['date', 'position', 'track_id', 'track_name', 'artist', 'streams'],
        'Description': ['Current Date of the Chart', 'Place in the Chart', 'Unique Identifier for the Song', 'Song Name', 'Name of the Singer', 'Total Number of Streams'],
        'Data Types': ['int64', 'object', 'object', 'object', 'object', 'int64']
    }
        
    st.table(pd.DataFrame(data_details).set_index('columns'))
    
    st.write('<b> Track Audio Features:</b>', unsafe_allow_html=True)
    st.markdown('<b>Sample Data Set:</b>', unsafe_allow_html=True)
    dataset_sample = {
                      'duration_ms': ['2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01'], 
                      'key': ['1', '2', '3', '4', '5'],
                      'mode': ['0ofbQMrRDsUaVKq2mGLEAb', '0tgVpDi06FyKpA1z0VMD4v', '3hBBKuWJfxlIlnd9QFoC8k', 
                                   '1mXVgsBdtIVeCLJnSnmtdV', '2ekn2ttSfGqwhhate0LSR0'],
                      'acousticness': ['1', '2', '3', '4', '5'],
                      'danceability': ['1', '2', '3', '4', '5'],
                      'energy': ['1', '2', '3', '4', '5'],
                      'instrumentalness': ['1', '2', '3', '4', '5'],
                      'liveness': ['1', '2', '3', '4', '5'],
                      'loudness': ['1', '2', '3', '4', '5'],
                      'speechiness': ['1', '2', '3', '4', '5'],
                      'valence': ['1', '2', '3', '4', '5'],
                      'tempo': ['1', '2', '3', '4', '5'],
                     }
    st.table(dataset_sample)
    data_details = {
        'columns': ['duration_ms', 'key', 'mode', 'acousticness', 'danceability', 'energy', 'instrumentalness',
                   'liveness', 'loudness', 'speechiness', 'valence', 'tempo'],
        'Description': ['The duration of the track in milliseconds.', 'The estimated overall key of the track.',
                       'Indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived.',
                       'A confidence measure from 0.0 to 1.0 of whether the track is acoustic.', 
                       'Describes how suitable a track is for dancing based on a combination of musical elements including '\
                        'tempo, rhythm stability, beat strength, and overall regularity.',
                       'A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.',
                       'Predicts whether a track contains no vocals.', 'Detects the presence of an audience in the recording.',
                        'The overall loudness of a track in decibels (dB).', 'Detects the presence of spoken words in a track.',
                        'A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.', 
                        'The overall estimated tempo of a track in beats per minute (BPM). '
                       ],
#         'Data Types': ['int64', 'object', 'object', 'object', 'object', 'int64']
    }
    
    st.table(pd.DataFrame(data_details).set_index('columns'))
    
    st.markdown('<b>Data Description:</b>', unsafe_allow_html=True)
    st.write('<b> Artist Details:</b>', unsafe_allow_html=True)
    st.markdown('<b>Sample Data Set:</b>', unsafe_allow_html=True)
    dataset_sample = {
                      'artist_id': ['2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01', '2018-01-01'], 
                      'artist_name': ['1', '2', '3', '4', '5'],
                      'album_id': ['0ofbQMrRDsUaVKq2mGLEAb', '0tgVpDi06FyKpA1z0VMD4v', '3hBBKuWJfxlIlnd9QFoC8k', 
                                   '1mXVgsBdtIVeCLJnSnmtdV', '2ekn2ttSfGqwhhate0LSR0'],
                      'artist_popularity': ['1', '2', '3', '4', '5'],
                     }
    
    st.table(dataset_sample)
    
    st.markdown('<b>Data Description:</b>', unsafe_allow_html=True)


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
    user_input = st.text_input("Song Title")
    st.write(user_input)


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

