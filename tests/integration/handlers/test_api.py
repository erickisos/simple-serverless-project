from handlers.api import check_stock


@pytest.mark.parametrize("event, expected", [({"body": {"sku": "SKU"}}, 3)])
def test_check_stock(event, expected):
    event = {"body": {"sku": "SKU"}}
    actual = check_stock(event, None)
    assert expected == actual
