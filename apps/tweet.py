import streamlit as st
import pandas as pd

def app():
    data=pd.read_csv('Tweets.csv')


    st.title("Tweet examples")
    st.markdown("""
    Shows five example of tweets based on its sentiment.
    """) #show tweets example of chosen sentiment
    tweets=st.radio('Choose sentiment type!',('positive','negative','neutral'))

    st.markdown("""
    ## **Tweets:**
    
    """)

    st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
    st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
    st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
    st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
    st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
