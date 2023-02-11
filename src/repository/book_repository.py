from typing import Union, Type, NoReturn

from pydantic import BaseModel
from sqlalchemy import select

from src.database.Base import BaseDatabaseModel
from src.database.db import get_session, Base
from src.domain import Book
from src.models import BookDatabaseModel
from src.repository.base_repository import  SqlAlchemyRepository


class BookRepository(SqlAlchemyRepository):

    def __init__(self, session):
        SqlAlchemyRepository.__init__(self, model=BookDatabaseModel, session=session)

    def get_book_by_title(self, title) -> Union[Type[Base], NoReturn]:
        result = self.session.execute(
            select(self.model).where(self.model.title == title)
        )
        model = result.scalars().first()
        self.session.close()
        if model:
            return self.parse(model)
        return model


if __name__ == '__main__':
    session = get_session()
    BookRepository(session).create(
       **{"id": 4, "title": "1234"}
    )
