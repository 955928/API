import streamlit as st
import pandas as pd


iris_df = pd.read_csv('iris_data.csv')

st.set_page_config(page_title='Iris Dataset')
st.header('Iris Machine Learnign Project')
st.markdown('Deployment of the Iris Dataset machine learning model using XGBoost')
st.markdown('Use this dashboard to understand the data and to make predictions')
st.markdown('')
st.image('iris.png')
