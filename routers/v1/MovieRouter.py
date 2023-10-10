from typing import List, Optional

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from schemes.pydantic.MovieSchema import MovieSchema
from services.MovieService import MovieService

MovieRouter = APIRouter(
    prefix="/v1/movies", tags=["movies"]
)


@MovieRouter.get("", response_model=List[MovieSchema], status_code=status.HTTP_200_OK,
                 summary="Listado de películas",
                 description="Obtiene un listado de películas, opcionalmente se puede filtrar por categoría")
def index(
        category: Optional[str] = None,
        movie_service: MovieService = Depends()
):
    return movie_service.list(category)


@MovieRouter.get("/{id}", response_model=MovieSchema)
def get(
        id: int,
        movie_service: MovieService = Depends()
) -> JSONResponse:
    response = movie_service.get(id)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return response


@MovieRouter.post("/", response_model=MovieSchema, status_code=status.HTTP_201_CREATED)
def create(
        movie: MovieSchema,
        movie_service: MovieService = Depends()
) -> JSONResponse:
    response = movie_service.create(movie)

    if not response:
        return JSONResponse(status_code=404, content={"message": "No se ha encontrado la película"})

    return response


@MovieRouter.put("/{id}", response_model=MovieSchema)
def update(
        id: int, movie: MovieSchema,
        movie_service: MovieService = Depends()
) -> JSONResponse:
    response = movie_service.update(id, movie)

    if not response:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "No se ha encontrado la película"})

    return response


@MovieRouter.delete("/{id}", response_model=MovieSchema)
def delete(
        id: int,
        movie_service: MovieService = Depends()
) -> JSONResponse:
    response = movie_service.delete(id)

    if not response:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": "No se ha encontrado la película"})

    return response
