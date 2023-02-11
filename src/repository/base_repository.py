import abc
from typing import NoReturn, List, Type, Union

from pydantic import BaseModel
from sqlalchemy import delete, select, update

from src.database.Base import BaseDatabaseModel
from src.database.db import Base


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def _get(self, id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def _create(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _delete(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _list(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _parse(self, model: BaseDatabaseModel) -> BaseModel:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, model: Type[Base], session):
        """
        Allows to perform operations with database models
        :param model: SQLAlchemy model
        :param session: SQLAlchemy session
        """
        self.model = model
        self.session = session

    def _get(self, id: int) -> Union[Type[Base], NoReturn]:
        """
        Get model from database by id
        :param id: Row id
        :return: SQLAlchemy model or None if not found
        """
        result = self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        model = result.scalars().first()
        self.session.close()
        return self.parse(model)

    def _create(self, **kwargs) -> Type[Base]:
        """
        Create row in database by kwargs
        :param kwargs: model fields
        :return: SQLAlchemy model
        """
        model = self.model()
        for key, value in kwargs.items():
            if hasattr(model, key):
                setattr(model, key, value)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        self.session.close()
        return self.parse(model)

    def _update(self, id: int, **kwargs) -> Union[Type[Base], None]:
        """
        Update row in database by id
        :param id: Row id
        :param kwargs: model fields
        :return: SQLAlchemy model or None if not found
        """
        self.session.execute(
            update(self.model).where(self.model.id == id).values(**kwargs)
        )
        result = self.session.get(self.model, id)
        try:
            self.session.commit()
        except Exception as err:
            print(err)
            self.session.rollback()
            self.session.close()
        return self.parse(result)

    def _list(self, limit: int = None, offset: int = 0, **kwargs) -> List[Type[Base]]:
        """
        Return list of rows from DB
        :param limit: limit of rows needed to be returned
        :param offset: offset of rows needed to be skipped
        :param kwargs: other filters from model fields
        :return: list of SQLAlchemy models
        """
        if limit:
            statement = select(self.model).limit(limit).offset(offset).filter_by(
                **{key: val for key, val in kwargs.items() if val is not None}
            )
            result = self.session.execute(
                statement
            )
        else:
            statement = select(self.model).filter_by(**kwargs)
            result = self.session.execute(
                statement
            )
        result = result.scalars().unique()
        res = [self.parse(i) for i in result]
        self.session.close()
        return res

    def _delete(self, id: int) -> NoReturn:
        """
        Deletes row in DB by id
        :param id: Row id
        :return: None
        """
        try:
            self.session.execute(
                delete(self.model).where(self.model.id == id)
            )
            self.session.commit()
        except Exception as err:
            self.session.rollback()
            self.session.close()
            raise err

    def count(self) -> int:
        """
        Counts all rows in DB
        :return: quantity of rows
        """
        statement = select(self.model.id)
        result = self.session.execute(
            statement
        )
        result = len(result.scalars().all())
        self.session.close()
        return result

    async def delete_all(self) -> NoReturn:
        """
        Clears DB table
        :return: None
        """
        self.session.execute(
            delete(self.model)
        )
        self.session.commit()

    def get(self, id: int) -> Union[Type[Base], None]:
        """
        Public get method
        :param id: Row id
        :return: SQLAlchemy model or None if not found
        """
        return self._get(id=id)

    def create(self, **kwargs) -> Type[Base]:
        """
        Public create method
        :return: SQLAlchemy model
        """
        return self._create(**kwargs)

    def update(self, id: int, **kwargs) -> Union[Type[Base], None]:
        """
        Public edit method
        :param id: Row id
        :return: SQLAlchemy model or None if not found
        """
        return self._update(id, **kwargs)

    def list(self, limit: int = None, offset: int = 0, **kwargs) -> List[Type[Base]]:
        """
        Public list method
        :param limit: limit of rows needed to be returned
        :param offset: offset of rows needed to be skipped
        :param kwargs: other filters from model fields
        :return: list of SQLAlchemy models
        """
        return self._list(limit, offset, **kwargs)

    def delete(self, id: int) -> NoReturn:
        """
        Public delete method
        :param id: Row id
        :return: None
        """
        self._delete(id)

    def parse(self, model: BaseDatabaseModel) -> BaseModel:
        return self._parse(model.__dict__)

    def _parse(self, model: dict) -> BaseModel:
        for key, value in model.items():
            if isinstance(value, list):
                model[key] = [i.__dict__ for i in value if isinstance(i, BaseDatabaseModel)]
        return self.model.domain_model.parse_obj(model)
