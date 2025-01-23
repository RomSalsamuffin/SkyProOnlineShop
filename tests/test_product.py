from src.product import Product


def test_product_init(product1):
    ''' Функция, тестирующая инициализацию объекта класса Product '''
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert product1.color == "Серый"


def test_product_new_product(product6):
    ''' Функция, тестирующая класс-метод new_product класса Product '''
    new_product = Product.new_product(product6)
    assert new_product.name == "HTC desire C"
    assert new_product.description == "128GB, Красный"
    assert new_product.price == 10000
    assert new_product.quantity == 10
    assert new_product.color == "Красный"


def test_product_price_setter(capsys, product1):
    ''' Функция, тестирующая сеттер аттрибута price класса Product '''
    assert product1.price == 180000
    product1.price = 200000
    assert product1.price == 200000
    product1.price = -10000
    captured = capsys.readouterr()
    assert captured.out == 'Цена не должна быть нулевая или отрицательная\n'
    assert product1.price == 200000


def test_product_str(product1):
    ''' Функция, тестирующая магический метод __str__ класса Product '''
    assert product1.__str__() == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(product1, product2):
    ''' Функция, тестирующая магический метод __add__ класса Product '''
    assert product1 + product2 == 2580000.0
