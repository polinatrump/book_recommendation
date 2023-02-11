from typing import NoReturn, List
from src.database.db import get_session
from src.domain.Recommendation import Recommendation
from src.repository.recommendation_repository import RecommendationRepository
from src.usecases.base_usecase import AbstractUseCase


class CreateRecommendationUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, **kwargs) -> Recommendation:
        return RecommendationRepository(self.session).create(**kwargs)


class DeleteRecommendationUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> NoReturn:
        RecommendationRepository(self.session).delete(id)


class GetRecommendationByIdRecommendationUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int) -> Recommendation:
        return RecommendationRepository(self.session).get(id)


class UpdateRecommendationUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> Recommendation:
        return RecommendationRepository(self.session).update(id, **kwargs)


class ListRecommendationUseCase(AbstractUseCase):

    def __init__(
            self,
            repository
    ) -> NoReturn:
        self.repository = repository
        self.session = get_session()

    def __call__(self, id: int, **kwargs) -> List[Recommendation]:
        return RecommendationRepository(self.session).list(id, **kwargs)
