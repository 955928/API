import json
import pickle as pk

def make_prediction(x):
    #charger le model à partir d'un fichier pickle
    with open('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pk.load(fichier_modele)
    