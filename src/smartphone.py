from src.product import Product


class Smartphone(Product):
    ''' Класс, описывающий смартфоны '''
    efficiency: float  # Производительность
    model: str  # Модель
    memory: float  # Объем встроенной памяти
    color: str  # Цвет

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 efficiency: float,
                 model: str,
                 memory: float,
                 color: str):
        ''' Конструктор объектов класса LawnGrass '''
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
