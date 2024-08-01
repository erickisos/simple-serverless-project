import json

from hypothesis import given
from pytest import raises

from ssp.models.context import Context
from ssp.models.webhook import WebhookMessage
from ssp.ports.http_inputs import webhook
from ssp.schema.aws import LambdaApiRequest

from ..aux.strategies import event_with_json_body

mock_config: Context = {
    'some-config': 'some-value'
}


@given(event=event_with_json_body(WebhookMessage))
def test_webhook(event: LambdaApiRequest):
    """Test that no matter which event we receive, the answer is the same"""
    expected = {
        'headers': {
            'content-type': 'application/json',
        },
        'statusCode': 200,
        'body': event.get('body'),
    }
    actual = webhook(event, mock_config)
    assert expected == actual
