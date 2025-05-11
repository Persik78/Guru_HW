import csv

def test_workers_are_adult():
    """
    Тест на то что все работники старше 18 лет
    """
    for worker in workers:
        assert int(worker['age']) >= 18


        #users = list(users)