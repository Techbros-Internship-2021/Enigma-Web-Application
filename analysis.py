from typing import Text
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.core.series import Series
import streamlit as st
import plotly.express as px
from apps import data, home, tweet,visual,maps,individual
from multiapps import MultiApp

app = MultiApp()

st.title("enigma.")
# st.markdown("""
# This is a web application to see the sentiment analysis
# """)

app.add_app("Home",home.app)
app.add_app("Data",data.app)
app.add_app("Tweet examples",tweet.app)
app.add_app("Visualization",visual.app)
app.add_app("Maps",maps.app)
app.add_app("Individual Data",individual.app)

app.run()













