from abc import abstractmethod
from typing import List, Optional, Protocol

from src.movie.domain.entities.movie import Movie


class IMovieRepository(Protocol):
    @abstractmethod
    async def create(self, movie: Movie) -> Movie:
        ...

    @abstractmethod
    async def update(self, movie: Movie) -> Optional[Movie]:
        ...

    @abstractmethod
    async def delete(self, movie_id: str) -> bool:
        ...

    @abstractmethod
    async def get_by_id(self, movie_id: str) -> Optional[Movie]:
        ...

    @abstractmethod
    async def get_by_title(self, title: str) -> Optional[Movie]:
        ...

    @abstractmethod
    async def get_all(self, limit: int = 10, offset: int = 0) -> List[Movie]:
        ...
