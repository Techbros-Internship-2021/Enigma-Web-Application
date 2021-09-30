import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    data=pd.read_csv('Tweets.csv')

    st.title("Visualization of data")
    st.markdown("Shows the visualtization of the number of total data.")

    #choose the type of visualisation
    select=st.selectbox('Type of visualization: ',['Histogram','Pie Chart'])

    sentiment=data['airline_sentiment'].value_counts()
    sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})

    #show sentiment values
    if select=='Histogram':
        fig=px.bar(sentiment, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)