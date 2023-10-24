"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


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
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(300)
        assert product.check_quantity(700)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product)
        assert cart.products[product] == 1

        cart.add_product(product, buy_count=2)
        assert cart.products[product] == 3

    def test_remove_one_product(self, product, cart):
        cart.add_product(product, buy_count=2)
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 1

    def test_remove_all_product(self, product, cart):
        cart.add_product(product, buy_count=4)
        cart.remove_product(product, remove_count=4)
        assert not cart.products

    def test_cart_remove_more_than_added(self, cart, product):
        cart.add_product(product, buy_count=3)
        cart.remove_product(product, remove_count=6)
        assert not cart.products

    def test_clear_cart(self, product, cart):
        cart.add_product(product, buy_count=1)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product)
        assert cart.get_total_price() == product.price

    def test_get_total_price_empty_cart(self, cart, product):
        assert cart.get_total_price() == 0.0

    def test_buy(self, product, cart):
        cart.add_product(product)
        cart.buy()
        assert cart.products == {}

    def test_buy_empty_cart(self, product, cart):
        assert cart.get_total_price() == 0.0
        cart.buy()
        assert not cart.products

    def test_cart_buy_more_than_available(self, product, cart):
        cart.add_product(product, buy_count=1003)
        with pytest.raises(ValueError):
            cart.buy()
