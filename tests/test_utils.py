# from unittest.mock import Mock, patch
#
# from src.category import Category
# from src.product import Product
# from src.utils import get_category_json
#
#
# @patch("src.utils.json.load")
# def test_get_category_json(mocked_json_load: Mock, smartphones, televisors):
#     ''' Функция, тестирующая работу функции get_category_json '''
#     test_category_list = []
#     for category in [smartphones, televisors]:
#         category_dict: dict = {}
#         category_dict["name"] = category.name
#         category_dict["description"] = category.description
#         category_dict["products"] = []
#         for product in category.products:
#             product_dict: dict = {}
#             product_dict["name"] = product.name
#             product_dict["description"] = product.description
#             product_dict["price"] = product.price
#             product_dict["quantity"] = product.quantity
#             category_dict["products"].append(product_dict)
#         test_category_list.append(category_dict)
#     mocked_json_load.return_value = test_category_list
#     category_list = get_category_json()
#     assert isinstance(category_list, list)
#     test_category_list = [smartphones, televisors]
#     for i in range(len(category_list)):
#         category = category_list[i]
#         assert isinstance(category, Category)
#         test_category = test_category_list[i]
#         assert category.name == test_category.name
#         assert category.description == test_category.description
#         assert isinstance(category.products, list)
#         for j in range(len(category.products)):
#             product = category.products[j]
#             assert isinstance(product, Product)
#             assert product.name == test_category.products[j].name
#             assert product.description == test_category.products[j].description
#             assert product.price == test_category.products[j].price
#             assert product.quantity == test_category.products[j].quantity
