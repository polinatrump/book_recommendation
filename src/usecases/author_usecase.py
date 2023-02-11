from typing import NoReturn, List
from src.database.db import get_session
from src.domain import Author
from src.repository.author_repository import AuthorRepository
from src.usecases.base_usecase import AbstractUseCase


class CreateAuthorUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, **kwargs) -> Author:
        return AuthorRepository(self.session).create(**kwargs)


class DeleteAuthorUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> NoReturn:
        AuthorRepository(self.session).delete(id)


class GetAuthorByIdAuthorUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> Author:
        return AuthorRepository(self.session).get(id)


class UpdateAuthorUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> Author:
        return AuthorRepository(self.session).update(id, **kwargs)


class ListAuthorUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> List[Author]:
        return AuthorRepository(self.session).list(id, **kwargs)
