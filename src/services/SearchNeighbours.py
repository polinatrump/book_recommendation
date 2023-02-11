import multiprocessing
import operator
from typing import List
from scipy import spatial
from src.domain import Book
from src.usecases.base_usecase import AbstractUseCase


class SearchNeighboursService:

    @classmethod
    def get_neighbors(
            cls,
            target_book: Book,
            neighbors_count: int,
            books: List[Book],
    ):
        """
        Method to find K neighbours books
        :param target_book: 
        :param neighbors_count:
        :param books:
        :return: 
        """
        distances = []
        for book in books:
            dist = cls.calculate_distance_between_books(target_book, book)
            distances.append([dist, book])
            distances.sort(key=lambda x : x[0])
            if len(distances) > neighbors_count:
                distances.pop(-1)
        results = [[i[0], i[1].title, i[1].authors[0].name, i[1].id] for i in distances]
        return results

    @classmethod
    def calculate_distance_between_books(
            cls,
            book1: Book,
            book2: Book
    ) -> float:
        """
        Method for calculating distances between books
        :param book1: 
        :param book2: 
        :return: 
        """
        genres_a = [int(i) for i in book1.genres_bin.split(',')]
        genres_b = [int(i) for i in book2.genres_bin.split(',')]
        # считаем дистанцию между книгами по жанру
        genre_distance = spatial.distance.cosine(genres_a, genres_b)
        # print('dist', genre_distance)
        author_a = [int(i) for i in book1.authors_bin.split(',')]
        author_b = [int(i) for i in book2.authors_bin.split(',')]

        # считаем дистанцию между книгами по автору
        author_distance = spatial.distance.cosine(author_a, author_b)
        # print('dist', author_distance)
        # if not genre_distance or not author_distance:
        #     return 3.0  # типа самая большая дистанция - книги вообще не похожи
        # else:
        # print(genre_distance + author_distance)
        return genre_distance + author_distance  # общая дистанция
        # except:
        #     return 3.0

    @classmethod
    def process_batches_in_separate_processes(
            cls,
            batches

    ):
        results = []
        with multiprocessing.Pool(6) as pool:
            for result in pool.starmap(SearchNeighboursService.get_neighbors, batches):
                results += result
        results.sort(key=operator.itemgetter(0))
        return results

    @classmethod
    def create_batches_as_input_arguments(
            cls,
            count_of_recomendations: int,
            book: Book,
            book_list_usecase: AbstractUseCase,
            batch_size: int = 5000,
    ):
        args = []
        for i in range(0, 51000, batch_size):
            books = book_list_usecase(limit=batch_size, offset=i)
            args.append((book, count_of_recomendations, books))
        return args

    @classmethod
    def delete_dublicates_in_results(
            cls,
            results
    ):
        results_book_dublicate_delete = []
        unique_book_names = []
        for item in results[1:]:
            if item[1] not in unique_book_names:
                unique_book_names.append(item[1])
                results_book_dublicate_delete.append(item)
        return results_book_dublicate_delete

    @classmethod
    def limit_same_authors_in_results(
            cls,
            results
    ):
        same_author_offset = 3
        dict_author_times_in_results = {}
        processed_results = []
        for item in results:
            if item[2] not in dict_author_times_in_results.keys():
                dict_author_times_in_results[item[2]] = 0
            if dict_author_times_in_results[item[2]] < same_author_offset:
                dict_author_times_in_results[item[2]] += 1
                processed_results.append(item)
        return processed_results
