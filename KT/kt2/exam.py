"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) < 4:
        return s[::-1]
    else:
        return s[-2:] + s[2:-2] + s[:2]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    # try:
    #     if text == '':
    #         return ''
    #     return text[leave_count: leave_count + take_count] + take_partial(text[leave_count + take_count:], leave_count, take_count)
    # except IndexError:
    #     return ''
    if text == '':
        return ''
    return text[leave_count: leave_count + take_count] + take_partial(text[leave_count + take_count:], leave_count, take_count)


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    sorted_nums = sorted(nums, reverse=True)
    list_of_diffs = []
    for index, num in enumerate(sorted_nums):
        try:
            list_of_diffs.append(sorted_nums[index] - sorted_nums[index + 1])
        except IndexError:
            pass
    return min(list_of_diffs)


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    new_dict = {}
    list_of_all_chars = list(text)
    list_of_chars = set(list_of_all_chars)
    for char in list_of_chars:
        if list_of_all_chars.count(char) in new_dict:
            new_dict[list_of_all_chars.count(char)] += [char]
        else:
            new_dict[list_of_all_chars.count(char)] = [char]
    return new_dict
