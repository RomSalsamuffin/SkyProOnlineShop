import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_lawngrass_init(grass1: LawnGrass):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_add(grass1: LawnGrass, grass2: LawnGrass, smartphone1: Smartphone):
    ''' Функция, тестирующая функцию сложения класса LawnGrass '''
    assert grass1 + grass2 == 16750.0
    with pytest.raises(Exception) as e:
        test_sum = grass1 + smartphone1
    assert e.type == TypeError
