Welcome to Chess.com Wrapper's Documentation!
=============================================
Description
------------
"A full Python Wrapper around Chess.com API which provides public data from the Chess.com 
website. All endpoints provided by Chess.com's API are available in the 
respectively named methods. The package allows for simple interaction with the API, eliminating the need for
repetitive code and testing."

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Getting Started
=============================================

Installation
------------
**The package requires Python 3.8 or higher**.

Install from `PyPI <https://pypi.org/project/chess.com/>`_ ``pip install chess.com``

Retrieving Data
---------------
All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes.

Using client instance
^^^^^^^^^^^
.. code-block:: python

   from chessdotcom import ChessDotComClient
      
   client = ChessDotComClient(user_agent = "My Python Application...")

   response = client.get_player_profile("fabianocaruana")

   player_name = response.json['player']['name']
   #or
   player_name = response.player.name


Using functions
^^^^^^^^^^^
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
==============

chessdotcom.client
---------------------
.. automodule:: chessdotcom.client
   :members:

chessdotcom.endpoints
------------------
.. automodule:: chessdotcom.endpoints
   :members: 
