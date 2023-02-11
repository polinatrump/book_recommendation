

class AuthorIdNotFoundException(Exception):
    message = 'Author with given id is not found'

    def __str__(self):
        return AuthorIdNotFoundException.message


class AuthorNameNotFoundException(Exception):
    message = 'Author with given name is not found'

    def __str__(self):
        return AuthorNameNotFoundException.message
