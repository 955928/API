from fastapi import FastAPI
import numpy as np
from train_model import make_model_save

app = FastAPI()

#ici c'est le fichier Back

@app.get('/infos')
def read_root():
    return {"message": "Hello, welcome on my dashboard!"}

@app.get('/train_model')
def train_model():
    make_model_save()#en appelalnt du fichier Front
    print('Training in progress')
    return{'Response': 'Training completed'}

