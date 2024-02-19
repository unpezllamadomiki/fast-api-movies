from abc import abstractmethod
from typing import List, Optional, Protocol

from domain.entities.movie import Movie


class MovieRepository(Protocol):
    @abstractmethod
    def create(self, movie: Movie) -> Movie:
        raise NotImplementedError

    @abstractmethod
    def update(self, movie: Movie) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, movie_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, movie_id: str) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def get_by_title(self, title: str) -> Optional[Movie]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self, limit: int = 10, offset: int = 0) -> List[Movie]:
        raise NotImplementedError