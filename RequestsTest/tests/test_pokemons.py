import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b6d0a4ecf0b09b7c6c2af7b555563f0f'
HEADER = {
    "trainer_token": TOKEN,
    "Content-Type": "application/json"
          }
TRAINER_ID = 4242


def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
def test_part_of_response():
    response_part = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_part.json()["data"][0]['trainer_name'] == 'GELIK'