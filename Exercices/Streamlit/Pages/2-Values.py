import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


iris_df = pd.read_csv('iris_data.csv')

st.set_page_config(page_title='Iris Dataset')
st.header('Values - Iris Dataset')
st.markdown('Explores how each individual variable is related to each species.'
           'We can intuit patterns with the individual values and understand how the data is used to perform classifications.')
st.sidebar.header('Individual Values')


#Setting graph to display
options = st.sidebar.radio('Select values',
                           options=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# print(iris_df.shape)
show_df = iris_df.filter(items=[options,'species'])

plot1 = px.histogram(
    show_df,
    x=show_df[options],
    title=f'{options} Histogram',
    nbins=30,
    color='species')

st.plotly_chart(plot1)