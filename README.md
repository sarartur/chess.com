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
The project uses `requests` package to interact with the API. Headers and proxies can be set through the `Client` object. Official Chess.com documentation recommends adding a `User-Agent` header. 
``` python
#optional
from chessdotcom import Client

Client.headers["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
```
All the methods from the module will now include the header when making a request to the API.


