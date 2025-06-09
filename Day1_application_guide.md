# FastAPI + SQLAlchemy Minimal Project Setup Guide

This guide walks you through setting up a minimal FastAPI project using SQLAlchemy with a SQLite database.

---

## 📦 Project Structure

```
project/
├── app.py
├── database.py
├── models.py
└── requirements.txt
```

---

## 🧾 `requirements.txt`

List of Python dependencies required to run the project:

```
sqlalchemy
fastapi
uvicorn
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧱 `models.py`

This file defines the data models using SQLAlchemy ORM. Here’s a sample `User` model:

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
```

- `__tablename__` tells SQLAlchemy to use `users` table.
- `id`, `name`, `email`, `hashed_password` are columns in the table.
- `Base` is inherited from `database.py`.

---

## 🛢️ `database.py`

This file handles the database connection setup and session management:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Key Points:

- Uses SQLite database file named `test.db`.
- `get_db()` provides a database session to use with FastAPI's dependency injection.
- `Base` is the declarative base class for all models.

---

## 🚀 `app.py`

Main FastAPI application entry point:

```python
from fastapi import FastAPI, Depends
import uvicorn
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
```

### Explanation:

- `models.Base.metadata.create_all(...)`: Creates tables in DB based on defined models.
- `/` endpoint returns a simple JSON response.

---

## 🛠️ Setup and Run

### 1. 📁 Make sure your files are structured as shown.

### 2. ✅ Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. ▶️ Run the FastAPI server:

```bash
python app.py
```

Server will be live at: [http://localhost:8000](http://localhost:8000)

To test the API, visit:  
`http://localhost:8000/` → should return `{"Hello": "World"}`


and the "test.db" will be created locally

---

---


