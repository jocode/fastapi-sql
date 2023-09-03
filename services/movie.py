from models.movie import Movie as MovieModel


class MovieService:

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        response = self.db.query(MovieModel).all()
        return response

    def get_movie(self, id: int):
        response = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return response

    def get_movies_by_category(self, category: str):
        response = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return response
