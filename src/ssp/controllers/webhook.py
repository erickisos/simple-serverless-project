from ..models.context import Context
from ..models.webhook import WebhookMessage


def process(message: WebhookMessage, _: Context) -> WebhookMessage:
    """
    Process the webhook message.
    """
    return message
