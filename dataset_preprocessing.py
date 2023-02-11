import pandas as pd
from threading import Thread
import matplotlib as plt

from src.database.db import get_session
from src.models import GenreDatabaseModel, AuthorDatabaseModel
from src.repository.author_repository import AuthorRepository
from src.repository.book_repository import BookRepository
from src.repository.genre_repository import GenreRepository


class Binary:
    def __init__(self):
        self.i = 0

    def genre_binary(self, book_genre_list, all_genres_list):
        binary_list = []
        if type(book_genre_list) == list:
            for genre in all_genres_list:
                if genre in book_genre_list:
                    binary_list.append(1)
                else:
                    binary_list.append(0)
            return binary_list
        else:
            return None

    def binary_authors(self, authors, authors_indx_dict):
        self.i = self.i + 1
        print(self.i)
        binary_list = [0] * len(authors_indx_dict)
        threads = [None] * len(authors)
        print(threads)
        for author_index in range(len(authors)):
            threads[author_index] = Thread(target=self.search_author, args=(authors[author_index], binary_list, authors_indx_dict))
            threads[author_index].start()
        for i in threads:
            i.join()
        return binary_list

    def search_author(self, author, binary_list, authors_indx_dict):
        if author:
            author_value = authors_indx_dict.get(author)
            if author_value:
                binary_list[author_value] = 1


def read_ds(filename):
    return pd.read_csv(filename)


def delete_unused_columns(full_books_table):
    return full_books_table.drop(['book_edition', 'book_format', 'book_isbn', 'book_pages', 'book_desc'], axis=1)


def column_values_split(books, column_name):
    books[column_name] = books[column_name].str.split('|')
    return books


def each_book_genres_union(books):
    all_book_genres = []
    for i in books['genres']:
        if type(i) == list:
            if int(len(i)) != 0:
                all_book_genres.extend(i)
    return all_book_genres


def graph_top_genres(all_books_genres):
    plt.subplots(figsize=(12,10))
    ax = pd.Series(all_books_genres).value_counts()[:10].sort_values(ascending=True).plot.barh(width=0.9,color=sns.color_palette('hls',10))
    for i, v in enumerate(pd.Series(all_books_genres).value_counts()[:10].sort_values(ascending=True).values):
        ax.text(.8, i, v, fontsize=12, color='white', weight='bold')
    plt.title('Top Genres')
    plt.show()


def find_count_unique_values(array):
    return pd.Series(array).value_counts()


def each_book_authors_union(books):
    all_books_authors = []
    for book in books['book_authors']:
        all_books_authors.extend(book)
    return all_books_authors


def graph_top_authors(all_books_authors):
    plt.subplots(figsize=(12,10))
    ax=pd.Series(all_books_authors).value_counts()[:15].sort_values(ascending=True).plot.barh(width=0.9,color=sns.color_palette('muted',40))
    for i, v in enumerate(pd.Series(all_books_authors).value_counts()[:15].sort_values(ascending=True).values):
        ax.text(.8, i, v,fontsize=10,color='white',weight='bold')
    plt.title('Authors with highest appearance')
    plt.show()


def create_author_idx_dict(author_list):
    author_idx_dict = {}
    for i in range(len(author_list.index)):
        author_idx_dict[author_list.index[i]] = i
    return author_idx_dict


def save_dataset(books):
    print(int(books.shape[0] / 10000))
    for index, i in books.iterrows():
        print(index)
        book_genres_in_db = []
        book_authors_in_db = []
        session = get_session()
        try:
            for genre in set(i['genres']):
                genre_in_db = GenreRepository(session).get_by_name(genre)
                if not genre_in_db:
                    book_genres_in_db.append(GenreDatabaseModel(name=genre))
                else:
                    book_genres_in_db.append(genre_in_db)
        except TypeError:
            continue
        session = get_session()
        for author in set(i['book_authors']):
            author_in_db = AuthorRepository(session).get_by_name(author)
            if not author_in_db:
                book_authors_in_db.append(AuthorDatabaseModel(name=author))
            else:
                book_authors_in_db.append(author_in_db)
        new_session = get_session()
        BookRepository(new_session).create(
           **{
               "id": index,
               "rating": i['book_rating'],
               "rating_count": i['book_rating_count'],
               "review_count": i['book_review_count'],
               "title": i['book_title'],
               "image_url": i['image_url'],
               "genres_bin": ','.join((str(i) for i in i['genres_bin'])),
               "authors_bin": ','.join((str(i) for i in i['authors_bin'])),
               'genres': book_genres_in_db,
               'authors': book_authors_in_db
           }
        )


if __name__ == '__main__':
    filename = 'data/book_data.csv'
    binary = Binary()

    ds = read_ds(filename)
    books = delete_unused_columns(ds)
    books = column_values_split(books, 'genres')
    books = column_values_split(books, 'book_authors')

    print(1)
    all_books_genres = each_book_genres_union(books)
    genre_list = find_count_unique_values(all_books_genres)

    books['genres_bin'] = books['genres'].apply(lambda x: binary.genre_binary(x, genre_list.index))
    print(2)
    all_books_authors = each_book_authors_union(books)
    author_list = find_count_unique_values(all_books_authors)
    author_idx_dict = create_author_idx_dict(author_list)

    books['authors_bin'] = books['book_authors'].apply(lambda x: binary.binary_authors(x, author_idx_dict))
    print(books['genres_bin'])
    print(books['authors_bin'])

    save_dataset(books)

    print("FINISHED!!!!")
