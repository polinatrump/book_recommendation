

class GenreIdNotFoundException(Exception):
    message = 'Genre with given id is not found'

    def __str__(self):
        return GenreIdNotFoundException.message


class GenreNameNotFoundException(Exception):
    message = 'Genre with given name is not found'

    def __str__(self):
        return GenreNameNotFoundException.message
