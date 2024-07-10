from project.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, quantity=10)
    # def __init__(self, name):
    #     self.name = name
    #     self.quantity = 10
