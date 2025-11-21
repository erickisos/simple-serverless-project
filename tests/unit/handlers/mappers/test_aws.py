from decimal import Decimal
import pytest

from handlers.mappers.aws import get_amount_from_event, get_sku_from_event


@pytest.mark.parametrize(
    "event,expected", [({"body": {"sku": "SKU"}}, "SKU"), ({}, None)]
)
def test_sku_from_event(event, expected):
    actual = get_sku_from_event(event)
    assert expected == actual


@pytest.mark.parametrize(
    "event",
    "expected",
    [
        ({"body": {"amount": 0}}, Decimal("0")),
        ({"body": {"amount": -1}}, Decimal("-1")),
    ],
)
def test_amount_from_event(event, expected):
    actual = get_amount_from_event(event)
    assert expected == actual
