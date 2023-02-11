from typing import NoReturn, List
from src.database.db import get_session
from src.domain import Genre
from src.repository.genre_repository import GenreRepository
from src.usecases.base_usecase import AbstractUseCase


class CreateGenreUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, **kwargs) -> Genre:
        return GenreRepository(self.session).create(**kwargs)


class DeleteGenreUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> NoReturn:
        GenreRepository(self.session).delete(id)


class GetGenreByIdGenreUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> Genre:
        return GenreRepository(self.session).get(id)


class UpdateGenreUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> Genre:
        return GenreRepository(self.session).update(id, **kwargs)


class ListGenreUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> List[Genre]:
        return GenreRepository(self.session).list(id, **kwargs)
