from ..client import Client, Resource
from ..response_builder import ChessDotComResponse
from ..utils import resolve_date
from .club_details import get_club_details
from .club_matches import get_club_matches
from .club_members import get_club_members
from .country_clubs import get_country_clubs
from .country_details import get_country_details
from .country_players import get_country_players
from .player_clubs import get_player_clubs
from .player_current_games import get_player_current_games
from .player_game_archives import get_player_game_archives
from .player_games_by_month import get_player_games_by_month
from .player_games_by_month_pgn import get_player_games_by_month_pgn
from .player_profile import get_player_profile
from .player_stats import get_player_stats
from .player_tournaments import get_player_tournaments
from .team_match import get_team_match
from .team_match_board import get_team_match_board
from .team_match_live import get_team_match_live
from .team_match_live_board import get_team_match_live_board
from .tournament_details import get_tournament_details
from .tournament_round import get_tournament_round
from .tournament_round_group_details import get_tournament_round_group_details


@Client.endpoint
def get_titled_players(
    title_abbrev: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param title_abbrev: abbreviation of chess title.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of usernames.
    """
    return Resource(
        uri=f"/titled/{title_abbrev}", tts=tts, request_options=request_options
    )


@Client.endpoint
def is_player_online(username: str, tts=0, **request_options) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing infomation about
                whether or not a player is online
    """
    return Resource(
        uri=f"/player/{username}/is-online", tts=tts, request_options=request_options
    )


@Client.endpoint
def get_player_current_games_to_move(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
    """
    :param username: username of the player.
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing a list of Daily Chess games
                where it is the player's turn to act.
    """
    return Resource(
        uri=f"/player/{username}/games/to-move",
        tts=tts,
        request_options=request_options,
    )


@Client.endpoint
def get_player_team_matches(
    username: str, tts=0, **request_options
) -> ChessDotComResponse:
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
        top_level_attribute="matches",
        request_options=request_options,
    )


@Client.endpoint
def get_current_daily_puzzle(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about the daily puzzle found in www.chess.com.
    """
    return Resource(
        uri="/puzzle",
        top_level_attribute="puzzle",
        tts=tts,
        request_options=request_options,
    )


@Client.endpoint
def get_random_daily_puzzle(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about a randomly picked daily puzzle.
    """
    return Resource(
        uri="/puzzle/random",
        tts=tts,
        top_level_attribute="puzzle",
        request_options=request_options,
    )


@Client.endpoint
def get_streamers(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about Chess.com streamers.
    """
    return Resource(uri="/streamers", tts=tts, request_options=request_options)


@Client.endpoint
def get_leaderboards(tts=0, **request_options) -> ChessDotComResponse:
    """
    :param tts: the time the client will wait before making the first request.
    :returns: ``ChessDotComResponse`` object containing
                information about top 50 player for daily and live games, tactics and lessons.
    """
    return Resource(
        uri="/leaderboards",
        tts=tts,
        top_level_attribute="leaderboards",
        request_options=request_options,
    )
