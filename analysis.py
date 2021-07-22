from typing import Text
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.series import Series
import streamlit as st
import plotly.express as px



st.title("Tweet Sentiment Analysis!")
st.markdown("""
This is an application to see the sentiment analysis
""")

st.sidebar.title('Sentimen analysis')
st.sidebar.markdown('Configure the analysis')

data=pd.read_csv('Tweets.csv')

if st.checkbox("Show Data"):
    st.write(data.head(50)) #show frist 50 data

st.sidebar.title("Tweet analyser")

tweets=st.sidebar.radio('Sentiment type',('positive','negative','neutral'))

st.markdown("""
## Example of tweets
""") #show tweets example of chosen sentiment
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])

#choose the type of visualisation
select=st.sidebar.selectbox('Visualisation of Tweets ',['Histogram','Pie Chart'])

sentiment=data['airline_sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})

#show sentiment values
st.markdown("## Number of tweets sentiment")
if select=='Histogram':
    fig=px.bar(sentiment, x='Sentiment', y='Tweets', color='Tweets', height=500)
    st.plotly_chart(fig)
else:
    fig=px.pie(sentiment, values='Tweets', names='Sentiment')
    st.plotly_chart(fig)



#to set the hour for the map
st.sidebar.markdown("Time and loation of the tweets")
hr = st.sidebar.slider("Hour of the day", 0, 23)
data['Date']=pd.to_datetime(data['tweet_created'])
hr_data=data[data['Date'].dt.hour == hr]

##show map, needs lat and lon
st.markdown("""## Maps of the Tweets
""")
st.markdown("%i tweets during %i:00 and %i:00" % (len(hr_data), hr, (hr+1)%24))
st.map(hr_data)

#show sentiment by airlines
st.sidebar.markdown("Airline tweets by sentiment")
choice=st.sidebar.multiselect("Airlines",('US Airways','United','American','Southwest','Delta','Virgin America'),key='0')
st.markdown("## Tweets sentiment based on the airlines")
if len(choice)>0:
    air_data=data[data.airline.isin(choice)]
    fig1=px.histogram(air_data, x='airline', y='airline_sentiment', histfunc='count', color='airline_sentiment', labels='airline_sentiment')
    st.plotly_chart(fig1)


