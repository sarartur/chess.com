from urllib3 import PoolManager
from certifi import where
import json
from typing import Dict

from chessdotcom.errors import ChessDotComError


class _internal:
    """
    This class holds the methods and variables that are module-only.
    """
    _api_base = "https://api.chess.com/pub"
    _https_requester = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=where())

    @staticmethod
    def do_get_request(path):
        """Preforms a GET request to the chess.com API using the specified path.

        :param path The URL path to use"""
        r = _internal._https_requester.request(
            method='GET',
            url=_internal._api_base + path
        )
        if r.status != 200:
            raise ChessDotComError(status_code=r.status)
        return r


def get_player_profile(username: str) -> Dict:
    """Public method that returns additional details about a player

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(f"/player/{username}")
    return json.loads(r.data.decode('utf-8'))


def get_titled_players(title_abbrev: str) -> Dict:
    """Public method that returns list of titled-player usernames

    Parameters:
        title_abbrev -- abbreviation of chess title
    """

    r = _internal.do_get_request(f"/titled/{title_abbrev}")
    return json.loads(r.data.decode('utf-8'))


def get_player_stats(username: str) -> Dict:
    """Public method that returns ratings, win/loss,
    and other stats about a player's game play, tactics,
    lessons and Puzzle Rush score.

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(f"/player/{username}/stats")
    return json.loads(r.data.decode('utf-8'))


def is_player_online(username: str) -> Dict:
    """Public method that returns True if user has been online
    in the last 5 minutes

    Parameters:
        username -- username of the player"""

    r = _internal.do_get_request(f"/player/{username}/is-online")
    return json.loads(r.data.decode('utf-8'))


def get_player_current_games(username: str) -> Dict:
    """Public method that returns an array
    of Daily Chess games that a player is currently playing

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(f"/player/{username}/games")
    return json.loads(r.data.decode('utf-8'))


def get_player_current_games_to_move(username: str) -> Dict:
    """Public method that returns an array of Daily Chess games
    where it is the player's turn to act

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(f"/player/{username}/games/to-move")
    return json.loads(r.data.decode('utf-8'))


def get_player_game_archives(username: str) -> Dict:
    """Public method that returns a array
    of monthly archives available for this player.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(f"/player/{username}/games/archives")
    return json.loads(r.data.decode('utf-8'))


def get_player_games_by_month(username: str, yyyy: str, mm: str) -> Dict:
    """Public method that returns an array of
    live and daily Chess games that a player has finished.

    Parameters:
        username -- username of the player
        yyyy -- integer: the year (yyyy)
        mm -- integer: the month (mm)
    """
    r = _internal.do_get_request(f"/player/{username}/games/{yyyy}/{mm}")
    return json.loads(r.data.decode('utf-8'))


def get_player_games_by_month_pgn(username: str, yyyy: str, mm: str):
    """Public method that returns standard multi-game format PGN
    containing all games for a month

    Parameters:
        username -- username of the player
        yyyy -- intger: the year (yyyy)
        mm -- integer: the month (mm)
    """

    r = _internal.do_get_request(f"/player/{username}/games/{yyyy}/{mm}/pgn")
    return r.data


def get_player_clubs(username: str) -> Dict:
    """Public method that returns list of clubs the player
    is a member of.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(f"/player/{username}/clubs")
    return json.loads(r.data.decode('utf-8'))


def get_player_team_matches(username: str) -> Dict:
    """Public method that returns List of Team matches the player has attended,
    is participating or is currently registered.

    Parameters:
        username -- username of the player
    """
    r = _internal.do_get_request(f"/player/{username}/matches")
    return json.loads(r.data.decode('utf-8'))


def get_player_tournaments(username: str) -> Dict:
    """List of tournaments the player is registered,
    is attending or has attended in the past.

    Parameters:
        username -- username of the player
    """

    r = _internal.do_get_request(f"/player/{username}/tournaments")
    return json.loads(r.data.decode('utf-8'))


def get_club_details(url_id: str) -> Dict:
    """Public method that returns additional details about a club

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(f"/club/{url_id}")
    return json.loads(r.data.decode('utf-8'))


def get_club_members(url_id: str) -> Dict:
    """Public method that return a list of club members

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(f"/club/{url_id}/members")
    return json.loads(r.data.decode('utf-8'))


