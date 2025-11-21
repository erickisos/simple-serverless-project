from decimal import Decimal

from ....domain.models.product import Product
from ....domain.ports.driven import ForInteractingWithStorage



class InMemoryStoreRepository(ForInteractingWithStorage):
    stock_manager = {}

    def __init__(self, initial_products: dict[str, int]):
        self.stock_manager = {
            sku:  quantity
            for sku, quantity
            in initial_products.items()
        }

    def get_product(self, sku: str) -> tuple[Product | None, int]:
        if sku not in self.stock_manager:
            return (None, 0)

        stock = self.stock_manager.get(sku, 0)
        product = Product(sku, sku, Decimal('1.0'), None)

        return (product, stock)

    def pick_product(self, sku: str, amount: int) -> Product | None:
        available_stock = self.stock_manager.get(sku, 0)

        if available_stock < amount:
            return None

        self.stock_manager[sku] = available_stock - amount
        return Product(sku, sku, Decimal('1.0'), None)
