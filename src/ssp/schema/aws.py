from typing import Dict, Text, TypedDict


class LambdaApiRequest(TypedDict):
    headers: Dict
    body: Text
    path: Text
    pathParameters: Dict
    queryStringParameters: Dict


class LambdaApiResponse(TypedDict):
    statusCode: int
    body: Text
