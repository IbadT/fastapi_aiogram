from pydantic import BaseModel, RootModel
from typing import Literal, Optional, List


class SAuth(BaseModel):
    wallet: str | None

class SPlayers(BaseModel):
    fullName: str
    league: str
    coins: int
    avatar: str
    isFriend: bool

class SAddFriend(BaseModel):
    status: Literal["success", "fail"]

class SUser(BaseModel):
    id: int
    firstName: str
    lastName: str
    avatar: str



################################################################################################

class DealBase(BaseModel):
    currency: str
    sum: float
    type: str
    balance: float
    stop_loss: float
    take_profit: float
    cross: bool
    deal_in: float
    finished_at: Optional[float] = None

class DealCreate(DealBase):
    id: str
    # pass

class Deal(DealBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True
class UserBase(BaseModel):
    first_name: str
    last_name: str
    tg_id: int

class UserCreate(UserBase):
    pass

class UserBase(UserBase):
    id: int
    ton_wallet_address: str
    ton_wallet_balance: float
    tg_wallet_address: str
    tg_wallet_balance: float
    # deals: List[Deal] = []
    deals: List[Deal]

    class Config:
        # orm_mode = True
        from_attributes = True

class WalletCreate(BaseModel):
    address: str

class TransferBase(BaseModel):
    wallet_address: str
    network: str
    amount: float










class Friend(BaseModel):
    full_name: str
    league: str
    coins: float
    avatar: str
    is_friend: bool

class FriendList(BaseModel):
    # __root__: List[Friend] = []
    friends: List[Friend]

class AddFriendResponse(BaseModel):
    status: str

