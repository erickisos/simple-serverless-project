
from dataclasses import dataclass
from decimal import Decimal

from .product import Product


@dataclass
class Ticket:
    id: str
    products: dict[Product, int]

    @property
    def total(self) -> Decimal:
        total = Decimal('0')
        for product, quantity in self.products.items():
            total += product.unit_price * Decimal(quantity)
        return total
