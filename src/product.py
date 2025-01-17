class Product:
    ''' Класс, описывающий товар '''

    name: str  # Название товара
    description: str  # Описание товара
    price: float  # Цена товара
    quantity: int  # Количество товара на складе

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
