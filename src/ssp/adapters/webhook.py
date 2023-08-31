from ..models.webhook import WebhookMessage
from ..schema.aws import LambdaApiRequest, LambdaApiResponse


def wire_to_internal(event: LambdaApiRequest) -> WebhookMessage:
    """
    Convert the webhook request from the API Gateway format to the internal
    format.
    """
    return WebhookMessage(
        body=event['body'],
        request_id=event['headers']['X-Request-ID'],
        request_timestamp=event['headers']['X-Request-Timestamp'],
    )


def internal_to_wire(response: WebhookMessage) -> LambdaApiResponse:
    """
    Convert the webhook response from the internal format to the API Gateway
    format.
    """
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': response.body,
    }
