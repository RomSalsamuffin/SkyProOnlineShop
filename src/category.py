from src.product import Product


class Category:
    ''' Класс, описывающий категории товара '''

    name: str  # Название товара
    description: str  # Описание товара
    products: list[Product]  # Список товаров в категории
    category_count: int = 0  # Счетчик количества категорий
    product_count: int = 0  # Счетчик количества товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __del__(self):
        Category.category_count -= 1
        Category.product_count -= len(self.products)
