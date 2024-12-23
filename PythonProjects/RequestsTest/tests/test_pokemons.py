import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = '87ea8841645574feb98f12ac53bb9968'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :  TOKEN }
TRAINER_ID = '22511'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id' :  TRAINER_ID})
    assert response_get.json()["data"][0]["id"] ==  "22511"



    
