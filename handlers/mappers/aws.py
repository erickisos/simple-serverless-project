def get_sku_from_event(event) -> str | None:
    return event.get('body', {}).get('sku', None)


def get_amount_from_event(event) -> int:
    return event.get('body', {}).get('amount', 0)
