from datetime import date
from typing import List, Optional, Dict


class Movie:
    def __init__(self, id: str, title: Optional[str] = None,
                 year: Optional[int] = None, rated: Optional[str] = None, released: Optional[date] = None,
                 runtime: Optional[int] = None, genre: Optional[List[str]] = None, director: Optional[str] = None,
                 writer: Optional[List[str]] = None, actors: Optional[List[str]] = None, plot: Optional[str] = None):
        self.id = id
        self.title = title,
        self.year = year,
        self.rated = rated,
        self.released = released,
        self.runtime = runtime,
        self.genre = genre
        self.director = director
        self.writer = writer
        self.actors = actors,
        self.plot = plot

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "rated": self.rated,
            "released": self.released,
            "runtime": self.runtime,
            "genre": self.genre,
            "director": self.director,
            "writer": self.writer,
            "actors": self.actors,
            "plot": self.plot
        }



