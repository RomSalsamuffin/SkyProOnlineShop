import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_init(smartphone1: Smartphone):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone1: Smartphone, smartphone2: Smartphone, grass1: LawnGrass):
    ''' Функция, тестирующая функцию сложения класса LawnGrass '''
    assert smartphone1 + smartphone2 == 2580000.0
    with pytest.raises(Exception) as e:
        test_sum = smartphone1 + grass1
    assert e.type == TypeError
