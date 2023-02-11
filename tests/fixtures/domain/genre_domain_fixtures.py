import pytest

from src.domain.Genre import Genre


@pytest.fixture
def create_genre_domain_model():
    return Genre(
         id=1,
         name='TestGenre'
    )
