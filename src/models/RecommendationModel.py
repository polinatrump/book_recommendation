from sqlalchemy import Column, Integer, ForeignKey
from src.database.Base import BaseDatabaseModel
from src.domain.Recommendation import Recommendation


class RecommendationDatabaseModel(BaseDatabaseModel):
    domain_model = Recommendation

    __tablename__ = 'recommendations'
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
