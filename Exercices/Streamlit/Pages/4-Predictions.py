import streamlit as st
import numpy as np
from make_pred import make_prediction
import json as js
import pandas as pd
import plotly.express as px
import requests



#Set up data from csv
df = pd.read_csv('iris_data.csv')
#sepal_length,sepal_width,petal_length,petal_width

#Setup title page 
st.set_page_config(page_title='Predictions')
st.header('Predictions - Iris Dataset')
st.markdown('Using RandomForestClassifier to make predictions for what classification the species should fall into.'
            'The prediction will appear on the graphs below to intuit how the prediction was made')       
st.sidebar.header('Make Predictions')

sep_len = st.sidebar.text_input('sepal_length')
sep_wid = st.sidebar.text_input('sepal_width')
pet_len = st.sidebar.text_input('petal_length')
pet_wid = st.sidebar.text_input('petal_width')
make_pred_API = st.sidebar.button('predict')


#Launch prediction with API
if make_pred_API:
    #Construire l'url avec les paramùetres
    url = f'http://localhost:8000/({float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)})'

#Envoyer la requete à FastAPI
response = requests.get(url)

#Vérifier si la requete à réussi (statut 200)
if response.status_code == 200:
    species_pred = response.js()['prediction']
    st.success(f'Prediction result: {species_pred}')
    
else:
    st.error('Error in prediction request')