from typing import List, Optional

from fastapi import APIRouter

from schemes.movie import Movie

MovieRouter = APIRouter(
    prefix="/v1/movies", tags=["movies"]
)


@MovieRouter.get("/", response_model=List[Movie])
def index(
        name: Optional[str] = None,
):
    pass
