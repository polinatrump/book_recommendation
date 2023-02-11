import pytest

from src.domain import Book, Author


@pytest.fixture
def create_book_domain_model(
        create_author_domain_model,
        create_genre_domain_model
):
    return Book(
        id=1,
        authors=[create_author_domain_model],
        rating=1.0,
        rating_count=1,
        review_count=1,
        title='Test',
        genres=[create_genre_domain_model],
        image_url='https://example.org',
        genres_bin='1,0,1,1',
        authors_bin='1,0,1,1',
    )


@pytest.fixture
def create_book_domain_model_with_params(
        id=1,
        authors=[Author(id=1, name = "Suzanne Collins")],
        rating=1.0,
        rating_count=1,
        review_count=1,
        title='',
        genres=None,
        image_url='https://example.org',
        genres_bin='1,0,1,1',
        authors_bin='1,0,1,1',
):
    return Book(
        id=id,
        authors=authors,
        rating=rating,
        rating_count=rating_count,
        review_count=review_count,
        title=title,
        genres=genres,
        image_url=image_url,
        genres_bin=genres_bin,
        authors_bin=authors_bin,
    )