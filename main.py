from fastapi import FastAPI
import root
import movies

app = FastAPI()

app.include_router(root.router)
app.include_router(movies.router)