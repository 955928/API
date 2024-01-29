from fastapi import FastAPI

app = FastAPI()

# Définition d'une route avec une méthode
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Définition d'une route avec une variable de chemin
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
    