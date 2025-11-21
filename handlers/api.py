from aws_xray_sdk.core import patch_all  # type: ignore
from ssp import configurator
from ssp.domain.ports import ForBuyingProducts
from ssp.domain.ports.driven import (
    ForInteractingWithStorage,
    ForStoringCartInfo,
)
from ssp.domain.services import StoreService
from ssp.infrastructure.adapters.driven.mem_cart import InMemoryCartRepository
from ssp.infrastructure.adapters.driven.mem_storage import (
    InMemoryStoreRepository,
)

from handlers.mappers import get_amount_from_event, get_sku_from_event

patch_all()


@configurator(
    {
        ForInteractingWithStorage: InMemoryStoreRepository(
            {"random_sku": 10, "another_sku": 8, "unavailable_product": 0}
        ),
        ForStoringCartInfo: InMemoryCartRepository,
        ForBuyingProducts: StoreService,
    }
)
def check_stock(event, _, service):
    sku = get_sku_from_event(event)
    if not sku:
        return

    stock = service.check_stock(sku)
    return stock


@configurator(
    {
        ForInteractingWithStorage: InMemoryStoreRepository(
            {"random_sku": 10, "another_sku": 8, "unavailable_product": 0}
        ),
        ForStoringCartInfo: InMemoryCartRepository,
        ForBuyingProducts: StoreService,
    }
)
def add_to_cart(event, _, service):
    sku = get_sku_from_event(event)
    if not sku:
        return

    amount = get_amount_from_event(event)
    return service.add_to_cart(sku, amount)
