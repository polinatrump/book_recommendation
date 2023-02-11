from src.exceptions.book_exceptions import BookTitleNotFoundException
from src.exceptions.user_exceptions import UserLastNameFirstNameNotFoundException
from src.repository import UserRepository, RecommendationRepository, BookRepository
from src.services.SearchNeighbours import SearchNeighboursService
from src.usecases import UserFindByLastFirstNameUseCase, UserCreateUseCase, GetBookByTitleUseCase
from src.usecases.book_usecase import ListBookUseCase
from src.usecases.recommendation_usecase import CreateRecommendationUseCase
from src.views.CLUserInterface import CLUserInterface


class ApplicationEntryPoint:

    @classmethod
    def start(cls):
        user_interface = CLUserInterface()
        user_interface.draw_hello_page()

        first_name = user_interface.get_user_first_name()
        last_name = user_interface.get_user_last_name()

        user_find_by_last_name_first_name_use_case = UserFindByLastFirstNameUseCase(UserRepository)
        user_create_use_case = UserCreateUseCase(UserRepository)
        book_by_title_use_case = GetBookByTitleUseCase(BookRepository)
        recommendations_create_usecase = CreateRecommendationUseCase(RecommendationRepository)
        book_list_usecase = ListBookUseCase(BookRepository)

        try:
            user = user_find_by_last_name_first_name_use_case(first_name.title(), last_name.title())
            user_interface.alert_welcome_back(first_name)
        except UserLastNameFirstNameNotFoundException:
            user = user_create_use_case(first_name=first_name, last_name=last_name)
            user_interface.alert_profile_created(first_name)

        book = None
        while not book:
            book_title = user_interface.get_book_title()
            try:
                book = book_by_title_use_case(book_title)
            except BookTitleNotFoundException:
                user_interface.alert_book_not_found(book_title)
        processes = []
        count_of_recommendations = user_interface.get_count_recommendations()
        batches = SearchNeighboursService.create_batches_as_input_arguments(
            count_of_recomendations=count_of_recommendations,
            book=book,
            book_list_usecase=book_list_usecase
        )
        results = SearchNeighboursService.process_batches_in_separate_processes(batches)
        user_interface.alert_recommendations_before_result()
        for i in results[0:count_of_recommendations]:
            print(*i)
            recommendations_create_usecase(book_id=int(i[2]), user_id=user.id)