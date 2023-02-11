

class UserIdNotFoundException(Exception):
    message = 'User with given id is not found'

    def __str__(self):
        return UserIdNotFoundException.message


class UserLastNameFirstNameNotFoundException(Exception):
    message = 'User with given first name and last name is not found'

    def __str__(self):
        return UserLastNameFirstNameNotFoundException.message
