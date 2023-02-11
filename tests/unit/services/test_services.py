from typing import NoReturn
from src.domain import Book
from src.services.SearchNeighbours import SearchNeighboursService


class TestSimilarity:

    def test_get_neighbors_returns_same_quantity_as_param(
            self,
            create_book_domain_model_with_params
    ) -> NoReturn:
        book = create_book_domain_model_with_params
        books = [book for i in range(0,10)]
        result = SearchNeighboursService.get_neighbors(book,3,books)
        assert len(result) == 3

    def test_empty_result_for_empty_book_list(
            self,
            create_book_domain_model_with_params
    ) -> NoReturn:
        book = create_book_domain_model_with_params
        result = SearchNeighboursService.get_neighbors(book,3,[])
        assert result == []

    def test_get_neighbors_returns_most_similar_books(
            self,
            create_genre_domain_model,
            create_author_domain_model
    ):
        book1 = Book(
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
        book2 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='True one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,1,1',
            authors_bin='1,0,1,1',
        )
        book3 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='False one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,0,1',
            authors_bin='1,0,0,1',
        )

        result = SearchNeighboursService.get_neighbors(book1,1,  [book3, book2])
        assert result[0][1] == 'True one'

    def test_distance_returns_zero_for_same_obj(
            self,
            create_book_domain_model_with_params
    ):
        book1 = create_book_domain_model_with_params
        book2 = create_book_domain_model_with_params

        result = SearchNeighboursService.calculate_distance_between_books(book1, book2)
        assert result == 0

    def test_distance_returns_not_zero_for_different_objects(
            self,
            create_genre_domain_model,
            create_author_domain_model
    ):
        book1 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='True one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,1,1',
            authors_bin='1,0,1,1',
        )
        book2 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='False one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,0,1',
            authors_bin='1,0,0,1',
        )

        result = SearchNeighboursService.calculate_distance_between_books(book1, book2)

        assert result > 0

    def test_independent_results_for_permutation(
            self,
            create_genre_domain_model,
            create_author_domain_model
    ):
        book1 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='True one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,1,1',
            authors_bin='1,0,1,1',
        )
        book2 = Book(
            id=1,
            authors=[create_author_domain_model],
            rating=1.0,
            rating_count=1,
            review_count=1,
            title='False one',
            genres=[create_genre_domain_model],
            image_url='https://example.org',
            genres_bin='1,0,0,1',
            authors_bin='1,0,0,1',
        )

        result1 = SearchNeighboursService.calculate_distance_between_books(book1, book2)
        result2 = SearchNeighboursService.calculate_distance_between_books(book2, book1)

        assert result1 == result2

    def test_process_batches_returns_empty_for_empty_list(self):
        result = SearchNeighboursService.process_batches_in_separate_processes([])
        assert [] == result


