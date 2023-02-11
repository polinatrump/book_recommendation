import abc
from src.repository.base_repository import AbstractRepository


class AbstractUseCase(abc.ABC):
    repository: AbstractRepository

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError