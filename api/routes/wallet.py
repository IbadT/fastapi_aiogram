# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from .. import models, schemas, database
#
# router = APIRouter()
#
# @router.post("/wallet", response_model=schemas.User)
# def connect_wallet(wallet: schemas.WalletCreate, db: Session = Depends(database.get_db)):
#     db_wallet = db.query(models.User).filter(models.User.tg_wallet_address == wallet.address).first()
#     if db_wallet:
#         raise HTTPException(status_code=400, detail="Wallet already exists")
#     db_user.tg_wallet_address = wallet.address
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
