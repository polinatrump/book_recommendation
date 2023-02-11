import pytest

from src.domain.Author import Author


@pytest.fixture
def create_author_domain_model():
    return Author(
         id=1,
         name='TestAuthor'
    )
