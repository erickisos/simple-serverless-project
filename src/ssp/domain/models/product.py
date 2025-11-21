from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Product:
    sku: str
    name: str
    unit_price: Decimal
    exp_date: Optional[datetime]

    @staticmethod
    def build(sku, name, unit_price, exp_date):
        if not sku or unit_price <= 0:
            return None
        return Product(sku, name, unit_price, exp_date)
