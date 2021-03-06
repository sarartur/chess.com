from types import SimpleNamespace
import re

class Collection(SimpleNamespace):

    def __init__(self, **kwargs) -> None:
        clean_kwargs = {Collection.clean(key): value for key, value in kwargs.items()}
        SimpleNamespace.__init__(self, **clean_kwargs)

    @staticmethod
    def clean(string: str) -> str:
        string = re.sub(
            '[^0-9a-zA-Z_]', '', 
            re.sub('^[^a-zA-Z_]+', '', string)
        )
        return string
  
class BaseType(object):

    def __init__(self) -> None:
        pass

    _exclude_from_str = ["json", "text"]
    def __str__(self) -> str:
        items = (
            f"{k}={v!r}" for k, v in self.__dict__\
                .items() if k not in self.__class__._exclude_from_str)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __repr__(self) -> str:
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