def get_club_matches(url_id: str) -> Dict:
    """Public method that returns a list of daily and club matches

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(f"/club/{url_id}/matches")
    return json.loads(r.data.decode('utf-8'))


def get_tournament_details(url_id: str) -> Dict:
    """Public method that returns details
    about a daily, live and arena tournament

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
    """
    r = _internal.do_get_request(f"/tournament/{url_id}")
    return json.loads(r.data.decode('utf-8'))


def get_tournament_round(url_id: str, round_num: int) -> Dict:
    """Public method that returns details about a
    tournament's round.

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
        round_num -- the round of the tournament
    """
    r = _internal.do_get_request(f"/tournament/{url_id}/{round_num}")
    return json.loads(r.data.decode('utf-8'))


def get_tournament_round_group_details(url_id: str, round_num: int, group_num: int) -> Dict:
    """Public method that returns details about a tournament's
    round group

    Parameters:
        url_id -- URL for the club's web page on www.chess.com.
        round_num -- the round of the tournament
        group_num -- the group in the tournament
    """
    r = _internal.do_get_request(f"/tournament/{url_id}/{round_num}/{group_num}")
    return json.loads(r.data.decode('utf-8'))


def get_team_match(match_id: int) -> Dict:
    """Public method that returns details about a team match
    and players playing that match

    Parameters:
        match_id -- the id of the match
    """
    r = _internal.do_get_request(f"/match/{match_id}")
    return json.loads(r.data.decode('utf-8'))


def get_team_match_board(match_id: int, board_num: int) -> Dict:
    """Public method that returns details about
    a team match board

    Parameters:
        match_id -- the id of the match
        board_num -- the number of the board
    """
    r = _internal.do_get_request(f"/match/{match_id}/{board_num}")
    return json.loads(r.data.decode('utf-8'))


def get_team_match_live(match_id: int) -> Dict:
    """Public method that returns details
    about a team match and players playing that match

    Parameters:
        match_id -- the id of the match
    """
    r = _internal.do_get_request(f"/match/live/{match_id}")
    return json.loads(r.data.decode('utf-8'))


def get_team_match_live_board(match_id: int, board_num: int) -> Dict:
    """Public method that returns details about a team match board

    Parameters:
        match_id -- the id of the match
        board_num -- the number of the board
    """
    r = _internal.do_get_request(f"/match/live/{match_id}/{board_num}")
    return json.loads(r.data.decode('utf-8'))


def get_country_details(iso: str) -> Dict:
    """Public method that returns additional details about a country

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(f"/country/{iso}")
    return json.loads(r.data.decode('utf-8'))


def get_country_players(iso):
    """Public method that returns list of usernames for players
    who identify themselves as being in this country.

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(f"/country/{iso}/players")
    return json.loads(r.data.decode('utf-8'))


def get_country_clubs(iso: str) -> Dict:
    """Public method that returns list of  URLs for clubs identified
    as being in or associated with this country.

    Parameters:
        iso -- country's 2-character ISO 3166 code
    """
    r = _internal.do_get_request(f"/country/{iso}/clubs")
    return json.loads(r.data.decode('utf-8'))


def get_current_daily_puzzle() -> Dict:
    """Public method that returns information
    about the daily puzzle found in www.chess.com"""
    r = _internal.do_get_request("/puzzle")
    return json.loads(r.data.decode('utf-8'))


def get_random_daily_puzzle() -> Dict:
    """Public method that returns information about a
    randomly picked daily puzzle"""
    r = _internal.do_get_request("/puzzle/random")
    return json.loads(r.data.decode('utf-8'))


def get_streamers():
    """Public method that returns information
    about Chess.com streamers."""
    r = _internal.do_get_request("/streamers")
    return json.loads(r.data.decode('utf-8'))


def get_leaderboards():
    """Public method that returns information about top 50 player
    for daily and live games, tactics and lessons."""
    r = _internal.do_get_request("/leaderboards")
    return json.loads(r.data.decode('utf-8'))
