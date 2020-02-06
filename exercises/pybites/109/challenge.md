# Bite 109. Workout dict lookups and raising an exception

In this Bite you learn how to lookup values from a dictionary or in Python: `dict`.

You are presented with `WORKOUT_SCHEDULE dict` (constant) with keys = days and values = workouts (or rest up). Complete `get_workout_motd` that receives a day string, title case it so the function can receive case insensitive days, look it up in the dict and do two things:

- If the day (key) is not in the dictionary, return `INVALID_DAY`, we don't want this function to continue.
- If the key is in the dictionary, return `CHILL_OUT` or `TRAIN` depending if it's a `REST` day or not. The latter you will need to string-interpolate using format.

Also check out the docstring and tests. Have fun and keep calm and code in Python!

Update 25th of Nov 2019: previously this Bite required re-raising the `KeyError`, but as that's already the default behavior of a missing key in a dict, we changed the requirements to return a value instead.