Welcome to Chess.com Wrapper's Documentation!
=============================================
Description
------------
A full Python Wrapper around Chess.com API which provides public data from the Chess.com 
website. All endpoints provided by Chess.com's API are available in the 
respectively named methods. The package allows for simple interaction with the API, eliminating the need for
repetitive code and testing.


Indices and tables
------------------

* :ref:`modindex`
* :ref:`search`


Installation
------------
**The package requires Python 3.8 or higher**.

Install from `PyPI <https://pypi.org/project/chess.com/>`_ ``pip install chess.com``

Retrieving Data
---------------
All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes.

Using client instance
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

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


Using functions
^^^^^^^^^^^^^^^
.. code-block:: python
   
   from chessdotcom import get_player_profile, Client
   
   Client.request_config["headers"]["User-Agent"] = (
      "My Python Application. "
      "Contact me at email@example.com"
   )
   response = get_player_profile("fabianocaruana")
  

Asynchronous
^^^^^^^^^^^^
.. code-block:: python
   
   from chessdotcom import ChessDotComClient

   client = ChessDotComClient(user_agent = "My Python Application...", aio = True)

   usernames = ["fabianocaruana", "GMHikaruOnTwitch", "MagnusCarlsen", "GarryKasparov"]

   cors = [client.get_player_profile(name) for name in usernames]

   async def gather_cors(cors):
      return await asyncio.gather(*cors)

   responses = asyncio.run(gather_cors(cors))

Managing Rate Limit
^^^^^^^^^^^^^^^^^^^

Every function accepts a `tts` parameter which controls the number of seconds the `Client` will wait before making the request. 
This is useful if running a lot of coroutines at once.

.. code-block:: python

   cors = [get_player_profile(name, tts = i / 10) for i, name in enumerate(usernames)]

The second method is to adjust the `rate_limit_handler` attribute of the `Client` object.

.. code-block:: python

   from chessdotcom import RateLimitHandler

   client = ChessDotComClient(
      rate_limit_handler = RateLimitHandler(tts = 4,retries = 2)
   )

If the initial request gets rate limited the client will automatically retry the request **2 more times** with an interval of **4 seconds**.


API Reference
^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   members/chessdotcom.client.rst
   members/chessdotcom.endpoints.rst

.. toctree::
   :maxdepth: 1

   members/chessdotcom.endpoints.player_profile.rst
   members/chessdotcom.endpoints.player_stats.rst
   members/chessdotcom.endpoints.player_clubs.rst
   members/chessdotcom.endpoints.player_game_archives.rst
   members/chessdotcom.endpoints.player_current_games.rst