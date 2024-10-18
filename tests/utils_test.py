from datetime import datetime

from chessdotcom.utils import resolve_date


def test_resolve_date():
    yyyy, mm = resolve_date(1981, 1, None)
    assert yyyy == "1981" and mm == "01"
    yyyy, mm = resolve_date("1981", "1", None)
    assert yyyy == "1981" and mm == "01"
    yyyy, mm = resolve_date(
        None, None, datetime(year=1981, month=1, day=1, hour=0, second=0, microsecond=0)
    )
    assert yyyy == "1981" and mm == "01"
    try:
        resolve_date(1981, None, None)
        assert False
    except ValueError:
        pass
    try:
        resolve_date(None, 1, None)
        assert False
    except ValueError:
        pass
    try:
        resolve_date(None, None, None)
        assert False
    except ValueError:
        pass
