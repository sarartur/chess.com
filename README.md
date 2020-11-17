# Python Chess.com Wrapper
Python wrapper around Chess.com API.
## Description & Implementation
A full Python Wrapper around Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods. 
## Usage
Please refer to https://www.chess.com/news/view/published-data-api for detailed instructions for Chess.com API. Detailed documentation specifically for the module will soon be available. Below is a simple example of the usage.
``` python
from chessdotcom import get_player_profile

data = get_player_profile("fabianocaruana")
print(data.json)
```
