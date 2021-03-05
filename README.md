# Python wrapper for Chess.com Public API
## Description & Implementation
Python wrapper for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 

The package is [avaliable](https://pypi.org/project/chess.com/) on the Python Package Index.

Install the package with: ```pip install chess.com``` 

## Usage
Refer to [package](https://chesscom.readthedocs.io/) and [api](https://www.chess.com/news/view/published-data-api) docs for information on the usage.

#### Retrieving Data
All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes:
``` python
from chessdotcom import get_player_profile

response = get_player_profile("fabianocaruana")

player_name = response.json['player']['name']
#or
player_name = response.player.name
```

#### Configuring the Client object
The project uses `requests` package to interact with the API. The `requests.Session` object is available through the `Client` object. Official Chess.com documentation recommends adding a `User-Agent` header.
``` python
#optional
from chessdotcom import Client

Client.session.headers.update(**{"User-Agent": "My Python Application. Contact me at email@example.com"})
```
All the methods from the module will now include the header when making the request to the API.

The Chess.com API uses Cloudflare cookies `__cf_bm` and `__cfuid`. By default all cookies are blocked by the `Client` object. If you would like to enable them simply set `Client.cookies = True`.

**important**: Starting with version 1.5.0 responses from some functions have been altered in order to maintain consistent response format across all functions. All `ChessDotComResponse` objects now have 2 attributes: `json` and `{nested_object}`. The `{nested_object}` attribute contains all the data in attributes and other nested objects and is named according to what makes sense based on the returning function's name. The `json` attribute still contains the response in dictionary format, but now also has a top level key with the same name as the `{nested_object}` attribute. All functions that already return data with a top level key are unchanged.


