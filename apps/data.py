import streamlit as st
import pandas as pd

def app():
    st.title("Data")
    st.markdown("The dataset used in this web application is the sentiment analysis of airlines in the United States. Here is the first 100 data from the dataset.")

    data=pd.read_csv('Tweets.csv')
    st.write(data.head(100)) #show frist 100 data