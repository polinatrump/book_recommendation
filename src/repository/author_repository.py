from sqlalchemy import select

from src.models import AuthorDatabaseModel
from src.repository.base_repository import SqlAlchemyRepository


class AuthorRepository(SqlAlchemyRepository):

    def __init__(self, session):
        SqlAlchemyRepository.__init__(self, model=AuthorDatabaseModel, session=session)

    def get_by_name(self, name: str) -> AuthorDatabaseModel:
        """
        Allows get author by name
        :param name: name of genre
        :return:
        """
        result = self.session.execute(
            select(self.model).where(self.model.name == name)
        )
        model = result.scalars().first()
        self.session.close()
        return model
