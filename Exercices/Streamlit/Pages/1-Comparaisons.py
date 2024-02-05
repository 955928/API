import streamlit as st
import pandas as pd
import plotly.express as px

iris_df = pd.read_csv('iris_data.csv')

#Make Page
st.set_page_config(page_title='Iris Dataset')
st.header('Comparaison - Iris Dataset')
st.markdown('Explore the variables  to understand between them and how they release to the species.')
st.sidebar.header('Variable Comparaison')


#setting graph to display
options = st.sidebar.radio('Select comparaison',
                           options=['Sepal Length Vs Sepal Width',
                                   'Petal Length Vs Petal Width',
                                   'Sepal Length Vs Petal Width',
                                   'Sepal Width Vs Petal Length'])

            
#on va changer des types d'options
if options == 'Sepal Length Vs Sepal Width':
        plot = px.scatter(
                iris_df,
                x='sepal_length',
                y='sepal_width',
                color='species',
                title=options)
        #le print va seulement s'afficher sur le terminal
        # print('back option1')
        # #alors que le st.markdown s'afficherait sur le site
        # st.markdown('option 1')
elif options == 'Petal Length Vs Petal Width':
        # st.markdown('option 2')
        plot = px.scatter(
                iris_df,
                x='petal_length',
                y='petal_width',
                color='species',
                title=options)        
elif options == 'Sepal Length Vs Petal Width':
        # st.markdown('option 3')
        plot = px.scatter(
                iris_df,
                x='sepal_length',
                y='petal_width',
                color='species',
                title=options)
elif options == 'Sepal Length Vs Petal Length':
        # st.markdown('option 4')
        plot = px.scatter(
                iris_df,
                x='sepal_length',
                y='petal_length',
                color='species',
                title=options)
  
#shows chart      
st.plotly_chart(plot)