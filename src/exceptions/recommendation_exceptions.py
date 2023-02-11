

class RecommendationIdNotFoundException(Exception):
    message = 'Recommendation with given id is not found'

    def __str__(self):
        return RecommendationIdNotFoundException.message
