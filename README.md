# Python Chess.com Wrapper
Python wrapper around Chess.com API.
## Description & Implementation
A full Python Wrapper around Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are avaliable as methods of the ChessDotCom class. 
## Usage
Please refer to https://www.chess.com/news/view/published-data-api for detailed instructions for Chess.com API. Detailed documentation specifically for the module will soon be avaliable. Below is a simple example of the usage.
```
from chessdotcom import ChessDotCom

client = ChessDotCom()

data = client.leaderboards()
print(data)
```