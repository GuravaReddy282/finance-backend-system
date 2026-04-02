from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

router = APIRouter(prefix="/transactions", tags=["Transactions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, data)


@router.get("/", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db, transaction_id)