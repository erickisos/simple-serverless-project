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
