from src.movie.domain.entities.movie import Movie
from src.movie.infrastructure.persistence.models import MovieModel
from src.shared.domain.singleton import SingletonMeta
from src.shared.infrastructure.database import mapper_registry


class SLQAlchemyMapper(metaclass=SingletonMeta):
    def __init__(self):
        movie_table = MovieModel.__table__

        mapper_registry.map_imperatively(
            Movie,
            movie_table,
        )
