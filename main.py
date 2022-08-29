from fastapi import FastAPI
from request import herois_por_id


app = FastAPI()


@app.get('/')
def home():
    return 'funcionou!'


@app.get('/heroes}')
def todos_herois():
    return herois_por_id


@app.get('/heroes/{id_heroes}')
def get_heroi_por_id(id_heroi: int):
    for id, heroi in herois_por_id:
        if id == id_heroi:
            return heroi
