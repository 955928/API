# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import json
# from sklearn.model_selection import train_test_split
# #from xgboost import XGBClassifier
# import pickle
# from sklearn.metrics import mean_absolute_error


# # Import dataframe
# iris_df = pd.read_csv("iris_data.csv")

# # Process Data
# label_encoder = LabelEncoder()
# iris_df['species_encoded'] = label_encoder.fit_transform(iris_df['species'])

# # Save processed data to new file
# iris_df.to_csv('encoded_data.csv')

# # Save encoder to json
# options_title = iris_df['species'].unique()
# dict_encoder = {}

# for item in options_title:
#     dict_encoder[str(iris_df[iris_df['species'] == item].iloc[0]['species_encoded'])] = item

# with open('encoder.json', 'w') as write_file:
#     json.dump(dict_encoder, write_file, indent=4)
    
# # Separate Features and Target : x and y datas
# y = iris_df['species_encoded'].copy()
# x = iris_df.drop(['species', 'species_encoded'], axis=1)

# # Separate TrainSet / ValidSet
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

# # Train model
# model = XGBClassifier()
# model.fit(x_train, y_train)

# Save model
with open('main_model.pkl', 'wb') as fichier_modele:
    pickle.dump(model, fichier_modele)
    
    
# Test model
predictions = model.predict(x_test)
print(f"MAE: {str(mean_absolute_error(predictions, y_test))}")