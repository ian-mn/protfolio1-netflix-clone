from datetime import date
from uuid import UUID

from pydantic import BaseModel, HttpUrl, validator
from queries.modified import modified_genres, modified_movies, modified_persons


class IdName(BaseModel):
    id: UUID
    name: str


class Movie(BaseModel):
    __query__ = modified_movies
    __index__ = "movies"

    id: UUID
    rating: float
    title: str
    description: str | None
    creation_date: date
    image_url: HttpUrl
    persons: list[IdName]
    genres: list[IdName]


class Genre(BaseModel):
    __query__ = modified_genres
    __index__ = "genres"

    id: UUID
    name: str
    rating: float


class Person(BaseModel):
    __query__ = modified_persons
    __index__ = "persons"
    id: UUID
    full_name: str
    image_url: HttpUrl
    rating: float


models = [Movie, Genre, Person]
