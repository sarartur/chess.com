from urllib3 import PoolManager
from certifi import where
import json
from typing import Dict, Optional, Union
from datetime import datetime

from chessdotcom.errors import ChessDotComError
from chessdotcom.response_parser import ChessDotComResponse


class _internal:
    """This class holds the methods and variables that are module-only.
    """
    _base_url = "https://api.chess.com/pub"
    _https = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=where())

    @classmethod
    def do_get_request(cls, path):
        """Private method that performs a 
        GET request to the chess.com API using the specified path.

        Parameters:
            path -- The URL path to use
        """
        r = cls._https.request(
            method='GET',
            url=cls._base_url + path
        )
        if r.status != 200:
            raise ChessDotComError(status_code=r.status)
        return r

    @staticmethod
    def resolve_date(year, month, date: datetime) -> (str, str):
        """Private method that resolves different date parameters 
        and returns 'yyyy' and 'mm'

        Parameters:
            year -- year
            month --month
            datetime -- datetime object
        """

        if (year is None) != (month is None):
            raise ValueError("You must provide both the year and the month, or a datetime.datetime object")
        if year is not None:
            if isinstance(year, int):
                year = str(year)
            if isinstance(month, int):
                month = str(month)
            return year, month.zfill(2)
        elif date is not None:
            return str(date.year), str(date.month).zfill(2)
        else:
            raise ValueError("You must provide both the year and the month, or a datetime.datetime object")


def get_player_profile(username: str) -> 'ChessDotComResponse':
    """Public method that returns additional details about a player

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(path = f"/player/{username}")
    return ChessDotComResponse(response_data = r.data)


def get_titled_players(title_abbrev: str) -> 'ChessDotComResponse':
    """Public method that returns list of titled-player usernames

    Parameters:
        title_abbrev -- abbreviation of chess title
    """

    r = _internal.do_get_request(path = f"/titled/{title_abbrev}")
    return ChessDotComResponse(response_data = r.data)


def get_player_stats(username: str) -> 'ChessDotComResponse':
    """Public method that returns ratings, win/loss,
    and other stats about a player's game play, tactics,
    lessons and Puzzle Rush score.

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(path = f"/player/{username}/stats")
    return ChessDotComResponse(response_data = r.data)


def is_player_online(username: str) -> bool:
    """Public method that returns True if user has been online
    in the last 5 minutes

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(path = f"/player/{username}/is-online")
    return ChessDotComResponse(response_data = r.data).json["online"]


def get_player_current_games(username: str) -> 'ChessDotComResponse':
    """Public method that returns an array
    of Daily Chess games that a player is currently playing

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(path = f"/player/{username}/games")
    return ChessDotComResponse(response_data = r.data)


def get_player_current_games_to_move(username: str) -> 'ChessDotComResponse':
    """Public method that returns an array of Daily Chess games
    where it is the player's turn to act

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(path = f"/player/{username}/games/to-move")
    return ChessDotComResponse(response_data = r.data)


def get_player_game_archives(username: str) -> 'ChessDotComResponse':
    """Public method that returns a array
    of monthly archives available for this player.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(path = f"/player/{username}/games/archives")
    return ChessDotComResponse(response_data = r.data)


def get_player_games_by_month(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None) -> 'ChessDotComResponse':
    """Public method that returns an array of
    live and daily Chess games that a player has finished.

    Parameters:
        username -- username of the player
        yyyy -- integer: the year (yyyy)
        mm -- integer: the month (mm)
    """
    yyyy, mm = _internal.resolve_date(year, month, datetime_obj)
    r = _internal.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}")
    return ChessDotComResponse(response_data = r.data)


def get_player_games_by_month_pgn(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None):
    """Public method that returns standard multi-game format PGN
    containing all games for a month

    Parameters:
        username -- username of the player
        year -- integer or string: the year
        month -- integer or string: the month
        date -- datetime.datetime: the date of the month
    You can pass in either the year and month or the datetime
    """
    yyyy, mm = _internal.resolve_date(year, month, datetime_obj)
    r = _internal.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}/pgn")
    return r.data


def get_player_clubs(username: str) -> 'ChessDotComResponse':
    """Public method that returns list of clubs the player
    is a member of.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(path = f"/player/{username}/clubs")
    return ChessDotComResponse(response_data = r.data)


def get_player_team_matches(username: str) -> 'ChessDotComResponse':
    """Public method that returns List of Team matches the player has attended,
    is participating or is currently registered.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(path = f"/player/{username}/matches")
    return ChessDotComResponse(response_data = r.data)


