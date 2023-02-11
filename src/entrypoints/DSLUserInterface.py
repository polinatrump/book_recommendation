import click
from src.repository import BookRepository, RecommendationRepository, UserRepository
from src.services.SearchNeighbours import SearchNeighboursService
from src.usecases import GetBookByTitleUseCase, UserFindByLastFirstNameUseCase
from src.usecases.book_usecase import ListBookUseCase
from src.usecases.recommendation_usecase import CreateRecommendationUseCase
from src.views.CLUserInterface import CLUserInterface
    
    
@click.command()
@click.option('--first_name', help='User first name')
@click.option('--last_name', help='User last name')
@click.option('--book_title', help='Book title for which recommendations will be searched')
@click.option('--recommend_count', help='Count of recommendations in range [1,10]')
def start(
        first_name: str,
        last_name: str,
        book_title: str,
        recommend_count: int
):
    book_by_title_use_case = GetBookByTitleUseCase(BookRepository)
    book_list_usecase = ListBookUseCase(BookRepository)
    user_interface = CLUserInterface()
    recommendations_create_usecase = CreateRecommendationUseCase(RecommendationRepository)
    user_find_by_last_name_first_name_use_case = UserFindByLastFirstNameUseCase(UserRepository)
    user = user_find_by_last_name_first_name_use_case(first_name.title(), last_name.title())
    book = book_by_title_use_case(book_title)
    batches = SearchNeighboursService.create_batches_as_input_arguments(
        count_of_recomendations=int(recommend_count),
        book=book,
        book_list_usecase=book_list_usecase
    )
    results = SearchNeighboursService.process_batches_in_separate_processes(batches)
    user_interface.alert_recommendations_before_result()
    for i in results[0:int(recommend_count)]:
        print(*i)
        recommendations_create_usecase(book_id=int(i[3]), user_id=user.id)