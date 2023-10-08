from typing import List

from fastapi import APIRouter, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from config.Database import SessionLocal
from middlewares.jwt_bearer import JWTBearer
from schemes.movie import Movie
from services.MovieService import MovieService

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200,
                  dependencies=[Depends(JWTBearer())])
def get_movies() -> JSONResponse:
    db = SessionLocal()
    response = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = SessionLocal()
    response = MovieService(db).get_movie(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> JSONResponse:
    db = SessionLocal()
    response = MovieService(db).get_movies_by_category(category)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado películas con esa categoría"})

    return JSONResponse(status_code=200, content=jsonable_encoder(response))


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> JSONResponse:
    db = SessionLocal()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> JSONResponse:
    db = SessionLocal()
    response = MovieService(db).update_movie(id, movie)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return JSONResponse(status_code=200, content={"message": "Se ha actualizado la película"})


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> JSONResponse:
    db = SessionLocal()
    response = MovieService(db).delete_movie(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
