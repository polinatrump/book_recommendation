from src.models import RecommendationDatabaseModel
from src.repository.base_repository import SqlAlchemyRepository


class RecommendationRepository(SqlAlchemyRepository):

    def __init__(self, session):
        SqlAlchemyRepository.__init__(self, model=RecommendationDatabaseModel, session=session)









