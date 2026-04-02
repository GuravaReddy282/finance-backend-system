from fastapi import FastAPI
from database import Base, engine
from routes import transactions
from models import Transaction

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions.router)

@app.get("/")
def home():
    return {"message": "Finance Backend Running"}