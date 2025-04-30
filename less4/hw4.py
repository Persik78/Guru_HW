import random
def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    l = []
    for i in range(10):
        l.append(random.randint(1,100))
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    print(l)
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))