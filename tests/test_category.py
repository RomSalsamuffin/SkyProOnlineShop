from src.category import Category


def test_category_init(smartphones):
    ''' Функция, тестирующая инициализацию объекта класса Category '''
    assert smartphones.name == "Смартфоны"
    assert smartphones.description == "Различные смартфоны"
    assert smartphones.category_count == 1
    assert smartphones.product_count == 3


def test_category_count(smartphones, televisors):
    ''' Функция, тестирующая подсчет количества категорий '''
    assert Category.category_count == 2
    assert smartphones.category_count == 2
    assert televisors.category_count == 2


def test_products_count(smartphones, televisors):
    ''' Функция, тестирующая подсчет количества продуктов '''
    assert Category.product_count == 4
    assert smartphones.product_count == 4
    assert televisors.product_count == 4


def test_category_add_product(smartphones, product5):
    ''' Функция, тестирующая функцию add_category класса Category '''
    assert smartphones.product_count == 3
    smartphones.add_product(product5)
    assert smartphones.product_count == 4
    assert smartphones.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                    'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                    'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                                    'Xiaomi Redmi Note 13, 50000.0 руб. Остаток: 20 шт.\n')


def test_category_products(televisors):
    ''' Функция, тестирующая геттер products класса Category '''
    assert televisors.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
