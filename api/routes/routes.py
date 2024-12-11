from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import crud
# from api.schemas.schemes import User, Deal, Transfer, UserCreate, WalletCreate, DealCreate
# from api.schemas.models import User
from api.schemas.schemes import UserBase, Deal, TransferBase, UserCreate, WalletCreate, DealCreate, FriendList, \
    AddFriendResponse
from api.schemas.database import get_db
from typing import Annotated
# from api.main import db_dependency

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

# @router.post("/auth", response_model=User)
@router.post("/auth")
async def auth_user(user: UserCreate, db: db_dependency):
# async def auth_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, tg_id=user.tg_id)
    if db_user is None:
        db_user = crud.create_user(db=db, user=user)
    # return db_user
    return {
        'wallet': db_user.ton_wallet_address
    }

# @router.post("/wallet", response_model=User)
@router.post("/wallet")
def connect_wallet(wallet: WalletCreate, user_id: int, db: db_dependency):
# def connect_wallet(wallet: WalletCreate, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.update_user_wallet(db, user_id=user_id, wallet=wallet)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# @router.post("/deal", response_model=Deal)
@router.post("/deal")
def manage_deal(deal: DealCreate, user_id: int, db: db_dependency):
# def manage_deal(deal: DealCreate, user_id: int, db: Session = Depends(get_db)):
    db_deal = crud.create_deal(db, deal=deal, user_id=user_id)
    return db_deal

# @router.post("/transfer", response_model=Transfer)
@router.post("/transfer")
def transfer_funds(transfer: TransferBase, db: db_dependency):
# def transfer_funds(transfer: TransferBase, db: Session = Depends(get_db)):
    result = crud.create_transfer(db, transfer=transfer)
    return result











# @router.get("/players", response_model=schemas.FriendList)
@router.get("/players")
def get_players(type: str, user_id: str, db: db_dependency):
    # friends_or_players = crud.get_friends_or_players(db, type=type)
    # return friends_or_players
    friends_or_players = crud.get_friends_or_players(db, type=type, user_id=user_id)
    return friends_or_players



# @router.get("/add_friend", response_model=schemas.AddFriendResponse)
@router.get("/add_friend", response_model=AddFriendResponse)
def add_friend(id: int, friend_id: int, db: db_dependency):
    result = crud.add_friend(db, user_id=id, friend_id=friend_id)
    return result


@router.get('/user-tg-id')
def get_user_id(tg_id: str, db: db_dependency):
    return crud.get_user_id(db, tg_id)




@router.get("/add_friend", response_model=AddFriendResponse)
def add_friend(id: int, friend_id: int, db: db_dependency):
    result = crud.add_friend(db, user_id=id, friend_id=friend_id)
    return result

@router.get("/check_friendship", response_model=bool)
def check_friendship(id: int, friend_id: int, db: db_dependency):
    result = crud.check_friendship(db, user_id=id, friend_id=friend_id)
    return result
