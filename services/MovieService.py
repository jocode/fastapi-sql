from schemes.movie import Movie


class MovieService:

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        response = self.db.query(Movie).all()
        return response

    def get_movie(self, id: int):
        response = self.db.query(Movie).filter(Movie.id == id).first()
        return response

    def get_movies_by_category(self, category: str):
        response = self.db.query(Movie).filter(Movie.category == category).all()
        return response

    def create_movie(self, movie: Movie):
        new_movie = Movie(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return movie

    def update_movie(self, id: int, movie: Movie):
        response = self.db.query(Movie).filter(Movie.id == id).first()
        if not response:
            return None

        # Update movie
        response.title = movie.title
        response.overview = movie.overview
        response.year = movie.year
        response.rating = movie.rating
        response.category = movie.category

        self.db.commit()
        return movie

    def delete_movie(self, id: int):
        response = self.db.query(Movie).filter(Movie.id == id).first()
        if not response:
            return None

        self.db.delete(response)
        self.db.commit()
        return response
