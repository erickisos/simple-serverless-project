
from aws_xray_sdk.core import patch_all  # type: ignore
from ssp.domain.ports import ForBuyingProducts
from ssp.domain.ports.driven import (ForInteractingWithStorage,
                                     ForStoringCartInfo)
from ssp.domain.services import StoreService
from ssp.infrastructure.adapters.driven.mem_cart import InMemoryCartRepository
from ssp.infrastructure.adapters.driven.mem_storage import \
    InMemoryStoreRepository

from handlers.mappers import get_amount_from_event, get_sku_from_event

patch_all()

store_repository: ForInteractingWithStorage = InMemoryStoreRepository({
    'random_sku': 10,
    'another_sku': 8,
    'unbearable_product': 0
})
cart_repository: ForStoringCartInfo = InMemoryCartRepository()
service: ForBuyingProducts = StoreService(store_repository, cart_repository)


def check_stock(event, _):
    sku = get_sku_from_event(event)
    if not sku:
        return

    stock = service.check_stock(sku)
    return stock

def add_to_cart(event, _):
    sku = get_sku_from_event(event)
    if not sku:
        return

    amount = get_amount_from_event(event)
    return service.add_to_cart(sku, amount)
