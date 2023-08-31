from pydantic.dataclasses import dataclass


@dataclass
class WebhookMessage:
    body: str
    request_id: str
    request_timestamp: str
