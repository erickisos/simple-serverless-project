from ssp.domain.ports.driven import ForStoringCartInfo


class InMemoryCartRepository(ForStoringCartInfo):
    cart = {}

    def update_cart(self, sku: str, new_amount: int) -> bool | None:
        try:
            self.cart[sku] = new_amount
            return True
        except Exception:
            return False

    def check_amount(self, sku: str) -> int | None:
        return self.cart.get(sku, 0)
