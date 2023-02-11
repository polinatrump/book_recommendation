from typing import NoReturn, List
from src.database.db import get_session
from src.domain.User import User
from src.exceptions.user_exceptions import UserLastNameFirstNameNotFoundException
from src.repository.user_repository import UserRepository
from src.usecases.base_usecase import AbstractUseCase


class UserFindByLastFirstNameUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, first_name, last_name) -> User:
        user = UserRepository(self.session).get_by_first_and_last_name(first_name, last_name)
        if user:
            return user
        raise UserLastNameFirstNameNotFoundException


class UserCreateUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, **kwargs) -> User:
        return UserRepository(self.session).create(**kwargs)


class DeleteUserUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> NoReturn:
        UserRepository(self.session).delete(id)


class GetUserByIdUserUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> User:
        return UserRepository(self.session).get(id)


class UpdateUserUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> User:
        return UserRepository(self.session).update(id, **kwargs)


class ListUserUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> List[User]:
        return UserRepository(self.session).list(id, **kwargs)
