from pytest import fixture

from ssp.adapters.webhook import (
    internal_to_wire,
    wire_to_internal,
)
import pytest
from ssp.models.webhook import WebhookMessage


@fixture
def webhook_message(body, request_id, request_timestamp):
    return WebhookMessage(
        body=body,
        request_id=request_id,
        request_timestamp=request_timestamp,
    )


@fixture
def wired(body, headers):
    return {
        'body': body,
        'headers': headers,
    }


@pytest.mark.parametrize(
    'body, request_id, request_timestamp, headers',
    [
        (
            '{"foo": "bar"}',
            '123',
            '456',
            {'X-Request-ID': '123', 'X-Request-Timestamp': '456'},
        )
    ],
    indirect=True,
)
def test_wire_to_internal(webhook_message, wired):
    value = wire_to_internal(wired)
    assert webhook_message == value
