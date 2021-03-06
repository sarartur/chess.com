Welcome to Chess.com Wrapper's documentation!
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



Installation
------------

Install chess.com by running:

.. code-block::

   pip install chess.com

Retrieving Data
---------------
"All the functions return a `ChessDotComResponse` object. The data can be accessed in dictionary format or via attributes:"

.. code-block:: python
   
   from chessdotcom import get_player_profile

   response = get_player_profile("fabianocaruana")

   player_name = response.json['player']['name']
   #or
   player_name = response.player.name

Configuring the Client object
------------------------------
The project uses `requests` package to interact with the API. 
Headers and proxies can be set through the `Client` object. 
Official Chess.com documentation recommends adding a `User-Agent` header. 

.. code-block:: python

   #optional
   from chessdotcom import Client

   Client.headers["User-Agent"] = (
      "My Python Application. "
      "Contact me at email@example.com"
   )

All the methods from the module will now include the header when making a request to the API.

API Reference
==============

chessdotcom.response
---------------------
.. automodule:: chessdotcom.response
   :members:

chessdotcom.errors
-------------------
.. automodule:: chessdotcom.errors
   :members:

chessdotcom.client
------------------
.. automodule:: chessdotcom.client
   :members: 
