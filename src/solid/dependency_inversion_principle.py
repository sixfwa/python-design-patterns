"""
Dependency Inversion Principle

A.  High-level modules should not depend on low-level modules. 
    Both should depend on abstractions (e.g., interfaces).

B.  Abstractions should not depend on details. 
    Details (concrete implementations) should depend on abstractions.

High-level classes shouldn’t have to change just because low-level classes change.
"""
from enum import Enum
from abc import abstractmethod


class Genre(Enum):
    HORROR = "HORROR"
    DRAMA = "DRAMA"
    ANIMATION = "ANIMATION"


class Movie:
    def __init__(self, title: str):
        self.title = title


class Catalogue:
    @abstractmethod
    def find_by_genre(self, genre: Genre):
        pass


class SeriesCatalogue(Catalogue):
    def find_by_genre(self, genre: Genre):
        pass


class MovieCatalogue(Catalogue):
    """
    Low Level Class
    """

    def __init__(self):
        self.movies = list()

    def add_movie(self, movie: Movie, genre: Genre):
        self.movies.append((movie, genre))

    def find_by_genre(self, genre: Genre):
        for movie in self.movies:
            if movie[1] == genre:
                yield f"{movie[0].title} is a {genre.value} movie"


class Netflix:
    """
    High Level Class
    """

    def __init__(self, catalogue: Catalogue, genre: Genre):
        for movie in catalogue.find_by_genre(genre):
            print(movie)


if __name__ == "__main__":
    the_godfather = Movie("The Godfather")
    pulp_fiction = Movie("Pulp Fiction")
    toy_story = Movie("Toy Story")
    sinister = Movie("Sinister")

    movie_catalogue = MovieCatalogue()
    movie_catalogue.add_movie(the_godfather, Genre.DRAMA)
    movie_catalogue.add_movie(pulp_fiction, Genre.DRAMA)
    movie_catalogue.add_movie(toy_story, Genre.ANIMATION)
    movie_catalogue.add_movie(sinister, Genre.HORROR)

    Netflix(movie_catalogue, Genre.DRAMA)