from tests.vcr import vcr


@vcr.use_cassette("get_player_game_archives.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_game_archives(username="afgano29")
    validate_response(response)


@vcr.use_cassette("get_player_game_archives.yaml")
def test_with_client(client):
    response = client.get_player_game_archives(username="afgano29")
    validate_response(response)


def validate_response(response):
    assert isinstance(response.json, dict)
    assert isinstance(response.text, str)

    archives = response.archives
    assert all(isinstance(url, str) for url in archives)
