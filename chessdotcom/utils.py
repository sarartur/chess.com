from datetime import datetime

def resolve_date(year, month, date: datetime) -> (str, str):
    """Private method that resolves different date parameters 
    and returns 'yyyy' and 'mm'.

    Parameters:
        year -- year
        month --month
        datetime -- datetime object
    """

    if (year is None) != (month is None):
        raise ValueError("You must provide both the year and the month, or a datetime.datetime object")
    if year is not None:
        if isinstance(year, int):
            year = str(year)
        if isinstance(month, int):
            month = str(month)
        return year, month.zfill(2)
    elif date is not None:
        return str(date.year), str(date.month).zfill(2)
    else:
        raise ValueError("You must provide both the year and the month, or a datetime.datetime object")