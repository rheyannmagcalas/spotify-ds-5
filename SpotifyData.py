#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
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

from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity


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
    ("Introduction", "Client", "List of Tools", "Process Flow", "Data Sourcing", "Data Set", 
     "Data Cleaning", "Exploratory Data Analysis", "Song Genre Classification", "Recommender Engine", 
     "Possible Business Strategies", "Contributors", "Spotify Settings")
)


# In[23]:


if add_selectbox == 'Introduction':
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
    
    st.write('-----------------------------')
    st.text('Spotify Statistics as of 10/16/2020')
    st.write('<table>'             '<tr><td><b>Popularity</b></td><td><b>Total Followers</b></td><td><b>Monthly Listeners</b></td></tr>'             '<tr><td>56</td><td>67077</td><td>246030</td></tr>'             '</table><br/>', unsafe_allow_html=True)
    
    st.text('Where People Listens as of 10/16/2020')
    st.write('<table>'             '<tr><td>Quezon City, PH</td><td>17,276 Listeners</td></tr>'             '<tr><td>Toronto, Ca</td><td>8, 963 Listeners</td></tr>'             '<tr><td>Vancouver, Ca</td><td>8, 155 Listeners</td></tr>'             '<tr><td>Makati City, PH</td><td>6, 596 Listeners</td></tr>'             '<tr><td>Manila, PH</td><td>6, 204 Listeners</td></tr>'             '</table><br/>', unsafe_allow_html=True)
    st.write('-----------------------------')
    st.write('<b>Playlist</b>', unsafe_allow_html=True)
    st.write('<table><tr><td><iframe src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7FY5ma9162x" '             'width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media">'             '</iframe></td></tr>'             '<tr><td><iframe src="https://open.spotify.com/embed/playlist/37i9dQZF1DWW4igXXl2Qkp" '             'width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media">'             '</iframe></td></tr>'             '<tr><td><iframe src="https://open.spotify.com/embed/playlist/1Os7m597ihMJ4xTohCkZIz" '             'width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media">'             '</iframe></td></tr>'             '<tr><td><iframe src="https://open.spotify.com/embed/playlist/37i9dQZF1DX59ogDi1Z2XL" '             'width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media">'             '</iframe></td></tr>'             '<tr><td><iframe src="https://open.spotify.com/embed/playlist/37i9dQZF1DX2WkIBRaChxW" '             'width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media">'             '</iframe></td></tr>'             '</table>', unsafe_allow_html=True)
    
    st.write('-----------------------------')
    st.write('<b>Albums</b>', unsafe_allow_html=True)
    
    data_details = {
        'album_name': ['No Saints Loading', 'No Saints Under Palm Shade'],
        'Total Tracks': ['10', '6'],
        'Release Date': ['2019-11-27', '2017-10-13']
    }
    
    st.write('<table>'             '<tr>'                 '<td><b>Title</b></td> <td><b>Total Tracks</b></td> <td><b>Release Date</b></td> <td><b>Songs</b></td>'             '</tr>'             '<tr>'                 '<td>No Saints Loading</td><td>10</td><td>2019-11-27</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/2wNYSXK9UBfBj5sGYOJpfT" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'
             '</tr>'
             '<tr>'\
                 '<td>No Saints Under Palm Shade</td><td>6</td><td>2017-10-13</td>'\
                '<td><iframe src="https://open.spotify.com/embed/album/58ToNt6xB7YugO9rhC7rEo" width="300" height="300" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'\
             '</tr>'
             '</table>', unsafe_allow_html=True)  
    
    st.write('<br><br><b>Singles and EPS</b>', unsafe_allow_html=True)
    st.write('<table>'             '<tr>'                 '<td><b>Title</b></td><td><b>Release Date</b></td> <td><b>Spotify Link</b></td>'             '</tr>'             '<tr>'                 '<td>Shibuya</td><td>2020-08-26</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/0C3NEeNrQGx9i189EuWglz" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Blue Vegata</td><td>2020-07-29</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/3pbG0i2bdjZVFuzd89adGd" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Silver Skies</td><td>2019</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/1zs9AJzF5Z8rvSuHvCfnLp" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Youth Water</td><td>2017-05-15</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/32MOJzuCDZsviw1hfBDOfk" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Friends of Friends</td><td>2018-02-23</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/2m4zj5J0Ta6Mt43hadaML9" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Midnight</td><td>2017-12-08</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/7n9LerpieN1jsQLDV0NSe7" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Free Spirit</td><td>2017</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/2L6oLL2eWz8DI6JF3cqVab" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Feel We like</td><td>2017</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/7KHzZS6lw9Y9wSxnXMS6sw" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Eastbound</td><td>2017</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/12zdLt8RAuiC23P4qu7eda" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Lined Up</td><td>2017-12-08</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/3x3ilXcSBtMIuKdEBz7vEa" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>Parking Lot</td><td>2016</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/7bDkp9qDtWEriKm7bQVmOu" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '<tr>'                 '<td>1Z</td><td>2016</td>'                 '<td><iframe src="https://open.spotify.com/embed/album/3d2OWITI93qH73X9Afq3SC" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td>'             '</tr>'             '</table>', unsafe_allow_html=True) 
    
    st.write('<br><br>More Info:<a href="https://www.manilagrey.com/" target="_blank">Website</a>, '             '<a href="https://open.spotify.com/artist/7KC9q5wx0bxMD5ABgLCoEd" target="_blank">Spotify</a>,     '             '<a href="https://www.youtube.com/channel/UCUNC9hmB6I7MvY2w2LF5fUQ" target="_blank">Youtube</a>     '             '<a href="https://www.instagram.com/manilagrey/?hl=en" target="_blank">Instagram</a>'             '<a href="https://facebook.com/manilagreymusic" target="_blank">Facebook</a>'
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
    image = Image.open('logo/numpy.png')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/wikipedia.png')
    st.image(image, caption='', width=300, height=150)


# In[ ]:


elif add_selectbox == 'Process Flow':
    st.subheader('Process Flow')
    st.write('-----------------------------')
    st.markdown("<ul>"                "<li>Data Sourcing</li>"                "<li>Data Cleaning</li>"                "<li>Exploratory Data Analysis</li>"                "<li>Feature Importance</li>"                "<li>Track Genre Classification</li>"                "<li>Recommendation Engine</li>"                "<li>Deployment</li>"                "</ul>", unsafe_allow_html=True)


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
    
    
    st.write('4. <a href="https://developer.spotify.com/documentation/web-api/reference/search/search/" target="_blank"> '             'Get Playlists</a>', unsafe_allow_html=True)
    
    st.write("&nbsp;<span style='font-size:14px;'>Parameters:</span>", unsafe_allow_html=True)
    st.code("q = Search query keywords", language='python')
    st.code("type = A comma-separated list of item types to search across.", language='python')
    st.code("market = An ISO 3166-1 alpha-2 country code", language='python')
    
    st.write('5. <a href="https://pypi.org/project/wikipedia/" target="_blank"> '             'Checking if an artist is a Filipino</a>', unsafe_allow_html=True)
    


# In[ ]:


elif add_selectbox == 'Data Set':
    st.subheader('Data Set')
    st.write('-----------------------------')
    
    st.markdown('<b>Data Dimensions:</b> Rows: 197800', unsafe_allow_html=True)
    
    st.write('<b> Top 200 Daily Charts:</b>', unsafe_allow_html=True)

    
    data_details = {
        'columns': ['date', 'position', 'track_id', 'track_name', 'artist', 'streams'],
        'Description': ['Current Date of the Chart', 'Place in the Chart', 'Unique Identifier for the Song', 'Song Name', 'Name of the Singer', 'Total Number of Streams'],
        'Data Types': ['int64', 'object', 'object', 'object', 'object', 'int64'],
        'Sample Data': ['2020-01-01', 1, '1xQ6trAsedVPCdbtDAmk0c', 'Savage Love', 'Jason Derulo', '125472']
    }
        
    st.table(pd.DataFrame(data_details).set_index('columns'))
    
    st.write('-----------------------------')
    st.write('<b> Track Audio Features:</b>', unsafe_allow_html=True)

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
        'Data Types': ['2018-01-01', 1, '0ofbQMrRDsUaVKq2mGLEAb', '2', '2', '1', 1, 2, 3, 1, 1, 1]
    }
    
    st.table(pd.DataFrame(data_details).set_index('columns'))
    
    st.write('-----------------------------')
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
    
    option = st.selectbox(
     'Topics:',
     ('1. R&B Top 200 Distribution', '2. Manila Grey & R&B Top 200 Distribution'))
    
    if option == '1. R&B Top 200 Distribution':
        
        st.markdown('<span style="margin-left:5%">1. R&B Data </span>', unsafe_allow_html=True)
        st.markdown('<span style="margin-left:5%">2. Merge Top 200 and R&B Data </span>', unsafe_allow_html=True)
        st.markdown('<span style="margin-left:5%">3. Check How Many R&B Songs in Top 200 </span>', unsafe_allow_html=True)
        st.markdown('<span style="margin-left:8%">a. <b>Count:</b> 37/2292 </span>', unsafe_allow_html=True)
        st.markdown('<span style="margin-left:8%">b. <b>Percentage:</b> 1.61% </span>', unsafe_allow_html=True)
        
        st.markdown('<span style="margin-left:5%">Conclusion: R&B is a tough market</span>', unsafe_allow_html=True)

    else:
        with open('top_200_rnb.pkl', 'rb') as handle:
            top_200 = pickle.load(handle)
        df_Non200 = top_200[top_200['Top200'] ==False]
        df_200 = top_200[top_200['Top200'] ==True]

        with open('seed_tracks.pkl', 'rb') as handle:
            manila_grey_songs = pickle.load(handle)
         
        for col in ['danceability', 'energy','loudness', 'speechiness', 'acousticness', 'instrumentalness','liveness', 'valence', 'tempo']:
            fig = plt.figure()
            ax= fig.add_subplot(111)

            sns.distplot(df_Non200[col], ax=ax, label= 'R&B')
            sns.distplot(manila_grey_songs[col], ax=ax, label= 'Manila Grey')
            plt.ylabel('Frequency')
            plt.legend(frameon=False)
            plt.show()
            
            st.pyplot(fig)
        
        st.write('Top 200')
        st.table(df_200[['danceability', 'energy', 'key',       'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',       'liveness', 'valence', 'tempo']].describe())
        
        st.write('R&B Top 200')
        st.table(df_Non200[['danceability', 'energy', 'key',        'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',        'liveness', 'valence', 'tempo']].describe())


# In[ ]:


elif add_selectbox == 'Song Genre Classification':
    st.subheader('Song Genre Classification')
    st.write('-----------------------------')
    
    st.write('Logistic Regression')
    


# In[ ]:


elif add_selectbox == 'Recommender Engine':
    st.subheader('Recommender Engine')
    st.write('-----------------------------')
    user_input = st.text_input("Song Title")
    
    
    if st.button('Check Results'):        
        
        chart_tracks_df = pickle.load(open("chart_tracks_df.pkl", "rb" ))
        feature_cols = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',                    'liveness', 'valence', 'tempo']

        seed_track_data = chart_tracks_df[chart_tracks_df['track_name']==user_input].iloc[0]
        
        ## cosine_similarity
        cosine_data = chart_tracks_df
        cosine_data['cosine_dist'] = cosine_data.apply(lambda x: cosine_similarity(x[feature_cols].values.reshape(-1, 1),                                                                      seed_track_data[feature_cols].values.reshape(-1, 1))                                                                      .flatten()[0], axis=1)

        cosine_recommendation_df = cosine_data[cosine_data['track_id']!=seed_track_data['track_id']][['track_id', 'track_name','artist_name','cosine_dist','predicted_genre']].sort_values('cosine_dist').drop_duplicates()[:10]    
        
        st.write('-----------------------------')
        st.markdown('<b>Cosine Similarity Result</b>', unsafe_allow_html=True)
            
        cosine_table = '<table>'
        cosine_table = '<tr><td><b>Track Name</b></td><td><b>Artist Name</b></td><td><b>Cosine Dist</b></td><td><b>Prediction Genre</b></td><td><b>Spotify Song</b></td></tr>'
        
        for index, row in cosine_recommendation_df.iterrows():
            row['cosine_dist'] = round(row['cosine_dist'], 2)
            cosine_table += '<tr><td>'+row['track_name']+'<td>'+row['artist_name']+            '</td><td>'+str(row['cosine_dist'])+'</td><td>'+str(row['predicted_genre'])+'</td>'
            cosine_table += '<td><iframe src="https://open.spotify.com/embed/track/'+row['track_id']+'" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td></tr>'         
        cosine_table += '</table>'
        
        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials
        
        import keyring
        import time

        client_id=os.environ['client_id']
        client_secret=os.environ['client_secret']

        username = os.environ['username']
        scope_playlist = 'playlist-modify-public'
        scope_user = 'user-library-modify'

        #Credentials to access the Spotify Music Data
        manager = SpotifyClientCredentials(client_id,client_secret)
        sp = spotipy.Spotify(client_credentials_manager=manager)
        
        sp_user = spotipy.Spotify(auth=os.environ['user_token'])
        sp_playlist = spotipy.Spotify(auth=os.environ['playlist_token'])
        
        new_playlist_name = "Eskwelabs: Cosine Similarity Recommendations for seed track: {}".format(user_input)    
        new_playlist = sp_playlist.user_playlist_create(username, name=new_playlist_name)   

        sp_playlist.user_playlist_add_tracks(username, new_playlist['id'], list(cosine_recommendation_df['track_id']))
        
        st.markdown('<a href ="'+new_playlist['external_urls']['spotify']+'" target="_blank">Listen to Cosine Suggested Playlist</a>', unsafe_allow_html=True)
        st.write(cosine_table, unsafe_allow_html=True)
        
        ## euclidean_distances
        st.write('-----------------------------')
        st.markdown('<b>Euclidean Distances Result</b>', unsafe_allow_html=True)
        euclidean_data = chart_tracks_df
        euclidean_data['euclidean_dist'] = euclidean_data.apply(lambda x: euclidean_distances(x[feature_cols].values.reshape(-1, 1),                                                                      seed_track_data[feature_cols].values.reshape(-1, 1))                                                                      .flatten()[0], axis=1)

        euclidean_recommendation_df = euclidean_data[euclidean_data['track_id']!=seed_track_data['track_id']][['track_id', 'track_name','artist_name','euclidean_dist','predicted_genre']].sort_values('euclidean_dist')[:10]    
        
        euclidean_table = '<table>'
        euclidean_table = '<tr><td><b>Track Name</b></td><td><b>Artist Name</b></td><td><b>Euclidean Dist</b></td><td><b>Prediction Genre</b></td><td><b>Spotify Song</b></td></tr>'
        for index, row in euclidean_recommendation_df.iterrows():
            row['euclidean_dist'] = round(row['euclidean_dist'], 2)
            euclidean_table += '<tr><td>'+row['track_name']+'<td>'+row['artist_name']+            '</td><td>'+str(row['euclidean_dist'])+'</td><td>'+str(row['predicted_genre'])+'</td>'
            euclidean_table += '<td><iframe src="https://open.spotify.com/embed/track/'+row['track_id']+'" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td></tr>'         
        euclidean_table += '</table>'
        st.write(euclidean_table, unsafe_allow_html=True)


        ## manhattan_distances
        st.write('-----------------------------')
        st.markdown('<b>Manhattan Distances Result</b>', unsafe_allow_html=True)
        manhattan_data = chart_tracks_df
        manhattan_data['manhattan_dist'] = manhattan_data.apply(lambda x: manhattan_distances(x[feature_cols].values.reshape(-1, 1),                                                                      seed_track_data[feature_cols].values.reshape(-1, 1))                                                                      .flatten()[0], axis=1)
        manhattan_recommendation_df = manhattan_data[manhattan_data['track_id']!=seed_track_data['track_id']][['track_id', 'track_name','artist_name','manhattan_dist','predicted_genre']].sort_values('manhattan_dist')[:10]    
        manhattan_table = '<table>'
        manhattan_table = '<tr><td><b>Track Name</b></td><td><b>Artist Name</b></td><td><b>Manhatan Dist</b></td><td><b>Prediction Genre</b></td><td><b>Spotify Song</b></td></tr>'
        for index, row in manhattan_recommendation_df.iterrows():
            row['manhattan_dist'] = round(row['manhattan_dist'], 2)
            manhattan_table += '<tr><td>'+row['track_name']+'<td>'+row['artist_name']+            '</td><td>'+str(row['manhattan_dist'])+'</td><td>'+str(row['predicted_genre'])+'</td>'
            manhattan_table += '<td><iframe src="https://open.spotify.com/embed/track/'+row['track_id']+'" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe></td></tr>'         
        manhattan_table += '</table>'
        st.write(manhattan_table, unsafe_allow_html=True)
        


# In[ ]:


elif add_selectbox == 'Possible Business Strategies':
    st.subheader('Possible Business Strategies')
    st.write('-----------------------------')


# In[ ]:


elif add_selectbox == 'Contributors':
    st.subheader('Contributors')
    st.write('-----------------------------')
    st.markdown("<ul>"                "<li>Danilo Jr. Gubaton</li>"                "<li>Fili Emerson Chua</li>"
                "<li>John Barrion</li>"\
                "<li>Justine Brian Santoalla </li>"\
                "<li>Rhey Ann Magcalas</li>"\
                 "</ul>", unsafe_allow_html=True)


# In[ ]:


else:
    username = st.text_input('Username')
    if username != '':
        os.environ['username'] = username
    
    client_id = st.text_input('Client Id')
    if client_id != '':
        os.environ['client_id'] = client_id
    
    client_secret = st.text_input('Client Secret')
    if client_secret != '':
        os.environ['client_secret'] = client_secret
    
    user_token = st.text_input('User Token')
    if user_token != '':
        os.environ['user_token'] = user_token
        
    playlist_token = st.text_input('Playlist Token')
    if playlist_token != '':
        os.environ['playlist_token'] = playlist_token

