from sqlalchemy import Column, Integer, String, Date, ARRAY
from src.shared.infrastructure.database import Base


class MovieModel(Base):
    __tablename__ = 'movie'

    id = Column(String, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rated = Column(String)
    released = Column(Date)
    runtime = Column(Integer)
    genre = Column(ARRAY(String))
    director = Column(String)
    writer = Column(ARRAY(String))
    actors = Column(ARRAY(String))
    plot = Column(String)

