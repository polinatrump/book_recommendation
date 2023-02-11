from sqlalchemy import Column, String
from src.database.Base import BaseDatabaseModel
from src.domain.Genre import Genre


class GenreDatabaseModel(BaseDatabaseModel):
    domain_model = Genre


    __tablename__ = 'genres'
    name = Column(String(255), unique=True)
