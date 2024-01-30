import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
 #from xgboost import XGBClassifier
import csv
import json
import pickle


def make_model_save():
    
    #Import Dataframe
    iris_df = pd.read_csv('iris_data.csv')
    #header: sepal_length, sepal_width, petal_length, petal_width, species

    #Process Data
    label_encoder = LabelEncoder()
    iris_df['species_encoded'] = label_encoder.fit_transform(iris_df['species'])

    #Save processed data to new file and json
    iris_df.to_csv('encoded_data_csv')
    options_title = iris_df['species'].unique()
    dict_encoder = {}
    
    for item in options_title:
        dict_encoder[str(iris_df[iris_df['species'] == item].iloc[0]['species_encoded'])] = item
        
    with open('encoder.json', 'w') as write_file:
        json.dump(dict_encoder, write_file, indent=4)
    print(iris_df.head(15))
    

    