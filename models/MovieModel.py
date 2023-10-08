from sqlalchemy import Column, Integer, String, Float

from models.BaseModel import EntityMeta


class Movie(EntityMeta):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
