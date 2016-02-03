import json
from tornado.httpclient import AsyncHTTPClient
from tornado import gen


DEFAULT_API_ENDPOINT = "https://mandrillapp.com/api/1.0/messages/send.json"


@gen.coroutine
def send(api_key, recipient, subject,
         fromemail, fromname, message,
         name='You', extra={}, mandrill_api=DEFAULT_API_ENDPOINT):
    http_client = AsyncHTTPClient()
    request_data = {
        "key": api_key,
        "message": {
            "html": message,
            "to": {
                "email": recipient,
                "type": "to",
                "name": name
            }
        }
    }
    request_data.merge(extra)
    response = yield http_client.fetch(
        mandrill_api,
        method='POST',
        body=json.dumps(request_data)
    )
    if response.code != 200:
        return 'lolnotsent'
    else:
        jresponse = json.loads(response.body)
        return jresponse
