

class BookIdNotFoundException(Exception):
    message = 'Book with given id is not found'

    def __str__(self):
        return BookIdNotFoundException.message


class BookTitleNotFoundException(Exception):
    message = 'Book with given title is not found'

    def __str__(self):
        return BookTitleNotFoundException.message
