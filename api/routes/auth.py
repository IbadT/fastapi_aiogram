# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# # from .. import models, schemas, database
#
# router = APIRouter()
#
# @router.post("/auth", response_model=schemas.User)
# def auth_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
#     db_user = db.query(models.User).filter(models.User.tg_id == user.tg_id).first()
#     if db_user:
#         return db_user
#     ton_wallet_address = "generated_ton_wallet_address"  # Генерация TON кошелька
#     db_user = models.User(first_name=user.first_name, last_name=user.last_name, tg_id=user.tg_id,
#                           ton_wallet_address=ton_wallet_address, tg_wallet_address="")
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
