# Python bindings for Chess.com Public API
## Description & Implementation
Python bindings for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 
\
Install the package with: ```pip install chess.com``` \
https://pypi.org/project/chess.com/
## Usage
Please refer to https://chesscom.readthedocs.io/ and https://www.chess.com/news/view/published-data-api for documentation. Below is a simple example of the usage.
``` python
from chessdotcom import get_player_profile

data = get_player_profile("fabianocaruana")
print(data.json)
```
output:
``` json
{"avatar": "https://images.chesscomfiles.com/uploads/v1/user/11177810.d53953f7.200x200o.3ef259191986.png", "player_id": 11177810, "@id": "https://api.chess.com/pub/player/fabianocaruana", "url": "https://www.chess.com/member/FabianoCaruana", "name": "Fabiano Caruana", "username": "fabianocaruana", "title": "GM", "followers": 12218, "country": "https://api.chess.com/pub/country/US", "last_online": 1614302241, "joined": 1363533272, "status": "premium", "is_streamer": False}
```


