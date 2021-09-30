import streamlit as st
import plotly.express as px
import pandas as pd


def app():
    data=pd.read_csv('Tweets.csv')
    st.title("Individual sentiment data")
    st.markdown("Shows the number of data by the name of the airlines")
    #show sentiment by airlines

    choice=st.multiselect("Airlines",('US Airways','United','American','Southwest','Delta','Virgin America'),key='0')
    st.markdown("## Tweets sentiment based on the airlines")
    if len(choice)>0:
        air_data=data[data.airline.isin(choice)]
        fig1=px.histogram(air_data, x='airline', y='airline_sentiment', histfunc='count', color='airline_sentiment', labels='airline_sentiment')
        st.plotly_chart(fig1)