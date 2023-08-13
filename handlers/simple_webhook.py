from simple_serverless_project.schema.aws import (
    LambdaApiRequest,
    LambdaApiResponse,
)
from simple_serverless_project.adapters.webhook import (
    internal_to_wire,
    wire_to_internal,
)
from simple_serverless_project.controllers.webhook import process


def webhook_handler(event: LambdaApiRequest, _) -> LambdaApiResponse:
    """
    This is a simple webhook handler that will return the event as a response.
    """
    return internal_to_wire(process(wire_to_internal(event)))
