from fastapi import APIRouter, HTTPException
from api.schemas.schemes import SPlayers, SAddFriend, SAuth
from typing import Literal
from api.repository import GameRepository


players_data = [ 
    {"fullName": "John Doe", "league": "Gold", "coins": 1500, "avatar": "avatar1.png", "isFriend": True}, 
    {"fullName": "Jane Smith", "league": "Silver", "coins": 1200, "avatar": "avatar2.png", "isFriend": False} 
] 

friends_data = [ 
    {"fullName": "Alice Johnson", "league": "Platinum", "coins": 2000, "avatar": "avatar3.png", "isFriend": True}, 
    {"fullName": "Bob Brown", "league": "Gold", "coins": 1800, "avatar": "avatar4.png", "isFriend": True} 
]






router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)

# 1
@router.get('/auth')
# async def auth_via_tg() -> SAuth:
async def auth_via_tg() -> dict:
    return await GameRepository.test(1)
    # {"wallet": "wallet_1"}
    # return {'wallet': 'Ok'}


# 2
@router.get("/get-players-list")
async def get_players_list(type: Literal['friends', 'players']) -> list[SPlayers]:
    if type == "players": 
        return players_data 
    elif type == "friends": 
        return friends_data 
    else: raise HTTPException(status_code=400, 
                              detail="Invalid type parameter")
#     return    [{
#         "fullName": "str",
#         "league": "str",
#         "coins": 200,
#         "avatar": "str",
#         "isFriend": False,
#    }]

# 3
@router.get("/add-friend", response_model=SAddFriend) 
async def add_friend(id: str) -> SAddFriend: 
    # Логика для добавления пользователя в друзья 
    try: 
        # Пример логики добавления в друзья 
        if not id: 
            raise ValueError("ID is required") 
        # Ваш код для добавления пользователя в друзья по ID 
        # Например, проверка существования пользователя и добавление в список друзей 
        # if add_to_friends(id): 
            # return StatusResponse(status="success") 
        # else: 
            # return StatusResponse(status="fail") 
        # В этом примере всегда возвращаем успех 
        return SAddFriend(status="success") 
    except Exception as e: 
        return SAddFriend(status="fail")