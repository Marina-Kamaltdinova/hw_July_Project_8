import pytest

from tests.models import Product, Cart

"""
Протестируйте классы из модуля tests/models.py
"""


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(quantity=100)
        assert product.quantity == 900

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(quantity=1100)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 1000)
        assert cart.products[product] == 1000

    def test_remove_product_bigger_than_buy_count(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 100)
        assert cart.products[product] == 900

    def test_clear(self, cart, product):
        cart.add_product(product, 40)
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

    def test_buy(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900

