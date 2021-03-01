from urllib3 import PoolManager
from certifi import where
import json
from typing import Dict, Optional, Union
from datetime import datetime

from chessdotcom.errors import ChessDotComError
from chessdotcom.response import ChessDotComResponse
from chessdotcom.utils import resolve_date


class Client:
    """Responsible for interacting with the API.
    """
    _base_url = "https://api.chess.com/pub"
    _https = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=where())
    headers = {}

    @classmethod
    def do_get_request(cls, path):
        """Private method that performs a 
        GET request to the chess.com API using the specified path.

        Parameters:
            path -- The URL path to use
        """
        r = cls._https.request(
            method='GET',
            url=cls._base_url + path,
            headers=cls.headers
        )
        if r.status != 200:
            raise ChessDotComError(status_code=r.status)
        return r

def get_player_profile(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains information about the chess.com user.
    """
    r = Client.do_get_request(path = f"/player/{username}")
    return ChessDotComResponse(response_data = r.data)


def get_titled_players(title_abbrev: str):
    """
    :param title_abbrev: abbreviation of chess title.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of usernames who have the specified title.
    """
    r = Client.do_get_request(path = f"/titled/{title_abbrev}")
    return ChessDotComResponse(response_data = r.data)


def get_player_stats(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains ratings, win/loss,
                and other stats about a player's game play, tactics,
                lessons and Puzzle Rush score.
    """
    r = Client.do_get_request(path = f"/player/{username}/stats")
    return ChessDotComResponse(response_data = r.data)


def is_player_online(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains information about whether or not the player is online. 
    """
    r = Client.do_get_request(path = f"/player/{username}/is-online")
    return ChessDotComResponse(response_data = r.data)


def get_player_current_games(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of Daily Chess games that a player is currently playing.

    """
    r = Client.do_get_request(path = f"/player/{username}/games")
    return ChessDotComResponse(response_data = r.data)


def get_player_current_games_to_move(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of Daily Chess games where it is the player's turn to act.

    """
    r = Client.do_get_request(path = f"/player/{username}/games/to-move")
    return ChessDotComResponse(response_data = r.data)


def get_player_game_archives(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of monthly archives available for this player.

    """
    r = Client.do_get_request(path = f"/player/{username}/games/archives")
    return ChessDotComResponse(response_data = r.data)


def get_player_games_by_month(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None):
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of live and daily Chess games that a player has finished.

    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    r = Client.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}")
    return ChessDotComResponse(response_data = r.data)


def get_player_games_by_month_pgn(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None):
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :returns: ``ChessDotComResponse`` object. The json property of the object contains 
                standard multi-game format PGN containing all games for a month.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    r = Client.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}/pgn")
    return ChessDotComResponse(response_data = json.dumps({
            'pgn': r.data.decode('utf-8')
        }).encode('utf-8'))


def get_player_clubs(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of clubs the player is a member of.
    """
    r = Client.do_get_request(path = f"/player/{username}/clubs")
    return ChessDotComResponse(response_data = r.data)


def get_player_team_matches(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of team matches the player has attended,
                is participating or is currently registered.
    """
    r = Client.do_get_request(path = f"/player/{username}/matches")
    return ChessDotComResponse(response_data = r.data)


def get_player_tournaments(username: str):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    r = Client.do_get_request(path = f"/player/{username}/tournaments")
    return ChessDotComResponse(response_data = r.data)


def get_club_details(url_id: str):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains additional details about a club.
    """
    r = Client.do_get_request(path = f"/club/{url_id}")
    return ChessDotComResponse(response_data = r.data)


def get_club_members(url_id: str):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of club members.
    """
    r = Client.do_get_request(path = f"/club/{url_id}/members")
    return ChessDotComResponse(response_data = r.data)


def get_club_matches(url_id: str):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of daily and club matches.
    """
    r = Client.do_get_request(path = f"/club/{url_id}/matches")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_details(url_id: str):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a daily, live and arena tournament.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_round(url_id: str, round_num: int):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a tournament's round.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}/{round_num}")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_round_group_details(url_id: str, round_num: int, group_num: int):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param group_num: the group in the tournament.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a tournament's round group.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}/{round_num}/{group_num}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match(match_id: int):
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a team match and players playing that match.
    """
    r = Client.do_get_request(path = f"/match/{match_id}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_board(match_id: int, board_num: int):
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a team match board.
    """
    r = Client.do_get_request(path = f"/match/{match_id}/{board_num}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_live(match_id: int):
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a team match and players playing that match.
    """
    r = Client.do_get_request(path = f"/match/live/{match_id}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_live_board(match_id: int, board_num: int):
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains details about a team match board.
    """
    r = Client.do_get_request(path = f"/match/live/{match_id}/{board_num}")
    return ChessDotComResponse(response_data = r.data)


def get_country_details(iso: str):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains additional details about a country.
    """
    r = Client.do_get_request(path = f"/country/{iso}")
    return ChessDotComResponse(response_data = r.data)


def get_country_players(iso: str):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of usernames for players
                who identify themselves as being in this country.
    """
    r = Client.do_get_request(path = f"/country/{iso}/players")
    return ChessDotComResponse(response_data = r.data)


def get_country_clubs(iso: str):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object. The json property of the object
                contains a list of URLs for clubs identified
                as being in or associated with this country.
    """
    r = Client.do_get_request(path = f"/country/{iso}/clubs")
    return ChessDotComResponse(response_data = r.data)


def get_current_daily_puzzle():
    """
    :returns: ``ChessDotComResponse`` object. The json property of the object contains
                information about the daily puzzle found in www.chess.com.
    """
    r = Client.do_get_request("/puzzle")
    return ChessDotComResponse(response_data = r.data)


def get_random_daily_puzzle():
    """
    :returns: ``ChessDotComResponse`` object. The json property of the object contains 
                information about a randomly picked daily puzzle.
    """
    r = Client.do_get_request(path = "/puzzle/random")
    return ChessDotComResponse(response_data = r.data)


def get_streamers():
    """
    :returns: ``ChessDotComResponse`` object. The json property of the object contains 
                information about Chess.com streamers.
    """
    r = Client.do_get_request(path = "/streamers")
    return ChessDotComResponse(response_data = r.data)


def get_leaderboards():
    """
    :returns: ``ChessDotComResponse`` object. The json property of the object contains 
                information about top 50 player for daily and live games, tactics and lessons.
    """
    r = Client.do_get_request(path = "/leaderboards")
    return ChessDotComResponse(response_data = r.data)
