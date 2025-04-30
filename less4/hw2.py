def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a + b) * 2

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b 

    assert area == 200