class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return list(filter(lambda item: item.startswith(first_letter), self.products))
        # return [product for product in self.products if product[0].lower() == first_letter.lower()]

    def __repr__(self):
        sorted_catalogue = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{sorted_catalogue}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
