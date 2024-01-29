import streamlit as st
import pandas as pd


iris_df = pd.read_csv('iris_data.csv')

st.set_page_config(page_title='Iris Dataset')
st.header('Values - Iris Dataset')