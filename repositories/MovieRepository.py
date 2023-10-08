from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from config.Database import get_db_connection
from models.MovieModel import Movie


class MovieRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(self, category: Optional[str]) -> List[Movie]:
        query = self.db.query(Movie)

        if category:
            query = query.filter_by(category=category)

        return query.all()

    def get(self, id: int) -> Movie:
        query = self.db.query(Movie).filter(Movie.id == id)
        return query.first()

    def create(self, movie: Movie) -> Movie:
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def update(self, id: int, movie: Movie) -> Movie:
        movie.id = id
        self.db.merge(movie)
        self.db.commit()
        return movie

    def delete(self, id: int) -> Movie | None:
        movie = self.db.query(Movie).filter(Movie.id == id).first()

        if not movie:
            return None

        self.db.delete(movie)
        self.db.commit()
        return movie
