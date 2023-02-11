import pytest

from src.domain.Recommendation import Recommendation


@pytest.fixture
def create_recommendation_domain_model():
    return Recommendation(
         id=1,
         book_id=1,
         user_id=1
    )
