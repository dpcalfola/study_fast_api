import abc
import typing

from api.entities.movie import Movie


class RepositoryException(Exception):
    pass


# CRUD
class Repository(abc.ABC):
    def create_movie(self, movie: Movie):
        """
        1. Create a movie and returns true on success
        2. Raise RepositoryException of failure
        """
        raise NotImplementedError

    def get_by_id(self, movie_id: str) -> typing.Optional[Movie]:
        """
        Retrieves a movie by its ID and if the movie is not found, it returns None
        """
        raise NotImplementedError

    def get_by_title(self, movie_title: str) -> typing.Optional[Movie]:
        """
        Return a list of movies which share same title
        """
        raise NotImplementedError

    def update_movie(self, movie_id: str, update_parameter: dict):
        """
        Update a movie by its id
        """
        raise NotImplementedError

    def delete_movie(self, movie_id: str):
        """
        1. Delete a movie by its id and return true on success
        2. Raise RepositoryException of failure
        """
        raise NotImplementedError
