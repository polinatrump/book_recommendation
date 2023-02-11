from sqlalchemy import Column, Integer, Table, ForeignKey, Float, String, Text
from sqlalchemy.orm import relationship

from src.database.Base import BaseDatabaseModel
from src.domain import Book

book_author_association_table = Table(
    "book_author",
    BaseDatabaseModel.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("author_id", ForeignKey("authors.id")),
)

book_genre_association_table = Table(
    "book_genre",
    BaseDatabaseModel.metadata,
    Column("book_id", ForeignKey("books.id")),
    Column("genre_id", ForeignKey("genres.id")),
)


class BookDatabaseModel(BaseDatabaseModel):
    domain_model = Book

    __tablename__ = 'books'
    rating = Column(Float())
    rating_count = Column(Integer())
    review_count = Column(Integer())
    title = Column(String(255))
    image_url = Column(String(255))
    genres_bin = Column(Text())
    authors_bin = Column(Text())

    genres = relationship(
        "GenreDatabaseModel",
        secondary=book_genre_association_table,
        backref="books",
        # lazy='joined'
    )

    authors = relationship(
        "AuthorDatabaseModel",
        secondary=book_author_association_table,
        backref="books",
        lazy='joined'
    )
