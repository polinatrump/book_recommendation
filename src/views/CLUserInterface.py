

class CLUserInterface:

    def draw_hello_page(self):
        print("*******************************************************")
        print("*****----", end='')
        print("Welcome to Book Recommendation System", end='')
        print('----***** ')
        print("*******************************************************")
        print()

    def get_user_first_name(self) -> str:
        return input('Please, enter your first name: ')

    def get_user_last_name(self) -> str:
        return input('Please, enter your last name: ')

    def alert_profile_created(self, first_name: str):
        print(f"{first_name.title()}, your profile was successfully created!")

    def alert_welcome_back(self, first_name: str):
        print(f"{first_name.title()},welcome back!")

    def get_book_title(self) -> str:
        return input('Enter a book title: ')

    def alert_book_not_found(self, book_title: str):
        print(f"Sorry, no book with name: {book_title} was found")

    def get_count_recommendations(self):
        count_of_recommendations = 0
        while int(count_of_recommendations) > 10 or int(count_of_recommendations) < 1:
            print("Please, enter how many books you want to get as recommendation")
            count_of_recommendations = input("Please, enter not more than 10 books and not less than 1, thank you: \n")
        return int(count_of_recommendations)

    def alert_recommendations_before_result(self):
        print('Your recommendations are: ')


