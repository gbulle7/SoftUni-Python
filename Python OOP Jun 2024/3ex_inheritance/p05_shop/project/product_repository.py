from typing import List, Optional
from project.product import Product


class ProductRepository:
    products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        # return next((p for p in self.products if p.name == product_name), None)
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        # product = self.find(product_name)
        # if product:
        #     self.products.remove(product)
        for product in self.products.copy():
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        all_products = f'\n'.join(f"{p.name}: {p.quantity}" for p in self.products)
        return all_products
