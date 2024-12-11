import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
# from .routes.router import router as my_router
from typing import List, Annotated
# from .schemas.database import engine, Base
# from schemas.database import engine
# from schemas import models
# import api.schemas.models as models
from api.schemas.models import Questions, Choices
from api.schemas.database import engine, Base, get_db
# from api.schemas.database import SessionLocal, engine, Base, get_db
from sqlalchemy.orm import Session
from . import crud
# from api.schemas.schemes import Item, ItemCreate
# from api.schemas.models import Item, ItemCreate
from api.schemas.models import Items
from api.routes.routes import router

# from .routes import auth, wallet, deal, transfer, auto_close

app = FastAPI()

Base.metadata.create_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/questions')
async def get_questions(db: db_dependency):
    return db.query(Questions).all()


@app.get('/questions/:id')
def get_item(db: db_dependency, item_id: int):
    return db.query(Items).filter(Items.id == item_id).first()


# @app.get("/items/", response_model=list[Items])
@app.get("/items/")
def read_items(db: db_dependency, skip: int = 0, limit: int = 10):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# @app.get("/items/{item_id}", response_model=Items)
@app.get("/items/{item_id}")
def read_item(item_id: int, db: db_dependency):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.post('/questions')
async def create_question(question: QuestionBase, db: db_dependency):
# async def get_question(question: QuestionBase, db: Session = Depends(get_db)):
    db_question = Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        # db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct)
        db_choice = Choices(choice_text=choice.choice_text, is_correct=choice.is_correct)
        db.add(db_choice)
    db.commit()


# @app.post("/items/", response_model=Items)
@app.post('/items')
async def create_item(item: ItemBase, db: db_dependency):
    return await crud.create_item(db=db, item=item)






# @app.put("/items/{item_id}", response_model=Item)
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: ItemCreate, db: db_dependency):
    db_item = crud.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# @app.delete("/items/{item_id}", response_model=Item)
@app.delete('/items/{item_id}')
async def delete_item(item_id: int, db: db_dependency):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
























app.include_router(router)

# app.include_router(auth.router, prefix="/api")
# app.include_router(wallet.router, prefix="/api")
# app.include_router(deal.router, prefix="/api")
# app.include_router(transfer.router, prefix="/api")
# app.include_router(auto_close.router)




# @app.post("/webhook")
# async def telegram_webhook(request: Request):
#     id = 1
#     response = request.get(f'http://217.114.7.9:8000/users/{id}/balance')
#     # data = await request.json(f'http://217.114.7.9:8000/users/{id}/balance')
#     # return data
#     return response
#     # Обработка данных от Telegram
#     return {"status": "ok"}


if __name__ == '__main__':
    # uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
