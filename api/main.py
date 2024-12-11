import uvicorn
from fastapi import FastAPI
from api.schemas.database import engine, Base
from api.routes.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
