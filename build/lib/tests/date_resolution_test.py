from datetime import datetime
import sys

sys.path.append("../")
from chessdotcom.caller import _internal

def test_date_resolution():
    yyyy, mm = _internal.resolve_date(1981, 1, None)
    assert yyyy == "1981" and mm == "01"
    yyyy, mm = _internal.resolve_date("1981", "1", None)
    assert yyyy == "1981" and mm == "01"
    yyyy, mm = _internal.resolve_date(None, None, datetime(year=1981, month=1, day=1, hour=0, second=0, microsecond=0))
    assert yyyy == "1981" and mm == "01"
    try:
        _internal.resolve_date(1981, None, None)
        assert False
    except ValueError:
        pass
    try:
        _internal.resolve_date(None, 1, None)
        assert False
    except ValueError:
        pass
    try:
        _internal.resolve_date(None, None, None)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_date_resolution()
