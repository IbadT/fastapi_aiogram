from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Boolean, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.schemas.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from datetime import datetime

#
# class Questions(Base):
#     __tablename__ = 'questions'
#
#     id = Column(Integer, primary_key=True, index=True)
#     question_text = Column(String, index=True)
#
# class Choices(Base):
#     __tablename__ = 'choices'
#
#     id = Column(Integer, primary_key=True, index=True)
#     choice_text = Column(String, index=True)
#     is_correct = Column(Boolean, default=False)
#     question_id = Column(Integer, ForeignKey('questions.id'))



# class Items(Base):
#     __tablename__ = 'items'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     description = Column(String)
#
# class ItemBase(BaseModel):
#     name: str
#     description: str
#
# class ItemCreate(ItemBase):
#     pass
#
# class Config:
#     orm_mode = True





#
# class Post(Base):
#     __tablename__ = "posts"
#
#     id = Column(Integer,primary_key=True,nullable=False, index=True)
#     title = Column(String,nullable=False)
#     content = Column(String,nullable=False)
#     published = Column(Boolean, server_default='TRUE')
#     created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
#





# Промежуточная таблица для отношения "многие ко многим"
friends_association = Table(
    'friends', Base.metadata,
    Column('user_id', Integer,
           ForeignKey('users.id')),
    Column('friend_id',
           Integer,
           ForeignKey('users.id'))
)


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    tg_id = Column(Integer, unique=True, index=True)
    ton_wallet_address = Column(String, unique=True)
    ton_wallet_balance = Column(Float, default=0.0)
    tg_wallet_address = Column(String, unique=True, nullable=True)
    tg_wallet_balance = Column(Float, default=0.0)
    avatar = Column(String, default='')
    league = Column(String, default='')
    deals = relationship("Deal", back_populates="owner")
    friends = relationship("User", secondary=friends_association, primaryjoin=id == friends_association.c.user_id,
                           secondaryjoin=id == friends_association.c.friend_id, backref="user_friends")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)






class Deal(Base):
    __tablename__ = "deals"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True, index=True)
    currency = Column(String)
    sum = Column(Float)
    type = Column(String)
    balance = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    cross = Column(Boolean)
    deal_in = Column(Float)
    finished_at = Column(Float, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="deals")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



# async def async_main():
#     async with engine.begin() as session:
#         await session.run_sync(Base.metadata.create_all)

