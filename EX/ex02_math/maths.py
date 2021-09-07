"""Math."""


def ects(eap: int, weeks: int):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in
    time then return a string "Impossible!".

    Examples:
    1. ects(30, 12) == 65
    2. ects(1, 1) == 26
    3. ects(1, 0) == "Impossible!".
    """
    if weeks > 0:
        hours = (eap * 26) / weeks
        if 0 <= hours <= 7 * 24:
            return hours
        else:
            return "Impossible!"
    else:
        return "Impossible!"


def average(x, y, z, o):
    """
    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position
    in the function (x, y, z = 1, 2, 3). Calculate and return the average.

    Examples:
    1. average(0, 0, 0, 4) === 4
    2. average(1, 2, 3, 4) == 7.5
    3. average(5, 0, 5, 1) == 6 .
    """
    average_number = (x + y * 2 + z * 3 + o * 4) / 4
    return average_number


def clock(days, hours, minutes, seconds):
    """
    Implement a function that has 4 numeric parameters.

    The values are: days, hours, minutes, seconds. Calculate how
    many minutes are in total and return the value.

    Examples:
    1. clock(1, 24, 60, 60) === 2941
    3. clock(0, 0, 0, 60) == 1
    3. clock(0, 0, 1, 60) == 2 .
    """
    total_minutes = days * 24 * 60 + hours * 60 + minutes + seconds / 60
    return total_minutes
