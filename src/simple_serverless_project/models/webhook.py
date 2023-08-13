from pydantic.dataclasses import dataclass


class WebhookMessage(dataclass):
    body: str
    request_id: str
    request_timestamp: str
