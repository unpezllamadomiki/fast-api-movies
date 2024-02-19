from typing import List

from sqlalchemy.orm import Session
from src.movie.domain.entities.movie import Movie
from src.movie.domain.repositories.movie_repository import IMovieRepository
from src.movie.infrastructure.persistence.models import MovieModel


class SQLAlchemyMovieRepository(IMovieRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create(self, movie: Movie) -> Movie:
        movie_data = MovieModel(
            id=movie.id,
            title=movie.title,
            year=movie.year,
            rated=movie.rated,
            released=movie.released,
            runtime=movie.runtime,
            genre=movie.genre,
            director=movie.director,
            writer=movie.writer,
            actors=movie.actors,
            plot=movie.plot
        )
        self.session.add(movie_data)
        self.session.commit()
        return movie

    async def update(self, movie: Movie) -> Movie:
        movie_data = self.session.query(MovieModel).filter_by(id=movie.id).first()
        if movie_data:
            movie_data.title = movie.title
            movie_data.year = movie.year
            movie_data.rated = movie.rated
            movie_data.released = movie.released
            movie_data.runtime = movie.runtime
            movie_data.genre = movie.genre
            movie_data.director = movie.director
            movie_data.writer = movie.writer
            movie_data.actors = movie.actors
            movie_data.plot = movie.plot
            self.session.commit()
            return movie
        else:
            raise ValueError(f"Movie with ID {movie.id} was not found.")

    async def delete(self, movie_id: str) -> bool:
        movie_data = self.session.query(MovieModel).filter_by(id=movie_id).first()
        if movie_data:
            self.session.delete(movie_data)
            self.session.commit()
            return True
        else:
            raise ValueError(f"Movie with ID {movie_id} was not found.")

    async def get_by_id(self, movie_id: str) -> Movie:
        movie_data = self.session.query(MovieModel).filter_by(id=movie_id).first()
        if movie_data:
            return Movie(
                id=movie_data.id,
                title=movie_data.title,
                year=movie_data.year,
                rated=movie_data.rated,
                released=movie_data.released,
                runtime=movie_data.runtime,
                genre=movie_data.genre,
                director=movie_data.director,
                writer=movie_data.writer,
                actors=movie_data.actors,
                plot=movie_data.plot
            )
        else:
            raise ValueError(f"Movie with ID {movie_id} was not found.")

    async def get_by_title(self, title: str) -> Movie:
        movie_data = self.session.query(MovieModel).filter_by(title=title).first()
        if movie_data:
            return Movie(
                id=movie_data.id,
                title=movie_data.title,
                year=movie_data.year,
                rated=movie_data.rated,
                released=movie_data.released,
                runtime=movie_data.runtime,
                genre=movie_data.genre,
                director=movie_data.director,
                writer=movie_data.writer,
                actors=movie_data.actors,
                plot=movie_data.plot
            )
        else:
            raise ValueError(f"No movie with title '{title}' was found in the database.")

    async def get_all(self, limit: int = 10, offset: int = 0) -> List[Movie]:
        movie_data = self.session.query(MovieModel).offset(offset).limit(limit).all()
        if movie_data:
            return [
                Movie(
                    id=movie.id,
                    title=movie.title,
                    year=movie.year,
                    rated=movie.rated,
                    released=movie.released,
                    runtime=movie.runtime,
                    genre=movie.genre,
                    director=movie.director,
                    writer=movie.writer,
                    actors=movie.actors,
                    plot=movie.plot
                )
                for movie in movie_data
            ]
        else:
            raise ValueError("No movies were found in the database.")
