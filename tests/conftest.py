import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture(scope="function")
def product1():
    ''' Фикстура, возвращающая объект класса Product'''
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5,
                   "Серый")


@pytest.fixture(scope="function")
def product2():
    ''' Фикстура, возвращающая объект класса Product'''
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8,
                   "Серый")


@pytest.fixture(scope="function")
def product3():
    ''' Фикстура, возвращающая объект класса Product'''
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0,
                   14,
                   "Синий")


@pytest.fixture(scope="function")
def smartphones(product1, product2, product3):
    ''' Фикстура, возвращающая объект класса Category'''
    return Category("Смартфоны",
                    "Различные смартфоны",
                    [product1, product2, product3])


@pytest.fixture(scope="function")
def product4():
    ''' Фикстура, возвращающая объект класса Product'''
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0,
                   7,
                   "Черный")


@pytest.fixture(scope="function")
def televisors(product4):
    ''' Фикстура, возвращающая объект класса Category'''
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
                    [product4])


@pytest.fixture(scope="function")
def product5():
    ''' Фикстура, возвращающая объект класса Product'''
    return Product("Xiaomi Redmi Note 13",
                   "1024GB, Черный",
                   50000.0,
                   20,
                   "Черный")


@pytest.fixture(scope="function")
def product6():
    ''' Фикстура, возвращающая словарь с атрибутами объекта класса Product'''
    return {"name": "HTC desire C",
            "description": "128GB, Красный",
            "price": 10000.0,
            "quantity": 10,
            "color": "Красный"}


@pytest.fixture(scope="function")
def smartphone1():
    ''' Фикстура, возвращающая объект класса Smartphone'''
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый")


@pytest.fixture(scope="function")
def smartphone2():
    ''' Фикстура, возвращающая объект класса Smartphone'''
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      98.2,
                      "15",
                      512,
                      "Gray space")


@pytest.fixture(scope="function")
def grass1():
    ''' Фикстура, возвращающая объект класса LawnGrass'''
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый")


@pytest.fixture(scope="function")
def grass2():
    ''' Фикстура, возвращающая объект класса LawnGrass'''
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0,
                     15,
                     "США",
                     "5 дней",
                     "Темно-зеленый")
