from sqlalchemy import MetaData, Integer, Column
from src.database.db import Base


class BaseDatabaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    metadata: MetaData = MetaData()
