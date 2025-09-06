
from aws_xray_sdk.core import patch_all  # type: ignore

from ssp.models.context import Context
from ssp.ports.http_inputs import webhook
from ssp.schema.aws import LambdaApiRequest, LambdaApiResponse

patch_all()

# Lo que sea que necesites inyectar en tu aplicación
config: Context = dict()


def webhook_handler(event: LambdaApiRequest, _) -> LambdaApiResponse:
    return webhook(event, config)
