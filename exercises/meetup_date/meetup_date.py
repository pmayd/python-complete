import calendar
import datetime
import doctest
from enum import IntEnum, unique


def meetup_date(
    year: int, month: int
) -> datetime.date:
    """Determine which day of the month the San Diego Python meetup should be.

    The meetup is on the fourth Thrusday of the month

    Exmaples:
    >>> meetup_date(2012, 3)
    datetime.date(2012, 3, 22)
    >>> meetup_date(2015, 2)
    datetime.date(2015, 2, 26)
    """
    pass


if __name__ == "__main__":
    doctest.testmod()
