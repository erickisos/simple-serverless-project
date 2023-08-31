from ..adapters.webhook import internal_to_wire, wire_to_internal
from ..controllers.webhook import process
from ..models.context import Context


def webhook(event, context: Context):
    message = wire_to_internal(event)
    response = process(message, context)
    return internal_to_wire(response)
