from dataclasses import dataclass

from ..ports.driven import ForInteractingWithStorage, ForStoringCartInfo
from ..ports.driving import ForBuyingProducts


@dataclass
class Configurator:
    store_service: ForBuyingProducts

    store_repository: ForInteractingWithStorage
    cart_repository: ForStoringCartInfo
