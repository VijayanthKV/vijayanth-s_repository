
# 🗓️ Day 1 – Introduction to Databases, ORM, and SQLAlchemy Models

---

## 📌 1. What is a Database?

A **database** is a structured place to store data so it can be easily retrieved and manipulated later.

🧱 Key Concepts:
- **Table**: Like an Excel sheet (rows + columns)
- **Row (Record)**: One entry in the table
- **Column (Field)**: A specific attribute (like Name, Age)
- **Primary Key**: A unique identifier for each row

---

## 📌 2. Why SQLite?

- A simple, file-based SQL database.
- No installation/server needed.
- Perfect for beginners and small apps.

📦 SQLite DB is just a `.db` file.

---

## 📌 3. What is an ORM?

ORM = Object Relational Mapper

🔁 It connects Python classes to database tables.

Instead of writing SQL manually:
```sql
INSERT INTO users (name, age) VALUES ('Alice', 25);
```

You can do this in Python:
```python
user = User(name="Alice", age=25)
session.add(user)
session.commit()
```

ORM handles all SQL behind the scenes.

---

## 📌 4. SQLAlchemy Setup (ORM Part)

### 📁 File: `models.py`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age})>"
```

---

## 📌 5. Creating the SQLite DB

### 📁 File: `database.py`

```python
from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine)

print("Database and tables created successfully.")
```

⏺️ Run this once:
```bash
python database.py
```

You’ll see a new file `test.db` generated.

---


---

## 🎯 Learning Outcomes of Day 1

✅ Know what a database is  
✅ Know why SQLite is used  
✅ Know what ORM does  
✅ Know how SQLAlchemy represents tables as classes  
✅ Know how to create a database

---

## ✅ Next Day Prep

For Day 2:
➡️ Use the same `User` model and add another table (like `Post`)  
➡️ Perform CRUD operations.  
➡️ Learn how to define relationships (foreign keys)  
➡️ Integrate SQLAlchemy with FastAPI routes
