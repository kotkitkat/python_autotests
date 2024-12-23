import requests


URL = "https://api.pokemonbattle.ru/v2"
TOKEN = '87ea8841645574feb98f12ac53bb9968'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :  TOKEN }
body = {
    "trainer_token": TOKEN,
    "email": "kuxi.kuk@yandex.ru",
    "password": "PuPuPu3"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_pokemon_live = {
    "name": "Виииу",
    "photo_id": 55
}
body_new_name = {
    "pokemon_id": "162732",
    "name": "мимипут",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "162732"
}
# response = requests.post( url = f'{URL}/trainers/reg', headers= HEADER, json = body )
# print(response.text)

'''response_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers =  HEADER, json = body_confirmation )
print(response_confirmation.text)'''

response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER , json =    body_pokemon_live)
print(response_create.text)

'''response_new_name = requests.put(url= f'{URL}/pokemons', headers =  HEADER, json=body_new_name)
print(response_new_name.text)'''
'''response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER , json =    body_pokeball)
print(response_pokeball.status_code)'''

message = response_create.json()['id']
print(message)