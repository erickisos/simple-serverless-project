from abc import ABC

from ..models import Ticket


class ForBuyingProducts(ABC):
    def check_stock(self, sku: str) -> int | None:
        ...

    def add_to_cart(self, sku: str, amount: int) -> bool | None:
        ...

    def remove_from_cart(self, sku: str, amount: int) -> bool | None:
        ...

    def checkout(self) -> Ticket | None:
        ...
