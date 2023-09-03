from typing import Optional, List

from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse

from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from services.movie import MovieService

movie_router = APIRouter()


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200,
                  dependencies=[Depends(JWTBearer())])
def get_movies() -> JSONResponse:
    db = Session()
    response = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    response = MovieService(db).get_movie(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> JSONResponse:
    db = Session()
    response = MovieService(db).get_movies_by_category(category)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado películas con esa categoría"})

    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> JSONResponse:
    db = Session()
    new_movie = MovieModel(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> JSONResponse:
    db = Session()
    response = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    # Update movie
    response.title = movie.title
    response.overview = movie.overview
    response.year = movie.year
    response.rating = movie.rating
    response.category = movie.category

    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha actualizado la película"})


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> JSONResponse:
    db = Session()
    response = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    # Delete movie
    db.delete(response)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
