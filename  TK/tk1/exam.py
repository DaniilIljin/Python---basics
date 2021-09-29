"""TK 1."""

def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) given 112 minutes, return '1h 52min'.
    2) given 23 minutes, return '23min'.
    3) given 180 minutes, return '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = minutes // 60
    new_minutes = minutes % 60
    if new_minutes == 0:
        return f'{hours}h'
    elif hours == 0:
        return f'{new_minutes}min'
    else:
        return f'{hours}h {new_minutes}min'


def lucky_guess(n: int) -> bool:
    """
    Determine whether the given number gives you points for this task or not.

    The number gives you points if it is:
    * either 1, 3 or 7
    * greater or equal than -6 and smaller or equals than 121 and
      divisible by 13 (-6 and 121 are inclusive)
    * smaller than 0 and does not contain number 5 or 6

    print(lucky_guess(7))  # True
    print(lucky_guess(26))  # True
    print(lucky_guess(-35))  # False

    :param n: given number
    :return: boolean - points or no points
    """
    return (n in [1, 3, 7]) or (-6 <= n <= 121 and n % 13 == 0) or (n < 0 and str(n) not in list(str(n)))


def sum_of_a_beach(s: str) -> int:
    """
    Count how many beach elements are in the string.

    Beaches are filled with sand, water, fish, and sun.
    Given a string, calculate how many times the words
    “Sand”, “Water”, “Fish”, and “Sun” appear without
    overlapping (regardless of the case).

    sum_of_a_beach("WAtErSlIde")                    ==>  1
    sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
    sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
    sum_of_a_beach("cItYTowNcARShoW")               ==>  0
    """
    s = s.lower()
    count = 0
    count += s.count('water')
    count += s.count('sun')
    count += s.count('fish')
    count += s.count('sand')
    return count


def index_index_value(nums: list) -> int:
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """
    if len(nums) >= nums[-1]:
        if len(nums) >= nums[nums[-1]]:
            return nums[nums[nums[-1]]]
        else:
            return -2
    else:
        return -1


def word_numeration(words: list) -> list:
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    for element in words:
        words[words.index(element)] = element + f"#{words.index(element) + 1}"
    return words


if __name__ == '__main__':
    print(format_time(112))  # 1h 52min
    print(lucky_guess(26))   # True
    print(sum_of_a_beach("gOfIshsunesunFiSh"))  # 4
    print(index_index_value([0, 2, 6, 2]))  # -2
    print(word_numeration(["Tere", "tere", "tulemast"]))
    # ["Tere#1", "tere#2", "tulemast#1"]
