def get_user_first_name():
    name = input('Please, enter your full name: ')
    return name


def alert_profile_created(func):
    print(f"{func()}, your profile was successfully created!")


def get_count_recommendations():
    count_of_recommendations = 0
    while int(count_of_recommendations) > 10 or int(count_of_recommendations) < 1:
        count_of_recommendations = input("Enter not more than 10 books and not less than 1: ")
    return int(count_of_recommendations)


def needed_number_of_users_recommendations():
    print("Please, enter how many books you want to get as recommendation.")
    return get_count_recommendations()


alert_profile_created(get_user_first_name)
recom_num = needed_number_of_users_recommendations()