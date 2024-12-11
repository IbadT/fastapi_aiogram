# import requests
import aiohttp
from typing import Literal
from api.schemas.schemes import SPlayers, SAddFriend, SAuth, SUser

# BASE_URL = "http://localhost:8000"

class GameRepository:
    BASE_URL = "http://217.114.7.9:8000"

    @classmethod
    async def auth_via_tg(cls, user: SUser) -> SAuth:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{cls.BASE_URL}', json=dict) as response:
                response_data = await response.json()
                return response_data
        # Запрос:
        #     {
        #     "firstName": "string",
        #     "lastName": "string",
        #     "id": "number",
        #     "avatar": "string"
        #     }


    @classmethod
    async def get_players_list(cls, user_id: str, type: Literal['friends', 'players']) -> list[SPlayers]:
        # получить 
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{cls.BASE_URL}/users{user_id}?type={type}', json=dict) as response:
                response_data = await response.json()
                return response_data


    @classmethod
    async def add_friend(cls, user_id: str, id: str) -> SAddFriend:
        async with aiohttp.ClientSession() as session:
            # добавить id друга которого нужно добавить в друзья
            async with session.get(f'{cls.BASE_URL}/users/{user_id}', json=dict) as response:
                response_data = await response.json()
                return response_data




    @classmethod
    async def test(cls, id: str) -> dict:
        balance = {
            "balance": 0
        }
        # response = requests.get(f'{BASE_URL}/users/{id}/balance', json=balance)
        # return response.json()
        async with aiohttp.ClientSession() as session: 
            async with session.get(f'{cls.BASE_URL}/users/{id}/balance', 
                                   json=balance) as response: 
                response_data = await response.json() 
                return response_data