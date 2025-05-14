from tabnanny import check

from future.utils import raise_

import pytest


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if Product.check_quantity(self, quantity) is True:
            self.quantity -= quantity
            return True
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if buy_count <= 0:
            raise ValueError
        elif product in self.products:
            self.products[product] += buy_count
            return self.products[product]
        else:
            self.products[product] = buy_count
            return self.products[product]
        

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count >= self.products[product]:
            self.products[product] = 0
        elif remove_count < 0:
            raise ValueError
        else:
            self.products[product] -= remove_count
        return self.products[product]

    def clear(self):
        self.products.clear()
        return 'Корзина очищена'

    def get_total_price(self) -> float:
        totalPrice = 0.0
        for product, count in self.products.items():
            totalPrice += product.price * count
        return totalPrice

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        for product, count in self.products.items():
            print(Product.check_quantity(product, count))
            if Product.check_quantity(product, count) is False:
                raise ValueError
            else:
                Product.buy(product, count)
                Cart.clear(self)
                return 'Спасибо за покупку'


