from fastapi import FastAPI, Depends
import uvicorn
from database import engine
import models

#this creates all the models based on the models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
