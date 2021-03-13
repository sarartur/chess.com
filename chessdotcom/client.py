import json
from typing import (
    Dict, 
    Optional, 
    Union
)
from datetime import datetime
from aiohttp import ClientSession
from asyncio import get_event_loop
from functools import wraps

from chessdotcom.types import (
    ChessDotComError, 
    ChessDotComResponse, 
    Resource
)
from chessdotcom.utils import resolve_date

class Client:
    """
    Client for Chess.com Public API. The client is only responsible for making calls.

    :cvar config: Dictionary containing extra keyword arguments for requests to the API
                    (headers, proxy, etc).
    :cvar loop: Asyncio event loop.
    :cvar aio: Determines if the functions behave asynchronously.
    """
    loop = get_event_loop()
    aio = False
    config = {"headers": {}}

    @classmethod
    async def do_get_request(cls, url: str, **kwargs):
        async with ClientSession(loop = cls.loop) as session:
            async with session.get(
                    url = url,
                    **Client.config
                ) as r:
                text = await r.text()
                if r.status != 200:
                    raise ChessDotComError(status_code = r.status, response_text = text)
                return text

    @classmethod
    async def handler(cls, func, *args, **kwargs):
        resource = func(*args, **kwargs)
        text = await Client.do_get_request(resource.url, **resource.request_extras)
        return ChessDotComResponse(text, resource.top_level_attr, resource.no_json)

    @classmethod
    def endpoint(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return cls.handler(func, *args, **kwargs) if Client.aio else cls.loop.run_until_complete(
                cls.handler(func, *args, **kwargs))
        return wrapper

@Client.endpoint
def get_player_profile(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing information about
                the player's profile.
    """
    return Resource(
        uri = f"/player/{username}",
        top_level_attr = "player",
        **kwargs
    )

@Client.endpoint
def get_titled_players(title_abbrev: str, **kwargs) -> ChessDotComResponse:
    """
    :param title_abbrev: abbreviation of chess title.
    :returns: ``ChessDotComResponse`` object containing a list of usernames.
    """
    return Resource(
        uri = f"/titled/{title_abbrev}",
        **kwargs
    )

@Client.endpoint
def get_player_stats(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing information about the
                plyers's ratings, win/loss, and other stats.
    """
    return Resource(
        uri = f"/player/{username}/stats",
        top_level_attr = "stats",
        **kwargs
    )

@Client.endpoint
def is_player_online(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing infomation about
                whether or not a player is online 
    """
    return Resource(
        uri = f"/player/{username}/is-online",
        **kwargs
    )

@Client.endpoint
def get_player_current_games(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                that a player is currently playing.
    """
    return Resource(
        uri = f"/player/{username}/games",
        **kwargs
    )

@Client.endpoint
def get_player_current_games_to_move(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games 
                where it is the player's turn to act.
    """
    return Resource(
        uri = f"/player/{username}/games/to-move",
        **kwargs
    )

@Client.endpoint
def get_player_game_archives(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a 
                list of monthly archives available for this player.
    """
    return Resource(
        uri = f"/player/{username}/games/archives",
        **kwargs
    )

@Client.endpoint
def get_player_games_by_month(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None, 
                                **kwargs) -> ChessDotComResponse:
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
    return Resource(
        uri = f"/player/{username}/games/{yyyy}/{mm}",
        **kwargs
    )

@Client.endpoint
def get_player_games_by_month_pgn(username: str, year: Optional[Union[str, int, None]] = None, 
                                month: Optional[Union[str, int, None]] = None, 
                                datetime_obj: Optional[Union[datetime, None]] = None, 
                                **kwargs) -> ChessDotComResponse:
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
    return Resource(
        uri = f"/player/{username}/games/{yyyy}/{mm}/pgn",
        top_level_attr = "pgn",
        no_json = True,
        **kwargs
    )

@Client.endpoint
def get_player_clubs(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing 
            a list of clubs the player is a member of.
    """
    return Resource(
        uri = f"/player/{username}/clubs",
        **kwargs
    )

@Client.endpoint
def get_player_team_matches(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a list of team matches the player has attended,
                is participating or is currently registered.
    """
    return Resource(
        uri = f"/player/{username}/clubs",
        top_level_attr = "matches",
        **kwargs
    )

@Client.endpoint
def get_player_tournaments(username: str, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :returns: ``ChessDotComResponse`` object containing a 
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    return Resource(
        uri = f"/player/{username}/tournaments",
        top_level_attr = "tournaments",
        **kwargs
    )

@Client.endpoint
def get_club_details(url_id: str, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing additional details about a club.
    """
    return Resource(
        uri = f"/club/{url_id}",
        top_level_attr = "club",
        **kwargs
    )

@Client.endpoint
def get_club_members(url_id: str, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing a list of club members.
    """
    return Resource(
        uri = f"/club/{url_id}/members",
        top_level_attr = "members",
        **kwargs
    )

@Client.endpoint
def get_club_matches(url_id: str, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing a list of daily and club matches.
    """
    return Resource(
        uri = f"/club/{url_id}/matches",
        top_level_attr = "matches",
        **kwargs
    )

@Client.endpoint
def get_tournament_details(url_id: str, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :returns: ``ChessDotComResponse`` object containing details about a daily, 
                live and arena tournament.
    """
    return Resource(
        uri = f"/tournament/{url_id}",
        top_level_attr = "tournament",
        **kwargs
    )

@Client.endpoint
def get_tournament_round(url_id: str, round_num: int, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :returns: ``ChessDotComResponse`` object containing
                 details about a tournament's round.
    """
    return Resource(
        uri = f"/tournament/{url_id}/{round_num}",
        top_level_attr = "tournament_round",
        **kwargs
    )

@Client.endpoint
def get_tournament_round_group_details(url_id: str, round_num: int, 
                                            group_num: int, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param group_num: the group in the tournament.
    :returns: ``ChessDotComResponse`` object containing 
                details about a tournament's round group.
    """
    return Resource(
        uri = f"/tournament/{url_id}/{round_num}/{group_num}",
        top_level_attr = "tournament_round_group",
        **kwargs
    )

@Client.endpoint
def get_team_match(match_id: int, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri = f"/match/{match_id}",
        top_level_attr = "match",
        **kwargs
    )

@Client.endpoint
def get_team_match_board(match_id: int, board_num: int, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match board.
    """
    return Resource(
        uri = f"/match/{match_id}/{board_num}",
        top_level_attr = "match_board",
        **kwargs
    )

@Client.endpoint
def get_team_match_live(match_id: int, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri = f"/match/live/{match_id}",
        top_level_attr = "match",
        **kwargs
    )

@Client.endpoint
def get_team_match_live_board(match_id: int, board_num: int, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :returns: ``ChessDotComResponse`` object containing details 
                about a team match board.
    """
    return Resource(
        uri = f"/match/live/{match_id}/{board_num}",
        top_level_attr = "match_board",
        **kwargs
    )

@Client.endpoint
def get_country_details(iso: str, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing
                additional details about a country.
    """
    return Resource(
        uri = f"/country/{iso}",
        top_level_attr = "country",
        **kwargs
    )

@Client.endpoint
def get_country_players(iso: str, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing a list of usernames for players
                who identify themselves as being in this country.
    """
    return Resource(
        uri = f"/country/{iso}/players",
        **kwargs
    )

@Client.endpoint
def get_country_clubs(iso: str, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :returns: ``ChessDotComResponse`` object containing a list of URLs for clubs identified
                as being in or associated with this country.
    """
    return Resource(
        uri = f"/country/{iso}/clubs",
        **kwargs
    )

@Client.endpoint
def get_current_daily_puzzle(**kwargs) -> ChessDotComResponse:
    """
    :returns: ``ChessDotComResponse`` object containing
                information about the daily puzzle found in www.chess.com.
    """
    return Resource(
        uri = "/puzzle",
        top_level_attr = "puzzle",
        **kwargs
    )

@Client.endpoint
def get_random_daily_puzzle(**kwargs) -> ChessDotComResponse:
    """
    :returns: ``ChessDotComResponse`` object containing
                information about a randomly picked daily puzzle.
    """
    return Resource(
        uri = "/puzzle/random",
        top_level_attr = "puzzle",
        **kwargs
    )

@Client.endpoint
def get_streamers(**kwargs) -> ChessDotComResponse:
    """
    :returns: ``ChessDotComResponse`` object containing 
                information about Chess.com streamers.
    """
    return Resource(
        uri = "/streamers",
        **kwargs
    )

@Client.endpoint
def get_leaderboards(**kwargs) -> ChessDotComResponse:
    """
    :returns: ``ChessDotComResponse`` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    return Resource(
        uri = "/leaderboards",
        top_level_attr = "leaderboards",
        **kwargs
    )