from fastapi import APIRouter

router = APIRouter()

# welcome end point
@router.get("/")
def read_root():
    return {"meassage":"Welcome to movie catalog API"}

