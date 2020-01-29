import datetime
import calendar
from enum import IntEnum, unique

@unique
class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(
    year: int, month: int, nth: int = 4, weekday: int = Weekday.THURSDAY
) -> datetime.date:
    """Determine which day of the month the San Diego Python meetup should be.

    The meetup is on the fourth Thrusday of the month
    """
    all_weeks_per_month = calendar.monthcalendar(year, month)
    weeks_with_day = [w for w in all_weeks_per_month if w[weekday] != 0]
    week_index_with_weekday = nth - 1 if nth >= 0 else nth

    return datetime.date(
        year, month, weeks_with_day[week_index_with_weekday][weekday]
    )


if __name__ == "__main__":
    print(meetup_date(2016, 2, nth=4, weekday=Weekday.THURSDAY))

