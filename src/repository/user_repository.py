from sqlalchemy import select

from src.models import UserDatabaseModel
from src.repository.base_repository import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository):

    def __init__(self, session):
        SqlAlchemyRepository.__init__(self, model=UserDatabaseModel, session=session)

    def get_by_first_and_last_name(
            self,
            first_name: str,
            last_name: str
    ):
        result = self.session.execute(
            select(
                self.model
            ).where(
                self.model.first_name == first_name
                and
                self.model.last_name == last_name
            )
        )
        model = result.scalars().first()
        self.session.close()
        return model


# Внутри SqlAlchemyRepository уже определены методы сreate update get delete
# поэтому достаточно связать репозиторий с моделью бд и пользоваться так как написано в
# бук репозитори внизу