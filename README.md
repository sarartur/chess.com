# Python wrapper for Chess.com Public API
Python wrapper for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 
## Installation 
**The package requires Python 3.7 or higher**.

Install latest version from [PyPI](https://pypi.org/project/chess.com/): ```pip install chess.com``` 

## Resources
* Documentation: [readthedocs.org](https://chesscom.readthedocs.io/)
* Published-Data API: [chess.com](https://www.chess.com/news/view/published-data-api)

## Usage
### Retrieving Data
All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes.
All functions can be made asynchronous. The package uses [aiohttp](https://docs.aiohttp.org/en/stable/) to send requests to the API. 
#### Synchronous
``` python
from chessdotcom import get_player_profile

response = get_player_profile("fabianocaruana")

player_name = response.json['player']['name']
#or
player_name = response.player.name
```
#### Asynchronous 
``` python 
from asyncio import gather

from chessdotcom.aio import get_player_profile, Client
#or
from chessdotcom import get_player_profile, Client
Client.aio = True

usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]
cors = [get_player_profile(name) for name in usernames]
responses = Client.loop.run_until_complete(gather(*cors))
```
**important**: The API will begin to rate limit the client if too many requests are made at once.

### Configuring the Client object
Headers and and other request parameters can be set through the `Client` object. Official Chess.com documentation recommends adding a `User-Agent` header. 
``` python
#optional
from chessdotcom import Client

Client.config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
```
All the methods from the module will now include the header when making a request to the API.

### Contact
* Email me at <saradzhyanatur@gmail.com> or open a new [Issue](https://github.com/sarartur/chess.com/issues) on Github.