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
