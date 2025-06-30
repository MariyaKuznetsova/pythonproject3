class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        name = dict_product["name"]
        description = dict_product["description"]
        price = dict_product["price"]
        quantity = dict_product["quantity"]
        return Product(name, description, price, quantity)

    @property
    def get_price(self):  # геттер
        return self.__price

    @get_price.setter
    def set_price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


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
        self.__products = products

        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def add_product(self, product):
        self.__products.append(product)
        Category.category_count += 1
        Category.product_count += product.quantity

    @property
    def products_str(self):
        product_new_list = []
        for product in self.__products:
            product_new = f"{product.name}, {product.get_price} руб. Остаток: {product.quantity} шт."
            product_new_list.append(product_new)
        return product_new_list


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products_str)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products_str)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.get_price)
    print(new_product.quantity)

    new_product.set_price = 800
    print(new_product.set_price)

    new_product.set_price = -100
    print(new_product.set_price)
    new_product.set_price = 0
    print(new_product.set_price)
