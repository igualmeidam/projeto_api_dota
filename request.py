import urllib3
import json

# Object handling connection pooling and thread safety.
http = urllib3.PoolManager()

# requests are made with the request() method of the manager instance and
# providing it with the HTTP method and the desired URL
lista_herois = http.request(
    'GET',
    'https://api.opendota.com/api/heroes'
)


# transformando a informação json em data manipulável para o python
dados_herois = json.loads(lista_herois.data.decode('utf-8'))

herois_por_id = [[x['id'], x['localized_name']] for x in dados_herois]

