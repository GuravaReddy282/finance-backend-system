from sqlalchemy.orm import Session
from models import Transaction
from schemas import TransactionCreate


def create_transaction(db: Session, data: TransactionCreate):
    new_transaction = Transaction(**data.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def get_transactions(db: Session):
    return db.query(Transaction).all()


def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
    return transaction