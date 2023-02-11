from sqlalchemy import Column, String
from src.database.Base import BaseDatabaseModel
from src.domain.User import User


class UserDatabaseModel(BaseDatabaseModel):
    domain_model = User

    __tablename__ = 'users'
    first_name = Column(String(255))
    last_name = Column(String(255))
