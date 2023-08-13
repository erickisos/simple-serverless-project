from simple_serverless_project.models.webhook import WebhookMessage


def process(message: WebhookMessage) -> WebhookMessage:
    """
    Process the webhook message.
    """
    return message
