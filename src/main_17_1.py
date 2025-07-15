class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"


class Category:
    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def __str__(self):
        products_str = ", ".join(str(product) for product in self.products)
        return f"{self.name}, {self.description}, Products: [{products_str}]"

    def middle_price(self):
        try:
            sum_price = 0
            count_product = 0
            for product in self.products:
                sum_price += product.price
                count_product += 1
            middle_price_product = round(sum_price / count_product, 2)
            return middle_price_product
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
