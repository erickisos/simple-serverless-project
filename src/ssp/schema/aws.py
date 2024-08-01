from typing import Dict, Literal, Text, TypedDict

Header = Literal[
    'X-Request-ID', 'X-Request-Timestamp', 'content-type', 'Content-Type'
]


class LambdaApiRequest(TypedDict):
    headers: Dict[Header, Text]
    body: Text
    path: Text
    pathParameters: Dict
    queryStringParameters: Dict


class LambdaApiResponse(TypedDict):
    statusCode: int
    headers: Dict[Header, Text]
    body: Text
