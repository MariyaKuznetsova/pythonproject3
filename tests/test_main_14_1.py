import pytest

from src.main_14_1 import Category, Product


@pytest.fixture
def product_product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product_product_1):
    assert product_product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_product_1.price == 180000.0
    assert product_product_1.quantity == 5


@pytest.fixture
def category_category_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category(category_category_1):
    assert category_category_1.name == "Смартфоны"
    assert (
        category_category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_category_1.category_count == 1
    assert category_category_1.product_count == 27
