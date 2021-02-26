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


