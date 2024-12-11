from api.schemas.models import Items, ItemBase, ItemCreate
from sqlalchemy.orm import Session
from api.schemas.schemes import UserBase, UserCreate, WalletCreate, DealCreate, TransferBase, Friend
import uuid
from api.schemas.models import User, Deal
# from api.schemas.models import Questions, Choices


def get_item(db: Session, item_id: int):
    return db.query(Items).filter(Items.id == item_id).first()

async def create_item(db: Session, item: ItemBase):
    db_item = Items(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Items).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item












def get_user(db: Session, tg_id: int):
    return db.query(User).filter(User.tg_id == tg_id).first()
    # return db.query(models.User).filter(models.User.tg_id == tg_id).first()

def create_user(db: Session, user: UserCreate):
# def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        tg_id=user.tg_id,
        ton_wallet_address=str(uuid.uuid4()),  # Генерация адреса кошелька
        tg_wallet_address=str(uuid.uuid4()),  # Генерация адреса кошелька
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
    # return db.query(models.User).filter(models.User.id == user_id).first()

def update_user_wallet(db: Session, user_id: int, wallet: WalletCreate):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db_user.tg_wallet_address = wallet.address
        db.commit()
        db.refresh(db_user)
    return db_user

def create_deal(db: Session, deal: DealCreate, user_id: int):
    db_deal = Deal(
        id=deal.id,
        currency=deal.currency,
        sum=deal.sum,
        type=deal.type,
        balance=deal.balance,
        stop_loss=deal.stop_loss,
        take_profit=deal.take_profit,
        cross=deal.cross,
        deal_in=deal.deal_in,
        owner_id=user_id,
    )
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

def update_deal(db: Session, deal_id: str, deal: DealCreate):
    db_deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if db_deal:
        db_deal.type = deal.type
        db_deal.balance = deal.balance
        db_deal.finished_at = deal.finished_at
        db.commit()
        db.refresh(db_deal)
    return db_deal

def create_transfer(db: Session, transfer: TransferBase):
    # Логика выполнения перевода средств
    return {"status": "success"}













def get_user_id(db: Session, tg_id):
    return db.query(User).filter(User.tg_id == tg_id).first()





def add_friend(db: Session, user_id: int, friend_id: int):
    user = get_user_by_id(db, user_id)
    friend = get_user_by_id(db, friend_id)
    if user and friend:
        user.friends.append(friend)
        db.commit()
        return {"status": "success"}
    return {"status": "fail"}




def check_friendship(db: Session, user_id: int, friend_id: int):
    user = get_user_by_id(db, user_id)
    friend = get_user_by_id(db, friend_id)
    if friend in user.friends:
        return True
    return False


def get_friends_or_players(db: Session, type: str, user_id: str):
    user = get_user_by_id(db, int(user_id))
    if not user:
        return []
    # Логика получения списка друзей или игроков
    if type == "friends":
        # Возвращаем список друзей
        friends = user.friends
        # friends = db.query(User).filter(User.friends.any()).all()
    elif type == "players":
        # Возвращаем список игроков
        friends = db.query(User).all()
    else:
        friends = {"message": "неизвестный тип"}

    # return friends
    result = []
    for friend in friends:
        is_friend = friend in user.friends
        result.append(Friend(full_name=f"{friend.first_name} {friend.last_name}", league=friend.league,
                                 coins=friend.ton_wallet_balance,  # Используем баланс в качестве монет
                                    avatar=friend.avatar,
                         is_friend=is_friend
                         ))
    return result
