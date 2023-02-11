import pytest

from src.domain.User import User


@pytest.fixture
def create_user_domain_model():
    return User(
         id=1,
         first_name='TestFirstName',
         last_name='TestLastName',
    )
