import json
import logging
import os.path

from src.category import Category
from src.config import APP_PATH
from src.product import Product

logger = logging.getLogger("utils")
log_filepath = os.path.join(APP_PATH, "logs", "utils.log")
file_handler = logging.FileHandler(log_filepath, encoding="utf-8", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_category_json() -> list:
    ''' Функция чтения категорий из JSON - файла. Возвращает список словарей,
    представляющих собой категории товаров '''
    logger.info('Запуск функции get_category_json')
    logger.info('Попытка открытия и чтения JSON файла')
    try:
        with open(os.path.join(APP_PATH, 'data', 'products.json'), encoding='UTF-8') as file:
            categories_list = json.load(file)
        logger.info('Проверка JSON-файла, что он не пустой')
        if not categories_list:
            categories_list = []
    except:
        categories_list = []
    logger.info('Создание пустого списка категорий')
    output_categories_list = []
    logger.info('Перебор считанного списка категорий из JSON файла, создание и заполнение объектов класса Category')
    for category_dict in categories_list:
        category = Category(name=category_dict.get('name'),
                            description=category_dict.get('description'),
                            products=[]
                            )
        products_list = category_dict.get('products')
        for product_dict in products_list:
            product = Product(name=product_dict.get('name'),
                              description=product_dict.get('description'),
                              price=product_dict.get('price'),
                              quantity=product_dict.get('quantity')
                              )
            category.products.append(product)
        output_categories_list.append(category)
    logger.info('Возврат списка категорий')
    return output_categories_list


categories_list = get_category_json()
for category in categories_list:
    print(type(category))
