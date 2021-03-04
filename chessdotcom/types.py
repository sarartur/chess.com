from types import SimpleNamespace
import re

class Node(SimpleNamespace):

    def __init__(self, **kwargs):
        clean_kwargs = {Node.clean(key): value for key, value in kwargs.items()}
        SimpleNamespace.__init__(self, **clean_kwargs)

    @staticmethod
    def clean(string):
        string = re.sub('[^0-9a-zA-Z_]', '', string)
        string = re.sub('^[^a-zA-Z_]+', '', string)
        return string
  

