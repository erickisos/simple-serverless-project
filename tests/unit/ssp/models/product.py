from decimal import Decimal

import pytest

from ssp.domain.models.product import Product


@pytest.mark.parametrize(
    "sku,name,unit_price,exp_date, expected",
    [
        # Should fail creating a product if the sku is empty
        ("", "", Decimal(1.0), None, None),
        # Should fail if the unit price is negative.
        ("SKU", "Name", Decimal(-1.0), None, None),
        # Should work if everythin seems correct
        (
            "SKU",
            "Name",
            Decimal(1.0),
            None,
            Product("SKU", "Name", Decimal(1.0), None),
        ),
    ],
)
def test_product_creation(sku, name, unit_price, exp_date, expected):
    product = Product.build(sku, name, unit_price, exp_date)

    assert product == expected
