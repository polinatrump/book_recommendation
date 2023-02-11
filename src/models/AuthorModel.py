from sqlalchemy import Column, String
from src.database.Base import BaseDatabaseModel
from src.domain.Author import Author


class AuthorDatabaseModel(BaseDatabaseModel):
    __tablename__ = 'authors'
    name = Column(String(255), unique=True)

    domain_model = Author
