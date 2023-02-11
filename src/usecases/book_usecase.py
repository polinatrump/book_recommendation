from typing import NoReturn, List
from src.database.db import get_session
from src.domain import Book
from src.exceptions.book_exceptions import BookTitleNotFoundException
from src.repository.book_repository import BookRepository
from src.usecases.base_usecase import AbstractUseCase


class GetBookByTitleUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, *args, **kwargs) -> Book:
        book = BookRepository(self.session).get_book_by_title(*args, **kwargs)
        if book:
            return book
        raise BookTitleNotFoundException


class CreateBookUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, **kwargs) -> Book:
        return BookRepository(self.session).create(**kwargs)


class DeleteBookUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> NoReturn:
        BookRepository(self.session).delete(id)


class GetBookByIdBookUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> Book:
        return BookRepository(self.session).get(id)


class UpdateBookUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> Book:
        return BookRepository(self.session).update(id, **kwargs)


class ListBookUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, limit, offset, **kwargs) -> List[Book]:
        return BookRepository(self.session).list(limit, offset, **kwargs)

