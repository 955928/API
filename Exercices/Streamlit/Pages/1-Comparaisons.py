import streamlit as st
import pandas as pd


iris_df = pd.read_csv('iris_data.csv')

st.set_page_config(page_title='Iris Dataset')
st.header('Comparaison - Iris Dataset')
st.markdown('Explore the variables  to understand between them and how they release to the species.')
st.sidebar.header('Variable Comparaison')


#setting graphs to display
options = st.sidebar.radio('Select comparaison',
                           options=['Sepal Length Vs Sepal Width',
                                   'Petal Length Vs Petal Width',
                                   'Sepal Length Vs Petal Width',
                                   'Sepal Width Vs Petal Length'])

            
