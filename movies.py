from fastapi import APIRouter,HTTPException
from model import Movie

router = APIRouter(prefix="/movies")

movies_list = {
  1: {
    "title": "The Shawshank Redemption",
    "director": "Frank Darabont",
    "genre": "Drama",
    "rating": 9.3,
    "release_year": 1994
  },
  2: {
    "title": "Inception",
    "director": "Christopher Nolan",
    "genre": "Science Fiction",
    "rating": 8.8,
    "release_year": 2010
  },
  3: {
    "title": "The Dark Knight",
    "director": "Christopher Nolan",
    "genre": "Action",
    "rating": 9.0,
    "release_year": 2008
  },
  4: {
    "title": "Parasite",
    "director": "Bong Joon-ho",
    "genre": "Thriller",
    "rating": 8.5,
    "release_year": 2019
  },
  5: {
    "title": "Pulp Fiction",
    "director": "Quentin Tarantino",
    "genre": "Crime",
    "rating": 8.9,
    "release_year": 1994
  }
}

#search by title
@router.get("/{movie_title}")
def get_movie(movie_title:str):
  x = len(movies_list)
  for i in range(1,x+1):
    if movies_list[i]["title"]== movie_title:
      mov = movies_list[i]
      return {"movie found details": mov}
    
    
#search by genre
@router.get("/movie/{movie_genre}")
def get_movie(movie_genre:str):
  x = len(movies_list)
  for i in range(1,x+1):
    if movies_list[i]["genre"].lower() == movie_genre.lower():
      mov = movies_list[i]
      return {"movie found details": mov}

 
  
  
#search by movie_id
@router.get("/mov/{movie_id}")
def get_movie(movie_id: int):
    mov = movies_list.get(movie_id)
    return {"movie_id": movie_id, "details": mov}
#add a movie
@router.post("/")
def add_movie(m : Movie):
  n = len(movies_list)
  movies_list[n+1]= m.dict()
  return {"message":"movie added","movie":m}
  