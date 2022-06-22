import sys
import asyncio

is_main = __name__ == "__main__"
if is_main:
    sys.path.append("../")

from chessdotcom.types import Resource, ChessDotComError
from chessdotcom import Client

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

RATE_LIMIT_RETRIES = 4


def configure_client():
    Resource._base_url = "https://mock.codes"
    Client.rate_limit_handler.retries = RATE_LIMIT_RETRIES
    Client.rate_limit_handler.tts = 1


@Client.endpoint
def sample_endpoint(**kwargs):
    return Resource(uri="/429", request_config=kwargs)


def test_sync():
    Client.aio = False
    configure_client()

    counter = {"count": 0}

    def count_function(r, *args, **kwargs):
        counter["count"] = counter["count"] + 1

    try:
        sample_endpoint(hooks={"response": count_function})
    except ChessDotComError:
        pass

    assert counter["count"] == RATE_LIMIT_RETRIES + 1


def test_async():
    configure_client()
    Client.aio = True
    try:
        asyncio.run(sample_endpoint())
    except Exception as err:
        assert isinstance(err, ChessDotComError)


if is_main:
    test_sync()
    test_async()
