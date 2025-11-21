from dataclasses import dataclass
from decimal import Decimal

from .product import Product


@dataclass
class Ticket:
    id: str
    products: dict[Product, Decimal]

    @property
    def total(self) -> Decimal:
        return sum(
            product.unit_price * quantity
            for product, quantity in self.products.items()
        )
