"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from less8.HWless8.models import Product, Cart

book = Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart(product):
    cart = Cart()
    assert cart.add_product(product, 5) == 5
    return cart

@pytest.fixture
def overly_filled_cart(product):
    cart = Cart()
    assert cart.add_product(product, 1001) == 1001
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False, f'{product.name} больше запрашиваемого'
        assert product.check_quantity(product.quantity - 1) is True, f'{product.name} больше запрашиваемого'
        assert product.check_quantity(0) is True # проверка нулевого значение
        assert product.check_quantity(-1) is True # проверка отрицательного значения (в классе нет ограничения)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(product.quantity) is True
        assert product.buy(product.quantity - 1) is True, f'{product.name} больше запрашиваемого'
        assert product.buy(product.quantity == 500)
        assert product.buy(0) is True  # проверка нулевого значение
        assert product.buy(-1) is True  # проверка отрицательного значения (в классе нет ограничения)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)
        with pytest.raises(ValueError):
            product.buy(product.quantity ** 2)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, cart):
        assert cart.add_product(product, 2) == 7
        assert cart.add_product(product, 3) == 10
        with pytest.raises(ValueError):
            cart.add_product(product, -1)
        with pytest.raises(ValueError):
            cart.add_product(product, 0)

    def test_remove_product(self, product, cart):
        assert cart.remove_product(product, 2) == 3
        assert cart.remove_product(product, 0) == 3
        assert cart.remove_product(product, None) == 0
        assert cart.remove_product(product, 2) == 0
        with pytest.raises(ValueError):
            cart.remove_product(product, -1)

    def test_get_total_price(self, product, cart):
        assert cart.get_total_price() == 500.0
        assert cart.remove_product(product, None) == 0
        assert cart.get_total_price() == 0.0

    def test_buy(self, cart, overly_filled_cart):
        assert cart.buy() == 'Спасибо за покупку'
        with pytest.raises(ValueError):
            overly_filled_cart.buy()

    def test_clear(self, cart, overly_filled_cart):
        assert cart.clear() == 'Корзина очищена'
        assert overly_filled_cart.clear() == 'Корзина очищена'