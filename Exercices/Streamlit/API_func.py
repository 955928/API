from fastapi import FastAPI
import numpy as np

app = FastAPI()


@app.get('/infos')
def read_root():
    return {"message": "Hello, welcome on my dashboard!"}

@app.get('/train_model')
def train_model():
    #make_model_save()
    print('Training in progress')
    return{'Response': 'Training completed'}

