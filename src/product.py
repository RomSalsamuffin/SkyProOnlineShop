class Product:
    ''' Класс, описывающий товар '''

    name: str  # Название товара
    description: str  # Описание товара
    __price: float  # Цена товара
    quantity: int  # Количество товара на складе
    color: str  # Цвет товара

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str = ''):
        ''' Конструктор объектов класса Product '''
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color

    @property
    def price(self):
        ''' Геттер-метод для получения цены товара '''
        return self.__price

    @price.setter
    def price(self, value: float):
        ''' Метод-сеттер для установки значения цены товара '''
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_dict: dict):
        ''' Метод для добавления нового продукта по данным из словаря '''
        name: str = product_dict['name']
        description: str = product_dict['description']
        price: float = product_dict['price']
        quantity: int = product_dict['quantity']
        color: str = product_dict['color']
        return cls(name, description, price, quantity, color)

    def __str__(self):
        ''' Магический метод для строкового отображения объекта  '''
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        ''' Магический метод, который вызывается при сложении двух объектов '''
        if not type(self) == type(other):
            raise TypeError('Складывать можно только объекты класса Product или дочерних классов')
        return self.price * self.quantity + other.price * other.quantity
