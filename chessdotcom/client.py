import requests
import json
from typing import Dict, Optional, Union
from datetime import datetime

from chessdotcom.errors import ChessDotComError
from chessdotcom.response import ChessDotComResponse
from chessdotcom.utils import resolve_date


class Client:
    """
    Client for Chess.com Public API. The client is only responsible for making calls.

    :cvar headers: Dictionary containing request headers.
    :cvar proxies: Dictionary containing proxy information.
    """
    _base_url = "https://api.chess.com/pub"
    headers = {}
    proxies = {}

    @classmethod
    def do_get_request(cls, path: str, **kwargs):
        r = requests.get(
            url = Client._base_url + path, 
            headers = cls.headers,
            proxies = cls.proxies,
            **kwargs
        )
        if r.status_code != 200:
            raise ChessDotComError(status_code = r.status_code, response_text = r.text)
        return r

def get_player_profile(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing information about
                the player's profile.
    """
    r = Client.do_get_request(path = f"/player/{username}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'player')


def get_titled_players(title_abbrev: str, **kwargs):
    """
    :param title_abbrev: abbreviation of chess title.
    :returns: ``ChessDotComResponse`` object containing a list of usernames.
    """
    r = Client.do_get_request(path = f"/titled/{title_abbrev}", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_stats(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing information about the
                plyers's ratings, win/loss, and other stats.
    """
    r = Client.do_get_request(path = f"/player/{username}/stats", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'stats')


def is_player_online(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing infomation about
                whether or not a player is online 
    """
    r = Client.do_get_request(path = f"/player/{username}/is-online", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_current_games(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                that a player is currently playing.
    """
    r = Client.do_get_request(path = f"/player/{username}/games", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_current_games_to_move(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games 
                where it is the player's turn to act.
    """
    r = Client.do_get_request(path = f"/player/{username}/games/to-move", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_game_archives(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a 
                list of monthly archives available for this player.
    """
    r = Client.do_get_request(path = f"/player/{username}/games/archives", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_games_by_month(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None, **kwargs):
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :returns: ``ChessDotComResponse`` object containing a list of live and daily 
                Chess games that a player has finished.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    r = Client.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_games_by_month_pgn(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None, **kwargs):
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :returns: ``ChessDotComResponse`` object containing 
                standard multi-game format PGN containing all games for a month.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    r = Client.do_get_request(path = f"/player/{username}/games/{yyyy}/{mm}/pgn", **kwargs)
    return ChessDotComResponse(response_text = json.dumps({'png': r.text}))

def get_player_clubs(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing 
            a list of clubs the player is a member of.
    """
    r = Client.do_get_request(path = f"/player/{username}/clubs", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_player_team_matches(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of team matches the player has attended,
                is participating or is currently registered.
    """
    r = Client.do_get_request(path = f"/player/{username}/matches", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'matches')


def get_player_tournaments(username: str, **kwargs):
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a 
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    r = Client.do_get_request(path = f"/player/{username}/tournaments", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'tournaments')


def get_club_details(url_id: str, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing additional details about a club.
    """
    r = Client.do_get_request(path = f"/club/{url_id}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'club')


def get_club_members(url_id: str, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing a list of club members.
    """
    r = Client.do_get_request(path = f"/club/{url_id}/members", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'members')


def get_club_matches(url_id: str, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing a list of daily and club matches.
    """
    r = Client.do_get_request(path = f"/club/{url_id}/matches", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'matches')


def get_tournament_details(url_id: str, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing details about a daily, 
                live and arena tournament.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'tournament')


def get_tournament_round(url_id: str, round_num: int, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :returns: ``ChessDotComResponse`` object containing
                 details about a tournament's round.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}/{round_num}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'tournament_round')


def get_tournament_round_group_details(url_id: str, round_num: int, group_num: int, **kwargs):
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param group_num: the group in the tournament.
    :returns: ``ChessDotComResponse`` object containing 
                details about a tournament's round group.
    """
    r = Client.do_get_request(path = f"/tournament/{url_id}/{round_num}/{group_num}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'tournament_round_group')


def get_team_match(match_id: int, **kwargs):
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    r = Client.do_get_request(path = f"/match/{match_id}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'match')


def get_team_match_board(match_id: int, board_num: int, **kwargs):
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match board.
    """
    r = Client.do_get_request(path = f"/match/{match_id}/{board_num}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'match_board')


def get_team_match_live(match_id: int, **kwargs):
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    r = Client.do_get_request(path = f"/match/live/{match_id}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = "match_live")


def get_team_match_live_board(match_id: int, board_num: int, **kwargs):
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object containing details 
                about a team match board.
    """
    r = Client.do_get_request(path = f"/match/live/{match_id}/{board_num}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = "match_live_board")


def get_country_details(iso: str, **kwargs):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing
                additional details about a country.
    """
    r = Client.do_get_request(path = f"/country/{iso}", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'country')


def get_country_players(iso: str, **kwargs):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing a list of usernames for players
                who identify themselves as being in this country.
    """
    r = Client.do_get_request(path = f"/country/{iso}/players", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_country_clubs(iso: str, **kwargs):
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing a list of URLs for clubs identified
                as being in or associated with this country.
    """
    r = Client.do_get_request(path = f"/country/{iso}/clubs", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_current_daily_puzzle(**kwargs):
    """
    :returns: ``ChessDotComResponse`` object containing
                information about the daily puzzle found in www.chess.com.
    """
    r = Client.do_get_request(path = "/puzzle", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'puzzle')


def get_random_daily_puzzle(**kwargs):
    """
    :returns: ``ChessDotComResponse`` object containing
                information about a randomly picked daily puzzle.
    """
    r = Client.do_get_request(path = "/puzzle/random", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'puzzle')


def get_streamers(**kwargs):
    """
    :returns: ``ChessDotComResponse`` object containing 
                information about Chess.com streamers.
    """
    r = Client.do_get_request(path = "/streamers", **kwargs)
    return ChessDotComResponse(response_text = r.text)


def get_leaderboards(**kwargs):
    """
    :returns: ``ChessDotComResponse`` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    r = Client.do_get_request(path = "/leaderboards", **kwargs)
    return ChessDotComResponse(response_text = r.text, top_level_attr = 'leaderboards')

