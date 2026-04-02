\# Finance Backend System



\## Overview

This project is a Python-based Finance Tracking Backend System built using FastAPI and SQLite.



\## Features

\- Create transactions

\- View transactions

\- Delete transactions

\- Summary (income, expense, balance)



\## Tech Stack

\- Python

\- FastAPI

\- SQLite

\- SQLAlchemy



\## How to Run



pip install fastapi uvicorn sqlalchemy



uvicorn main:app --reload



Open:

http://127.0.0.1:8000/docs



\## API Endpoints

\- POST /transactions

\- GET /transactions

\- DELETE /transactions/{id}

\- GET /transactions/summary



\## 📊 Sample Output
Example summary response:



{

&#x20; "total\_income": 1000,

&#x20; "total\_expense": 200,

&#x20; "balance": 800

}

##  Running Locally

To run this project locally:

1. Install dependencies:
pip install fastapi uvicorn sqlalchemy

2. Run the server:
uvicorn main:app --reload

3. Open in browser:
http://127.0.0.1:8000/docs

