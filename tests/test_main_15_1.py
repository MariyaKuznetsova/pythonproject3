import pytest

from src.main_15_1 import Category, Product


@pytest.fixture
def product_product_15_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_15_1(product_product_15_1):
    assert str(product_product_15_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_15_1_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert product1 + product2 == 2580000.0
    assert product2 + product3 == 2114000.0
    assert str(product2) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'



@pytest.fixture
def category_category_15_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category_15_1(category_category_15_1):
    assert str(category_category_15_1) == 'Смартфоны, количество продуктов: 27 шт.'
    assert category_category_15_1.products_str == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
 'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']
