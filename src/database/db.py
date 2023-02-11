from typing import NoReturn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base = declarative_base()


class DBEngine:
    """
    Singleton class which represents connection engine of database
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not DBEngine._instance:
            DBEngine._instance = super(DBEngine, cls).__new__(cls, *args, **kwargs)
        return DBEngine._instance

    def __init__(self, *args, **kwargs):
        self.engine = create_engine(
            f'sqlite:///./src/database/database.s3db',
            echo=False
        )

    def get_session(self) -> Session:
        """
        Method to get async connection session to Database
        :return: sqlalchemy.ext.asyncio.AsyncSession
        """
        session = sessionmaker(
            self.engine, expire_on_commit=False,
        )
        with session() as session:
            try:
                return session
            finally:
                session.close()

    def init_models(self) -> NoReturn:
        """
        Method to init models in runtime
        :return: None
        """
        with self.engine.begin() as conn:
            Base.metadata.create_all()


def get_session() -> Session:
    """
    Function which allows to get session without DBEngine class initialization
    :return: sqlalchemy.ext.asyncio.AsyncSession
    """
    return DBEngine().get_session()


if __name__ == '__main__':
    print(DBEngine().get_session())