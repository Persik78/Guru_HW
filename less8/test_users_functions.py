import pytest

from models.providers import UserProvider, CsvUserProvider, DataBaseUserProvider, ApiUserProvider
from models.users import User, Status, USER_ADULT_AGE, Worker



@pytest.fixture(params=[CsvUserProvider, DataBaseUserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()

@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()

@pytest.fixture
def workers(users) -> list[Worker]:
    """
    Отбираем только рабоников из списка пользователей
    """
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == Status.worker]
    return workers

def test_workers_are_adult(workers):
    """
    Тест на то что все работники старше 18 лет
    """
    for worker in workers:
        assert worker.is_adult(), f"Работник {worker.name} младше {USER_ADULT_AGE} лет"
