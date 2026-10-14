# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12

from task33 import Product


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    @property
    def total_price(self):
        return sum(product.price for product in self.products)


if __name__ == "__main__":
    book = Product("Book", 10)
    pen = Product("Pen", 2)
    order = Order()
    order.add_product(book)
    order.add_product(pen)
    print(f"Общая стоимость: {order.total_price}")  # 12
    