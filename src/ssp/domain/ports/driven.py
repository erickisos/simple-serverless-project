from abc import ABC

from ..models.product import Product


class ForInteractingWithStorage(ABC):
    def get_product(self, sku: str) -> tuple[Product | None, int]:
        ...

    def pick_product(self, sku: str, amount: int) -> Product | None:
        ...


class ForStoringCartInfo(ABC):
    def update_cart(self, sku: str, new_amount: int) -> bool | None:
        ...

    def check_amount(self, sku: str) -> int | None:
        ...
