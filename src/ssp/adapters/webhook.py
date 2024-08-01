from ..models.webhook import WebhookMessage
from ..schema.aws import LambdaApiRequest, LambdaApiResponse


def wire_to_internal(event: LambdaApiRequest) -> WebhookMessage:
    """Convert the webhook request from the API Gateway format to the internal
    format."""
    return WebhookMessage(
        body=event['body'],
        request_id=event['headers'].get('X-Request-ID') or '',
        request_timestamp=event['headers'].get('X-Request-Timestamp') or '',
    )


def internal_to_wire(response: WebhookMessage) -> LambdaApiResponse:
    """Convert the webhook response from the internal format to the API Gateway
    format."""
    return {
        'statusCode': 200,
        'headers': {'content-type': 'application/json'},
        'body': response.body,
    }
