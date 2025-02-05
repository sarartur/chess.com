# Python client for Chess.com Public API
<img alt="GitHub Workflow Status (event)" src="https://img.shields.io/github/actions/workflow/status/sarartur/chess.com/build_and_publish.yml?branch=master"> <img src="https://img.shields.io/readthedocs/chessdotcom"> <img src="https://img.shields.io/github/license/sarartur/chess.com">  <img alt="PyPI" src="https://img.shields.io/pypi/v/chess.com"> <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/chess.com?color=007EC6"> <img src="https://img.shields.io/github/forks/sarartur/chess.com"> <img src="https://img.shields.io/github/stars/sarartur/chess.com">
---
Python client for Chess.com API which provides public data from the chess.com website. 
## Installation 
**The package requires Python 3.8 or higher**.

Install latest version from [PyPI](https://pypi.org/project/chess.com/) ```pip install chess.com``` 

## Resources
* Documentation: [readthedocs.org](https://chesscom.readthedocs.io/)
* Published-Data API: [chess.com](https://www.chess.com/news/view/published-data-api)

## Usage
### Retrieving Data
The package uses [aiohttp](https://docs.aiohttp.org/en/stable/) for asynchronous requests and [requests](https://requests.readthedocs.io/en/latest/) for synchronous requests to interact with the API. 

#### Using client instance

``` python
from chessdotcom import ChessDotComClient
   
client = ChessDotComClient(user_agent = "My Python Application...")

response = client.get_player_profile("fabianocaruana")

response.player.name # 'Fabiano Caruana'
response.player.title # 'GM'
response.player.last_online_datetime # datetime.datetime(2024, 10, 25, 20, 8, 28)
response.player.joined_datetime # datetime.datetime(2013, 3, 17, 15, 14, 32)
# See readthedocs for full documentation of responses

# or access the source
response.json['player']['name'] # 'Fabiano Caruana'
```

#### Using functions

``` python
from chessdotcom import get_player_profile, Client
   
Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
response = get_player_profile("fabianocaruana")
```

#### Asynchronous 
``` python 
from chessdotcom import ChessDotComClient

client = ChessDotComClient(user_agent = "My Python Application...", aio = True)

usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]

cors = [client.get_player_profile(name) for name in usernames]

async def gather_cors(cors):
    return await asyncio.gather(*cors)

responses = asyncio.run(gather_cors(cors))

```
#### Managing Rate Limit
Every function accepts a `tts` parameter which controls the number of seconds the `Client` will wait before making the request. This is useful if running a lot of coroutines at once.
 
 ``` python 
 cors = [get_player_profile(name, tts = i / 10) for i, name in enumerate(usernames)]
```
The second method is to pass ```rate_limit_handler``` option to the client.

``` python
from chessdotcom import RateLimitHandler

client = ChessDotComClient(
    rate_limit_handler = RateLimitHandler(tts = 4,retries = 2)
)
```
If the initial request gets rate limited the client will automatically retry the request **2 more times** with an interval of **4 seconds**.

## Available Endpoints

#### Player Data

- [Profile](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_profile.html)
- [Stats](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_stats.html)
- [Clubs](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_clubs.html)
- [Game archives](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_game_archives.html)
- [Current games](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_current_games.html)
- [Games by month](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_games_by_month.html)
- [Games by month PGN](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_games_by_month_pgn.html)
- [Tournaments](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_tournaments.html)
- [Titled players](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.titled_players.html)
- [Team matches](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_team_matches.html)
- [Current games to move](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.player_current_games_to_move.html)

#### Clubs

- [Club details](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.club_details.html)
- [Club members](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.club_members.html)
- [Club matches](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.club_matches.html)


#### Tournaments

- [Tournament details](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.tournament_details.html)
- [Tournament round](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.tournament_round.html)
- [Tournament round group details](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.tournament_round_group_details.html)

#### Team Matches

- [Team match](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.team_match.html)
- [Team match board](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.team_match_board.html)
- [Team match live](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.team_match_live.html)
- [Team match live board](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.team_match_live_board.html)

#### Countries

- [Country clubs](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.country_clubs.html)
- [Country players](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.country_players.html)
- [Country details](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.country_details.html)

#### Daily Puzzle

- [Random daily puzzle](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.random_daily_puzzle.html)
- [Current daily puzzle](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.current_daily_puzzle.html)

#### Other

- [Streamers](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.streamers.html)
- [Leaderboards](https://chesscom.readthedocs.io/en/latest/members/chessdotcom.endpoints.leaderboards.html)

## Reporting Issues

Chess.com API is subject to change. Smoke tests are ran daily to make sure the package is working correctly.

<img src="https://img.shields.io/github/actions/workflow/status/sarartur/chess.com/smoke_tests.yml?branch=master&label=smoke%20tests"> <img src="https://img.shields.io/github/issues/sarartur/chess.com">

Please open an [Issue](https://github.com/sarartur/chess.com/issues) if you spot any bugs.