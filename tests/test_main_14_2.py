import pytest

from src.main_14_2 import Category, Product


@pytest.fixture
def product_product_14_2_1():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


def test_product_14_2(product_product_14_2_1):
    assert product_product_14_2_1.name == '55" QLED 4K'
    assert product_product_14_2_1.description == "Фоновая подсветка"
    assert product_product_14_2_1.get_price == 123000.0
    assert product_product_14_2_1.quantity == 7


@pytest.fixture
def category_category_14_2_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category_14_2(category_category_14_2_1):
    assert category_category_14_2_1.name == "Смартфоны"
    assert (
        category_category_14_2_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_category_14_2_1.category_count == 1
    assert category_category_14_2_1.product_count == 27
    assert category_category_14_2_1.products_str == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
