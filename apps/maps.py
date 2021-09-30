import streamlit as st
import pandas as pd

def app():
    data=pd.read_csv('Tweets.csv')

    st.title("Maps")
    st.markdown("Shows the number of tweets and location where the tweets are created within the time span of one hour")

    #to set the hour for the map
    hr = st.slider("Hour of the day:", 0, 23)
    data['Date']=pd.to_datetime(data['tweet_created'])
    hr_data=data[data['Date'].dt.hour == hr]

    ##show map, needs lat and lon
    st.markdown("""## Location of the tweets
    """)
    st.markdown("%i tweets during %i:00 and %i:00" % (len(hr_data), hr, (hr+1)%24))
    st.map(hr_data)