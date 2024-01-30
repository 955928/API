import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBClassifier
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


    print(iris_df.head(15))