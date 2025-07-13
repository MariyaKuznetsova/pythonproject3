import pytest

from src.main_16_1 import Category, Smartphone, LawnGrass


@pytest.fixture
def product_smartphone_16_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_grass_16_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_product_smartphone_16_1(product_smartphone_16_1):
    assert product_smartphone_16_1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone_16_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_16_1.price == 180000.0
    assert product_smartphone_16_1.quantity == 5
    assert product_smartphone_16_1.efficiency == 95.5
    assert product_smartphone_16_1.model == "S23 Ultra"
    assert product_smartphone_16_1.memory == 256
    assert product_smartphone_16_1.color == "Серый"


def test_product_grass_16_1(product_grass_16_1):
    assert product_grass_16_1.name == "Газонная трава"
    assert product_grass_16_1.description == "Элитная трава для газона"
    assert product_grass_16_1.price == 500.0
    assert product_grass_16_1.quantity == 20
    assert product_grass_16_1.country == "Россия"
    assert product_grass_16_1.germination_period == "7 дней"
    assert product_grass_16_1.color == "Зеленый"


def test_product_smartphone_16_1_1():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    assert smartphone1 + smartphone2 == 2580000.0
    assert smartphone2 + smartphone3 == 2114000.0
    assert grass1 + grass2 == 16750.0
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1])
    assert category_smartphones.products_str == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
    ]
    category_smartphones.add_product(smartphone3)
    assert category_smartphones.products_str == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
    assert Category.product_count == 47
    assert category_grass.products_str == ["Газонная трава, 500.0 руб. Остаток: 20 шт."]
    category_grass.add_product(grass2)
    assert category_grass.products_str == [
        "Газонная трава, 500.0 руб. Остаток: 20 шт.",
        "Газонная трава 2, 450.0 руб. Остаток: 15 шт.",
    ]
