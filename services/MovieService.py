from typing import Optional, List

from fastapi import Depends

from models.MovieModel import Movie
from repositories.MovieRepository import MovieRepository
from schemes.pydantic.MovieSchema import MovieSchema


class MovieService:
    movieRepository: MovieRepository

    def __init__(
            self, movie_repository: MovieRepository = Depends()
    ) -> None:
        self.movieRepository = movie_repository

    def list(
            self,
            category: Optional[str] = None
    ) -> List[Movie]:
        return self.movieRepository.list(category)

    def get(self, id: int) -> Movie:
        return self.movieRepository.get(id)

    def create(self, movie_body: MovieSchema) -> Movie:
        return self.movieRepository.create(
            Movie(
                title=movie_body.title,
                overview=movie_body.overview,
                year=movie_body.year,
                rating=movie_body.rating,
                category=movie_body.category
            )
        )

    def update(self, id: int, movie_body: MovieSchema) -> Movie:
        return self.movieRepository.update(
            id,
            Movie(
                title=movie_body.title,
                overview=movie_body.overview,
                year=movie_body.year,
                rating=movie_body.rating,
                category=movie_body.category
            )
        )

    def delete(self, id: int) -> Movie:
        return self.movieRepository.delete(id)
