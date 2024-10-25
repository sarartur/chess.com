# Python wrapper for Chess.com Public API
<img alt="GitHub Workflow Status (event)" src="https://img.shields.io/github/actions/workflow/status/sarartur/chess.com/build_and_publish.yml?event=push"> <img src="https://img.shields.io/readthedocs/chessdotcom"> <img src="https://img.shields.io/github/license/sarartur/chess.com">  <img alt="PyPI" src="https://img.shields.io/pypi/v/chess.com"> <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/chess.com?color=007EC6"> <img src="https://img.shields.io/github/forks/sarartur/chess.com"> <img src="https://img.shields.io/github/stars/sarartur/chess.com">
---
Python wrapper for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 
## Installation 
**The package requires Python 3.8 or higher**.

Install latest version from [PyPI](https://pypi.org/project/chess.com/) ```pip install chess.com``` 

## Resources
* Documentation: [readthedocs.org](https://chesscom.readthedocs.io/)
* Published-Data API: [chess.com](https://www.chess.com/news/view/published-data-api)

## Usage
### Retrieving Data
All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes.

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

## Contact
* Open a new [Issue](https://github.com/sarartur/chess.com/issues) on Github.