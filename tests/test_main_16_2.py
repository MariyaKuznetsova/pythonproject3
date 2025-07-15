import pytest

from src.main_16_2 import Category, Product


@pytest.fixture
def product_product_16_2():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_16_2(product_product_16_2):
    assert product_product_16_2.name == "Samsung Galaxy S23 Ultra"
    assert product_product_16_2.description == "256GB, Серый цвет, 200MP камера"
    assert product_product_16_2.price == 180000.0
    assert product_product_16_2.quantity == 5


def test_product_16_2_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    assert len(category1.products) == 3
    assert category1.category_count == 2
    assert category1.product_count == 34
    assert len(category2.products) == 1
