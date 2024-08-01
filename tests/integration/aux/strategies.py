import json

from hypothesis.strategies import composite, from_type
from pydantic.json import pydantic_encoder

from ssp.schema.aws import LambdaApiRequest


@composite
def event_with_json_body(draw, body):
    """Add any Pydantic dataclass as body of ApiEvent."""
    api_event = draw(from_type(LambdaApiRequest))
    api_body = draw(from_type(body))
    return {
        **api_event,
        'body': json.dumps(api_body, default=pydantic_encoder),
    }
