from src.product import Product


class Category:
    ''' Класс, описывающий категории товара '''

    name: str  # Название товара
    description: str  # Описание товара
    __products: list[Product]  # Список товаров в категории
    category_count: int = 0  # Счетчик количества категорий
    product_count: int = 0  # Счетчик количества товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __del__(self):
        Category.category_count -= 1
        Category.product_count -= len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return product_list
