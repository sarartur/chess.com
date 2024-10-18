from tests.vcr import vcr


@vcr.use_cassette("get_current_daily_puzzle.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_current_daily_puzzle()
    validate_response(response)


@vcr.use_cassette("get_current_daily_puzzle.yaml")
def test_with_client(client):
    response = client.get_current_daily_puzzle()
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    puzzle = response.puzzle

    assert isinstance(puzzle.title, str)
    assert isinstance(puzzle.url, str)
    assert isinstance(puzzle.publish_time, int)
    assert isinstance(puzzle.fen, str)
    assert isinstance(puzzle.pgn, str)
    assert isinstance(puzzle.image, str)
