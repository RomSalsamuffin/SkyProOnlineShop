from src.product import Product


class Category:
    ''' Класс, описывающий категории товара '''

    name: str  # Название товара
    description: str  # Описание товара
    __products: list[Product]  # Список товаров в категории
    category_count: int = 0  # Счетчик количества категорий
    product_count: int = 0  # Счетчик количества товаров

    def __init__(self, name: str, description: str, products: list[Product]):
        ''' Конструктор объектов класса Category '''
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __del__(self):
        ''' Деструктор класса Category '''
        Category.category_count -= 1
        Category.product_count -= len(self.__products)

    def add_product(self, product: Product):
        ''' Метод для добавления объекта класса Product в Category '''
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        ''' Геттер-метод для получения строкового отображения списка продуктов '''
        products_str = ''
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def __str__(self):
        ''' Магический метод для строкового отображения объекта  '''
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
        return f"{self.name}, количество продуктов: {product_count} шт."
