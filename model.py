from pydantic import BaseModel
class Movie(BaseModel):
    title:str
    director :str
    genre: str
    rating: float
    released_year:int