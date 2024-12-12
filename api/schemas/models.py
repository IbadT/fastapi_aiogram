from sqlalchemy import Float, Boolean, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api.schemas.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from datetime import datetime


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
