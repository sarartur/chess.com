from urllib3 import PoolManager
from urllib.parse import urlencode
from certifi import where
import json
from typing import Dict

from chessdotcom.errors import ChessDotComError


class ChessDotCom(object):

    __HOST__ = "https://api.chess.com/pub"
    https = PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=where())


    @classmethod
    def player_profile(cls, username: str) -> Dict:
        """Public method that returns additional details about a player
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION,
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def titled_players(cls, title_abbrev: str) -> Dict:
        """Public method that returns list of titled-player usernames
        
        Parameters:
            title_abbrev -- abbreviation of chess title
        """

        URL_EXTENSION = f"/titled/{title_abbrev}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))

    
    @classmethod
    def player_stats(cls, username: str) -> Dict:
        """Public method that returns ratings, win/loss, 
        and other stats about a player's game play, tactics, 
        lessons and Puzzle Rush score.
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/stats"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_is_online(cls, username: str) -> Dict:
        """Public method that returns True if user has been online
        in the last 5 minutes
        
        Parameters:
            username -- username of the player"""

        URL_EXTENSION = f"/player/{username}/is-online"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))

    
    @classmethod
    def player_current_games(cls, username: str) -> Dict:
        """Public method that returns an array
        of Daily Chess games that a player is currently playing
       
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/games"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_current_games_to_move(cls, username: str) -> Dict:
        """Public method that returns an array of Daily Chess games 
        where it is the player's turn to act

        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/games/to-move"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_games_archives(cls, username: str) -> Dict:
        """Public method that returns a array 
        of monthly archives available for this player.
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/games/archives"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_games_by_month(cls, username: str, yyyy: str, mm: str) -> Dict:
        """Public method that returns an array of 
        live and daily Chess games that a player has finished.
        
        Parameters:
            username -- username of the player
            yyyy -- intger: the year (yyyy)
            mm -- integer: the month (mm)
        """

        URL_EXTENSION = f"/player/{username}/games/{yyyy}/{mm}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))

    
    @classmethod
    def player_games_by_month_pgn(cls, username: str, yyyy: str, mm: str):
        """Public method that returns standard multi-game format PGN 
        containing all games for a month
        
        Parameters:
            username -- username of the player
            yyyy -- intger: the year (yyyy)
            mm -- integer: the month (mm)
        """

        URL_EXTENSION = f"/player/{username}/games/{yyyy}/{mm}/pgn"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return r.data


    @classmethod
    def player_clubs(cls, username: str) -> Dict:
        """Public method that returns list of clubs the player 
        is a member of.
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/clubs"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_team_matches(cls, username: str) -> Dict:
        """Public method that returns List of Team matches the player has attended, 
        is partecipating or is currently registered.
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/matches"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def player_tournaments(cls, username: str) -> Dict:
        """List of tournaments the player is registered, 
        is attending or has attended in the past.
        
        Parameters:
            username -- username of the player
        """

        URL_EXTENSION = f"/player/{username}/tournaments"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def clubs(cls, url_id: str) -> Dict:
        """Public method that returns additional details about a club
        
        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
        """

        URL_EXTENSION = f"/club/{url_id}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def club_members(cls, url_id: str) -> Dict:
        """Public method that return a list of club members
        
        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
        """

        URL_EXTENSION = f"/club/{url_id}/members"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def club_matches(cls, url_id: str) -> Dict:
        """Public method that returns a list of daily and club matches

        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
        """

        URL_EXTENSION = f"/club/{url_id}/matches"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def tournament(cls, url_id: str) -> Dict:
        """Public method that returns details 
        about a daily, live and arena tournament
        
        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
        """

        URL_EXTENSION = f"/tournament/{url_id}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def tournament_round(cls, url_id: str, round_num: int) -> Dict:
        """Public method that returns details about a
        tournament's round.

        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
            round_num -- the round of the tournament
        """

        URL_EXTENSION = f"/tournament/{url_id}/{round_num}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def tournament_round_group(cls, url_id: str, round_num: int, group_num: int) -> Dict:
        """Public method that returns details about a tournament's
        round group

        Parameters:
            url_id -- URL for the club's web page on www.chess.com.
            round_num -- the round of the tournament
            group_num -- the group in the tournament
        """

        URL_EXTENSION = f"/tournament/{url_id}/{round_num}/{group_num}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def team_match(cls, match_id: int) -> Dict:
        """Public method that returns details about a team match 
        and players playing that match

        Parameters:
            match_id -- the id of the match
        """

        URL_EXTENSION = f"/match/{match_id}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def team_match_board(cls, match_id: int, board_num: int) -> Dict:
        """Public method that returns details about
        a team match board
        
        Parameters:
            match_id -- the id of the match
            board_num -- the number of the board
        """

        URL_EXTENSION = f"/match/{match_id}/{board_num}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def team_match_live(cls, match_id: int) -> Dict:
        """Public method that returns details 
        about a team match and players playing that match
        
        Parameters:
            match_id -- the id of the match
        """

        URL_EXTENSION = f"/match/live/{match_id}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def team_match_live_board(cls, match_id: int, board_num: int) -> Dict:
        """Public method that returns details about a team match board
        
        Parameters:
            match_id -- the id of the match
            board_num -- the number of the board
        """

        URL_EXTENSION = f"/match/live/{match_id}/{board_num}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def country(cls, iso: str) -> Dict:
        """Public method that returns additional details about a country
        
        Parameters:
            iso -- country's 2-character ISO 3166 code
        """

        URL_EXTENSION = f"/country/{iso}"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def country_players(cls, iso):
        """Public method that returns list of usernames for players 
        who identify themselves as being in this country.
        
        Parameters:
            iso -- country's 2-character ISO 3166 code
        """

        URL_EXTENSION = f"/country/{iso}/players"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def country_clubs(cls, iso: str) -> Dict:
        """Public method that returns list of  URLs for clubs identified 
        as being in or associated with this country.

        Parameters:
            iso -- country's 2-character ISO 3166 code
        """

        URL_EXTENSION = f"/country/{iso}/clubs"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def puzzle(cls) -> Dict:
        """Public method that returns information 
        about the daily puzzle found in www.chess.com"""

        URL_EXTENSION = f"/puzzle"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod 
    def puzzle_random(cls) -> Dict:
        """Public method that returns information about a 
        randomly picked daily puzzle"""

        URL_EXTENSION = f"/puzzle/random"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def streamers(cls):
        """Public method that returns information 
        about Chess.com streamers."""

        URL_EXTENSION = f"/streamers"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION, 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))


    @classmethod
    def leaderboards(cls):
        """Public method that returns information about top 50 player 
        for daily and live games, tactics and lessons."""

        URL_EXTENSION = f"/leaderboards"
        r = cls.https.request(
            method='GET',
            url = cls.__HOST__ + URL_EXTENSION, 
        )
        if r.status != 200:
            raise ChessDotComError(status_code = r.status)
        return json.loads(r.data.decode('utf-8'))
