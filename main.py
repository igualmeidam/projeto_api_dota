from fastapi import FastAPI
from request import list_comprehension


app = FastAPI()


@app.get('/')
def home():
    return 'Funcionando!'


@app.get('/heroes}')
def todos_herois():
    return list_comprehension


@app.get('/heroes/{id_heroes}')
def get_heroi_por_id(id_heroi: int):
    for id, heroi in list_comprehension:
        if id == id_heroi:
            return heroi
