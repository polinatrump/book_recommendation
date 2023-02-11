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

    # def parse(self, model: BookDatabaseModel) -> BaseModel:
    #     # model_as_dict = model.__dict__
    #     model.genres_bin = model.genres_bin.split(',')
    #     model.authors_bin =  model.authors_bin.split(',')
    #     return self._parse(model.__dict__)
    # #
    # def _parse(self, model: dict) -> BaseModel:
    #     for key, value in model.items():
    #         if key not in ['genres_bin', 'authors_bin']:
    #             if isinstance(value, list):
    #                 model[key] = [i.__dict__ for i in value if isinstance(i, BaseDatabaseModel)]
    #     return self.model.domain_model.parse_obj(model)


    # def _create(self, **kwargs) -> Type[Base]:
    #     """
    #     Create row in database by kwargs
    #     :param kwargs: model fields
    #     :return: SQLAlchemy model
    #     """
    #     model = self.model()
    #     print(kwargs.items())
    #     for key, value in kwargs.items():
    #         if hasattr(model, key):
    #             setattr(model, key, value)
    #     self.session.add(model)
    #     self.session.commit()
    #     self.session.refresh(model)
    #     self.session.close()
    #     return model


if __name__ == '__main__':
    session = get_session()
    BookRepository(session).create(
       **{"id": 4, "title": "1234"}
    )
    # print(BookRepository(session).get_book_by_title(
    #    title="Test"
    # ))