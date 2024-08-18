# Python wrapper for Chess.com Public API

> Maintained Fork

[![Github Issues](https://img.shields.io/github/issues/sarartur/chess.com)](https://github.com/sarartur/chess.com/issues)
[![GitHub Forks](https://img.shields.io/github/forks/sarartur/chess.com)](https://github.com/sarartur/chess.com/forks)
[![Github Stars](https://img.shields.io/github/stars/sarartur/chess.com)](https://github.com/sarartur/chess.com/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI - Version](https://img.shields.io/pypi/v/chess.com)](https://pypi.org/project/chess.com/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/chess.com?color=007EC6)](https://pypi.org/project/chess.com/)
[![Python package](https://github.com/Naviamold1/chess.com/actions/workflows/python-package.yml/badge.svg)](https://github.com/Naviamold1/chess.com/actions/workflows/python-package.yml)

Python wrapper for Chess.com API which provides public data from the chess.com website. All endpoints provided by Chess.com's API are available in the respectively named methods.

## Installation

**The package requires Python 3.9 or higher**.

Install latest version from [PyPI](https://pypi.org/project/chess.com/):

```py
pip install nav-chess.com
```

## Resources

- Documentation: [readthedocs.org](https://chesscom.readthedocs.io/)
- Published-Data API: [chess.com](https://www.chess.com/news/view/published-data-api)

## Usage

### Configuring Headers

Headers and and other request parameters can be set through the `Client` object. Official Chess.com documentation requires adding a `User-Agent` header.

```python
from chessdotcom import Client

Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
```

### Retrieving Data

All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes.

The package uses [aiohttp](https://docs.aiohttp.org/en/stable/) for asynchronous requests and [requests](https://requests.readthedocs.io/en/latest/) for synchronous requests to interact with the API.

#### Synchronous

```python
from chessdotcom import get_player_profile, Client

Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)
response = get_player_profile("fabianocaruana")

player_name = response.json['player']['name']
#or
player_name = response.player.name
```

#### Asynchronous

```python
import asyncio

from chessdotcom.aio import get_player_profile

usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]

cors = [get_player_profile(name) for name in usernames]

async def gather_cors(cors):
    return await asyncio.gather(*cors)

responses = asyncio.run(gather_cors(cors))

```

#### Managing Rate Limit

The package offers several ways to deal with the rate limit. Every function accepts a `tts` parameter which controls the number of seconds the `Client` will wait before making the request. This is useful if running a lot of coroutines at once.

```python
cors = [get_player_profile(name, tts = i / 10) for i, name in enumerate(usernames)]
```

The second method is to adjust the `rate_limit_handler` attribute of the `Client` object.

```python
Client.rate_limit_handler.tries = 2
Client.rate_limit_handler.tts = 4
```

If the initial request gets rate limited the client will automatically retry the request **2 more times** with an interval of **4 seconds**.

All the methods from the package will now include the header when making a request to the API.

### Contact

- Email me at <sarartur.ruk@gmail.com> or open a new [Issue](https://github.com/sarartur/chess.com/issues) on Github.
