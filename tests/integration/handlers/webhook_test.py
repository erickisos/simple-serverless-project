from hypothesis import given

from ..aux.strategies import event_with_json_body

# @given(event=event_with_json_body(WebhookMessage))
# def test_webhook(event: LambdaApiRequest):
#     """Test that no matter which event we receive, the answer is the same."""
#     expected = {
#         'headers': {
#             'content-type': 'application/json',
#         },
#         'statusCode': 200,
#         'body': event.get('body'),
#     }
#     actual = webhook(event, mock_config)
#     assert expected == actual
