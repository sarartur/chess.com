# Python wrapper for Chess.com Public API
## Description & Implementation
Python wrapper for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 
\
Install the package with: ```pip install chess.com``` \
https://pypi.org/project/chess.com/
## Usage
Please refer to https://chesscom.readthedocs.io/ and https://www.chess.com/news/view/published-data-api for documentation. Below is a simple example of the usage.
``` python
from chessdotcom import get_player_profile

data = get_player_profile("fabianocaruana")
```
Optional Headers can also be set. Official Chess.com documentation recommends adding a `user-agent` header.
``` python
#optional
from chessdotcom import Client
Client.headers = {"User-Agent": "My Python Application. Contact me at email@example.com"}
```
All the methods from the module will now include the header when making the request to the API.