def get_player_tournaments(username: str) -> 'ChessDotComResponse':
    """List of tournaments the player is registered,
    is attending or has attended in the past.

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(path = f"/player/{username}/tournaments")
    return ChessDotComResponse(response_data = r.data)


def get_club_details(url_id: str) -> 'ChessDotComResponse':
    """Public method that returns additional details about a club

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(path = f"/club/{url_id}")
    return ChessDotComResponse(response_data = r.data)


def get_club_members(url_id: str) -> 'ChessDotComResponse':
    """Public method that return a list of club members

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(path = f"/club/{url_id}/members")
    return ChessDotComResponse(response_data = r.data)


def get_club_matches(url_id: str) -> 'ChessDotComResponse':
    """Public method that returns a list of daily and club matches

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(path = f"/club/{url_id}/matches")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_details(url_id: str) -> 'ChessDotComResponse':
    """Public method that returns details
    about a daily, live and arena tournament

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(path = f"/tournament/{url_id}")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_round(url_id: str, round_num: int) -> 'ChessDotComResponse':
    """Public method that returns details about a
    tournament's round.

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
        round_num -- the round of the tournament
    """
    r = _internal.do_get_request(path = f"/tournament/{url_id}/{round_num}")
    return ChessDotComResponse(response_data = r.data)


def get_tournament_round_group_details(url_id: str, round_num: int, group_num: int) -> 'ChessDotComResponse':
    """Public method that returns details about a tournament's
    round group

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
        round_num -- the round of the tournament
        group_num -- the group in the tournament
    """
    r = _internal.do_get_request(path = f"/tournament/{url_id}/{round_num}/{group_num}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match(match_id: int) -> 'ChessDotComResponse':
    """Public method that returns details about a team match
    and players playing that match

    Parameters:
        match_id -- the id of the match
    """
    r = _internal.do_get_request(path = f"/match/{match_id}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_board(match_id: int, board_num: int) -> 'ChessDotComResponse':
    """Public method that returns details about
    a team match board

    Parameters:
        match_id -- the id of the match
        board_num -- the number of the board
    """
    r = _internal.do_get_request(path = f"/match/{match_id}/{board_num}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_live(match_id: int) -> 'ChessDotComResponse':
    """Public method that returns details
    about a team match and players playing that match

    Parameters:
        match_id -- the id of the match
    """
    r = _internal.do_get_request(path = f"/match/live/{match_id}")
    return ChessDotComResponse(response_data = r.data)


def get_team_match_live_board(match_id: int, board_num: int) -> 'ChessDotComResponse':
    """Public method that returns details about a team match board

    Parameters:
        match_id -- the id of the match
        board_num -- the number of the board
    """
    r = _internal.do_get_request(path = f"/match/live/{match_id}/{board_num}")
    return ChessDotComResponse(response_data = r.data)


def get_country_details(iso: str) -> 'ChessDotComResponse':
    """Public method that returns additional details about a country

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(path = f"/country/{iso}")
    return ChessDotComResponse(response_data = r.data)


def get_country_players(iso: str) -> 'ChessDotComResponse':
    """Public method that returns list of usernames for players
    who identify themselves as being in this country.

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(path = f"/country/{iso}/players")
    return ChessDotComResponse(response_data = r.data)


def get_country_clubs(iso: str) -> 'ChessDotComResponse':
    """Public method that returns list of  URLs for clubs identified
    as being in or associated with this country.

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(path = f"/country/{iso}/clubs")
    return ChessDotComResponse(response_data = r.data)


def get_current_daily_puzzle() -> 'ChessDotComResponse':
    """Public method that returns information
    about the daily puzzle found in www.chess.com"""
    r = _internal.do_get_request("/puzzle")
    return ChessDotComResponse(response_data = r.data)


def get_random_daily_puzzle() -> 'ChessDotComResponse':
    """Public method that returns information about a
    randomly picked daily puzzle"""
    r = _internal.do_get_request(path = "/puzzle/random")
    return ChessDotComResponse(response_data = r.data)


def get_streamers() -> 'ChessDotComResponse':
    """Public method that returns information
    about Chess.com streamers."""
    r = _internal.do_get_request(path = "/streamers")
    return ChessDotComResponse(response_data = r.data)


def get_leaderboards() -> 'ChessDotComResponse':
    """Public method that returns information about top 50 player
    for daily and live games, tactics and lessons."""
    r = _internal.do_get_request(path = "/leaderboards")
    return ChessDotComResponse(response_data = r.data)
