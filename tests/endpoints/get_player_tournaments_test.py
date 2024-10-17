from tests.vcr import vcr


@vcr.use_cassette("get_player_tournaments.yaml")
def test_with_endpoints(endpoints):
    response = endpoints.get_player_tournaments(username="fabianocaruana")
    validate_response(response)


@vcr.use_cassette("get_player_tournaments.yaml")
def test_with_client(client):
    response = client.get_player_tournaments(username="fabianocaruana")
    validate_response(response)


def validate_response(response):
    tournaments = response.tournaments
    for tournament in tournaments.finished:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.wins, int)
        assert isinstance(tournament.losses, int)
        assert isinstance(tournament.draws, int)
        assert isinstance(tournament.placement, int)
        assert isinstance(tournament.status, str)
        assert isinstance(tournament.total_players, int)
        assert isinstance(tournament.time_class, str)
        assert isinstance(tournament.type, str)

    for tournament in tournaments.in_progress:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)

    for tournament in tournaments.registered:
        assert isinstance(tournament.url, str)
        assert isinstance(tournament.id, str)
        assert isinstance(tournament.status, str)
