from typing import Dict, Literal, Text, TypedDict


class LambdaApiRequest(TypedDict):
    headers: Dict
    body: Text
    path: Text
    pathParameters: Dict
    queryStringParameters: Dict


Header = Literal[
    'X-Request-ID', 'X-Request-Timestamp', 'content-type', 'Content-Type'
]


class LambdaApiResponse(TypedDict):
    statusCode: int
    headers: Dict[Header, Text]
    body: Text
