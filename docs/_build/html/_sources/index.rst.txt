Welcome to Chess.com Wrapper's documentation!
=============================================
Description
------------
A full Python Wrapper around Chess.com API which provides public data from the Chess.com 
website. All endpoints provided by Chess.com's API are available in the 
respectively named methods. The package allows for simple interaction with the API, eliminating the need for
repetitive code and testing.

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

Usage
------------

.. code-block:: python
   
   from chessdotcom import get_player_profile

   data = get_player_profile("fabianocaruana")

Optional Headers can also be set. Official Chess.com documentation recommends adding a `user-agent` header.

.. code-block:: python

   #optional
   from chessdotcom import Client
   Client.headers = {"User-Agent": "My Python Application. Contact me at email@example.com"}

All the methods from the module will now include the header when making the request to the API.

chessdotcom.response
====================
.. automodule:: chessdotcom.response
   :members:

chessdotcom.caller
==================
.. automodule:: chessdotcom.client
   :members: