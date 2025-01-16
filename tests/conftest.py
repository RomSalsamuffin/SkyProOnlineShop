import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(scope="function")
def product1():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


@pytest.fixture(scope="function")
def product2():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


@pytest.fixture(scope="function")
def product3():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0,
                   14)


@pytest.fixture(scope="function")
def smartphones(product1, product2, product3):
    return Category("Смартфоны",
                    "Различные смартфоны",
                    [product1, product2, product3])


@pytest.fixture(scope="function")
def product4():
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0,
                   7)


@pytest.fixture(scope="function")
def televisors(product4):
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [product4])
