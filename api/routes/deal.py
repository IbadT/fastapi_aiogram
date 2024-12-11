# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from .. import models, schemas, database
#
# router = APIRouter()
#
# @router.post("/deal", response_model=schemas.Deal)
# def manage_deal(deal: schemas.DealCreate, db: Session = Depends(database.get_db)):
#     db_deal = models.Deal(**deal.dict())
#     db.add(db_deal)
#     db.commit()
#     db.refresh(db_deal)
#     return db_deal
