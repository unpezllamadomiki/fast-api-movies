from datetime import date
from typing import List, Optional


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



