import pytest

from src.main_17_1 import Category, Product


@pytest.fixture
def product_product_17_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_17_1(product_product_17_1):
    assert product_product_17_1.name == "Samsung Galaxy S23 Ultra"
    assert product_product_17_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_product_17_1.price == 180000.0
    assert product_product_17_1.quantity == 5


def test_product_raises():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)


def test_product_17_1_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category1.middle_price() == 140333.33
    assert category1.category_count == 3
    assert category1.product_count == 40
    assert category2.middle_price() == 195000.0
    assert category_empty.middle_price() == 0
