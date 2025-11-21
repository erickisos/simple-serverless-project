from ..models.ticket import Ticket
from ..ports.driven import ForInteractingWithStorage, ForStoringCartInfo
from ..ports.driving import ForBuyingProducts

from decimal import Decimal


class StoreService(ForBuyingProducts):
    def __init__(
        self,
        store_repository: ForInteractingWithStorage,
        cart_repository: ForStoringCartInfo,
    ):
        self.cart_repository = cart_repository
        self.store_repository = store_repository

    def check_stock(self, sku: str) -> Decimal | None:
        [product, stock] = self.store_repository.get_product(sku)
        return None if not product else stock

    def add_to_cart(self, sku: str, amount: Decimal) -> bool | None:
        product = self.store_repository.pick_product(sku, amount)
        if not product:
            return None

        current_amount = self.cart_repository.check_amount(sku) or 0
        return self.cart_repository.update_cart(sku, amount + current_amount)

    def remove_from_cart(self, sku: str, amount: Decimal) -> bool | None:
        raise NotImplementedError("This method is not implemented yet")

    def checkout(self) -> Ticket | None:
        raise NotImplementedError("This method is not implemented yet")
