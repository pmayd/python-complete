WORKOUT_SCHEDULE = {
    "Friday": "Shoulders",
    "Monday": "Chest+biceps",
    "Saturday": "Rest",
    "Sunday": "Rest",
    "Thursday": "Legs",
    "Tuesday": "Back+triceps",
    "Wednesday": "Core",
}
REST, CHILL_OUT, TRAIN = "Rest", "Chill out!", "Go train {}"
INVALID_DAY = "Not a valid day"


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """
    day = day.title()

    workout = WORKOUT_SCHEDULE.get(day)

    if workout is None:
        return INVALID_DAY

    if workout == "Rest":
        return CHILL_OUT

    return TRAIN.format(workout)
