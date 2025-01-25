from src.product import Product


class LawnGrass(Product):
    ''' Класс, описывающий газонную траву '''
    country: str  # Страна производства
    germination_period: str  # Срок прорастания

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 country: str,
                 germination_period: str,
                 color: str):
        ''' Конструктор объектов класса LawnGrass '''
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
