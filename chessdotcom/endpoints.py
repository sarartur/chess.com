from datetime import datetime
from typing import Optional, Union

from .client import Client
from .types import ChessDotComResponse, Resource
from .utils import resolve_date


@Client.endpoint
def get_player_profile(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing information about
                the player's profile.
    """
    return Resource(
        uri=f"/player/{username}",
        tts=tts,
        top_level_attr="player",
        request_config=kwargs,
    )


@Client.endpoint
def get_titled_players(title_abbrev: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param title_abbrev: abbreviation of chess title.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of usernames.
    """
    return Resource(uri=f"/titled/{title_abbrev}", tts=tts, request_config=kwargs)


@Client.endpoint
def get_player_stats(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing information about the
                plyers's ratings, win/loss, and other stats.
    """
    return Resource(
        uri=f"/player/{username}/stats",
        tts=tts,
        top_level_attr="stats",
        request_config=kwargs,
    )


@Client.endpoint
def is_player_online(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing infomation about
                whether or not a player is online
    """
    return Resource(uri=f"/player/{username}/is-online", tts=tts, request_config=kwargs)


@Client.endpoint
def get_player_current_games(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                that a player is currently playing.
    """
    return Resource(uri=f"/player/{username}/games", tts=tts, request_config=kwargs)


@Client.endpoint
def get_player_current_games_to_move(
    username: str, tts=0, **kwargs
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                where it is the player's turn to act.
    """
    return Resource(
        uri=f"/player/{username}/games/to-move", tts=tts, request_config=kwargs
    )


@Client.endpoint
def get_player_game_archives(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a
                list of monthly archives available for this player.
    """
    return Resource(
        uri=f"/player/{username}/games/archives", tts=tts, request_config=kwargs
    )


@Client.endpoint
def get_player_games_by_month(
    username: str,
    year: Optional[Union[str, int, None]] = None,
    month: Optional[Union[str, int, None]] = None,
    datetime_obj: Optional[Union[datetime, None]] = None,
    tts=0,
    **kwargs,
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param year: the year (yyyy).
    :param month: the month (mm).
    :param date: datetime.datetime of the month. Can be passed in instead of month
                    and year parameters.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of live and daily
                Chess games that a player has finished.
    """
    yyyy, mm = resolve_date(year, month, datetime_obj)
    return Resource(
        uri=f"/player/{username}/games/{yyyy}/{mm}", tts=tts, request_config=kwargs
    )


@Client.endpoint
def get_player_games_by_month_pgn(
    username: str,
    year: Optional[Union[str, int, None]] = None,
    month: Optional[Union[str, int, None]] = None,
    datetime_obj: Optional[Union[datetime, None]] = None,
    tts=0,
    **kwargs,
) -> ChessDotComResponse:
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
        uri=f"/player/{username}/games/{yyyy}/{mm}/pgn",
        tts=tts,
        top_level_attr="pgn",
        no_json=True,
        request_config=kwargs,
    )


@Client.endpoint
def get_player_clubs(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
            a list of clubs the player is a member of.
    """
    return Resource(uri=f"/player/{username}/clubs", tts=tts, request_config=kwargs)


@Client.endpoint
def get_player_team_matches(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of team matches
                the player has attended,
                is participating or is currently registered.
    """
    return Resource(
        uri=f"/player/{username}/matches",
        tts=tts,
        top_level_attr="matches",
        request_config=kwargs,
    )


@Client.endpoint
def get_player_tournaments(username: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a
                list of tournaments the player is registered,
                is attending or has attended in the past.
    """
    return Resource(
        uri=f"/player/{username}/tournaments",
        tts=tts,
        top_level_attr="tournaments",
        request_config=kwargs,
    )


@Client.endpoint
def get_club_details(url_id: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing additional details about a club.
    """
    return Resource(
        uri=f"/club/{url_id}", tts=tts, top_level_attr="club", request_config=kwargs
    )


@Client.endpoint
def get_club_members(url_id: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of club members.
    """
    return Resource(
        uri=f"/club/{url_id}/members",
        tts=tts,
        top_level_attr="members",
        request_config=kwargs,
    )


@Client.endpoint
def get_club_matches(url_id: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of daily and club matches.
    """
    return Resource(
        uri=f"/club/{url_id}/matches",
        tts=tts,
        top_level_attr="matches",
        request_config=kwargs,
    )


@Client.endpoint
def get_tournament_details(url_id: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing details about a daily,
                live and arena tournament.
    """
    return Resource(
        uri=f"/tournament/{url_id}",
        tts=tts,
        top_level_attr="tournament",
        request_config=kwargs,
    )


@Client.endpoint
def get_tournament_round(
    url_id: str, round_num: int, tts=0, **kwargs
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                 details about a tournament's round.
    """
    return Resource(
        uri=f"/tournament/{url_id}/{round_num}",
        tts=tts,
        top_level_attr="tournament_round",
        request_config=kwargs,
    )


@Client.endpoint
def get_tournament_round_group_details(
    url_id: str, round_num: int, group_num: int, tts=0, **kwargs
) -> ChessDotComResponse:
    """
    :param url_id: URL for the club's web page on www.chess.com.
    :param round_num: the round of the tournament.
    :param group_num: the group in the tournament.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a tournament's round group.
    """
    return Resource(
        uri=f"/tournament/{url_id}/{round_num}/{group_num}",
        tts=tts,
        top_level_attr="tournament_round_group",
        request_config=kwargs,
    )


@Client.endpoint
def get_team_match(match_id: int, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri=f"/match/{match_id}", tts=tts, top_level_attr="match", request_config=kwargs
    )


@Client.endpoint
def get_team_match_board(
    match_id: int, board_num: int, tts=0, **kwargs
) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match board.
    """
    return Resource(
        uri=f"/match/{match_id}/{board_num}",
        tts=tts,
        top_level_attr="match_board",
        request_config=kwargs,
    )


@Client.endpoint
def get_team_match_live(match_id: int, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                details about a team match and players playing that match.
    """
    return Resource(
        uri=f"/match/live/{match_id}",
        tts=tts,
        top_level_attr="match",
        request_config=kwargs,
    )


@Client.endpoint
def get_team_match_live_board(
    match_id: int, board_num: int, tts=0, **kwargs
) -> ChessDotComResponse:
    """
    :param match_id: the id of the match.
    :param board_num: the number of the board.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing details
                about a team match board.
    """
    return Resource(
        uri=f"/match/live/{match_id}/{board_num}",
        tts=tts,
        top_level_attr="match_board",
        request_config=kwargs,
    )


@Client.endpoint
def get_country_details(iso: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                additional details about a country.
    """
    return Resource(
        uri=f"/country/{iso}", tts=tts, top_level_attr="country", request_config=kwargs
    )


@Client.endpoint
def get_country_players(iso: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of usernames for players
                who identify themselves as being in this country.
    """
    return Resource(uri=f"/country/{iso}/players", tts=tts, request_config=kwargs)


@Client.endpoint
def get_country_clubs(iso: str, tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param iso: country's 2-character ISO 3166 code.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of URLs for clubs identified
                as being in or associated with this country.
    """
    return Resource(uri=f"/country/{iso}/clubs", tts=tts, request_config=kwargs)


@Client.endpoint
def get_current_daily_puzzle(tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about the daily puzzle found in www.chess.com.
    """
    return Resource(
        uri="/puzzle", top_level_attr="puzzle", tts=tts, request_config=kwargs
    )


@Client.endpoint
def get_random_daily_puzzle(tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about a randomly picked daily puzzle.
    """
    return Resource(
        uri="/puzzle/random", tts=tts, top_level_attr="puzzle", request_config=kwargs
    )


@Client.endpoint
def get_streamers(tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about Chess.com streamers.
    """
    return Resource(uri="/streamers", tts=tts, request_config=kwargs)


@Client.endpoint
def get_leaderboards(tts=0, **kwargs) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    return Resource(
        uri="/leaderboards",
        tts=tts,
        top_level_attr="leaderboards",
        request_config=kwargs,
    )
