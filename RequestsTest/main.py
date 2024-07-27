import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b6d0a4ecf0b09b7c6c2af7b555563f0f'
HEADER = {
    "trainer_token": TOKEN,
    "Content-Type": "application/json"
          }


body_create = {
    "name": "Gelik",
    "photo_id": 25
}

body_change = {
    "pokemon_id": "45466",
    "name": "Pukich",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "45466"
}


response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.json())

changes = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(changes.json())

catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(catch.json())

