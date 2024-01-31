import json as js
import pickle as pk

def make_prediction(x):
    #charger le model à partir d'un fichier pickle
    with open('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pk.load(fichier_modele)
    
    
    #faire la prédiction
    predictions_out = loaded_model.predict(x)
    
    #charger le fichier encoder pour traduire la prédiction
    with open('encoder.json') as json_file:
        data = js.load(json_file)
        
    #conversion prédiction brute --> traduite
    predictions_string = data[str(int(predictions_out))]
    
    print('Predictions', predictions_string)
    
    #Retourne la valeur
    return predictions_string