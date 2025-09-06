import pytest

from ssp.adapters.webhook import internal_to_wire, wire_to_internal
from ssp.models.webhook import WebhookMessage


@pytest.mark.parametrize(
    'webhook_message, wired',
    [
        (
            WebhookMessage(
                body='body',
                request_id='request_id',
                request_timestamp='request_timestamp',
            ),
            {
                'body': 'body',
                'headers': {
                    'X-Request-ID': 'request_id',
                    'X-Request-Timestamp': 'request_timestamp',
                },
            },
        ),
    ],
)
def test_wire_to_internal(webhook_message, wired):
    value = wire_to_internal(wired)
    assert webhook_message == value


@pytest.mark.parametrize(
    'webhook_message, wired',
    [
        (
            WebhookMessage(
                body='body',
                request_id='request_id',
                request_timestamp='request_timestamp',
            ),
            {
                'body': 'body',
                'headers': {
                    'content-type': 'application/json',
                },
                'statusCode': 200,
            },
        ),
    ],
)
def test_internal_to_wire(webhook_message, wired):
    value = internal_to_wire(webhook_message)
    assert wired == value
