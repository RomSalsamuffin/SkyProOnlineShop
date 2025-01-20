class Product:
    ''' Класс, описывающий товар '''

    name: str  # Название товара
    description: str  # Описание товара
    __price: float  # Цена товара
    quantity: int  # Количество товара на складе

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_dict: dict):
        name = product_dict.get('name')
        description = product_dict.get('description')
        price = product_dict.get('price')
        quantity = product_dict.get('quantity')
        return cls(name, description, price, quantity)
