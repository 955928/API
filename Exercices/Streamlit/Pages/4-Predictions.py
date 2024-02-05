import streamlit as st
import numpy as np
from make_pred import make_prediction
import json as js
import pandas as pd
import plotly.express as px
import requests



#Set up data from csv
iris_df = pd.read_csv('iris_data.csv')
#sepal_length,sepal_width,petal_length,petal_width

#Setup title page 
st.set_page_config(page_title='Predictions')
st.header('Predictions - Iris Dataset')
st.markdown('Using RandomForestClassifier to make predictions for what classification the species should fall into.'
            'The prediction will appear on the graphs below to intuit how the prediction was made')       
st.sidebar.header('Make Prediction')

sep_len = st.sidebar.text_input('Sepal Length')
sep_wid = st.sidebar.text_input('Sepal Width')
pet_len = st.sidebar.text_input('Petal Length')
pet_wid = st.sidebar.text_input('Petal Width')
make_pred_API = st.sidebar.button('Predict')

#Affichage scatter plot 

plot1 = px.scatter(
    
    iris_df,
    x='petal_length',
    y='petal_width',
    color='species',
    title='Petal Length Vs Petal Width') 


plot2 = px.scatter(
    
    iris_df,
    x='sepal_length',
    y='petal_length',
    color='species',
    title='Sepal Length Vs Petal Length')


#Launch prediction with API
if make_pred_API:
    #Construire l'url avec les paramùetres
    url = f'http://localhost:8000/{float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)}'

#Envoyer la requete à FastAPI
    response = requests.get(url)

    #Vérifier si la requete à réussi (statut 200)
    if response.status_code == 200:
        species_pred = response.json()['prediction']
        st.success(f'Prediction result: {species_pred}')
        
    else:
        st.error('Error in prediction request.')
    
    #Transformer mes x1/x2/x3/x4 en df
    p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
    x = np.array([p1])
    row = {'sepal_length': [float(sep_len)],
           'sepal_width': [float(sep_wid)],
           'petal_length': [float(pet_len)],
           'petal_width': [float(pet_wid)]}
    
    p1_df = pd.DataFrame(row)
    
    plot1.add_scatter(x=p1_df['petal_length'],
                      y=p1_df['petal_width'],
                      mode='markers',
                      name=species_pred,
                      marker=dict(
                          color='red', #Couleur des points
                          size=10,#Taille des points
                          symbol='circle', #Type de marqueur (vous pouvez choisi)
                          line=dict(
                              color='white',#couleur de la bordure des points
                              width=2#largeur de la bordure des points 
                          )
                          
                      ))
    
    
    plot1.add_scatter(x=p1_df['sepal_length'],
                    y=p1_df['petal_length'],
                    mode='markers',
                    name=species_pred,
                    marker=dict(
                        color='red', #Couleur des points
                        size=10,#Taille des points
                        symbol='circle', #Type de marqueur (vous pouvez choisi)
                        line=dict(
                            color='white',#couleur de la bordure des points
                            width=2#largeur de la bordure des points 
                        )
                        
                    ))

    
    
    
    
st.plotly_chart(plot1)
st.plotly_chart(plot2)