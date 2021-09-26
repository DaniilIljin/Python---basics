"""EX04 - List and Tuple."""

import string
import random

letters = string.ascii_letters
data_type_dictionary = {
    'string': list(string.ascii_letters),
    'int': list(range(0, 1000)),
    'float': list(x * 0.5 for x in range(0, 1000)),
    'list': list(list(i) for i in string.ascii_letters),
    'tuple': list(tuple(i) for i in string.ascii_letters),
    'bool': [True, False],
    'dict': list(dict(a=random.choice(list(range(0, 10000)))) for a in range(100)),
    'set': list(set(i) for i in list(string.ascii_letters))
}


def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    new_list = []
    for element in range(amount):
        new_list.append(random.choice(data_type_dictionary[data_type]))
    return new_list


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    """
    new_list = []
    data_type_amount_dict = {}
    for element in inputs:
        data_type = element[1]
        amount = element[0]
        if data_type in data_type_amount_dict:
            if data_type_amount_dict[data_type] < amount:
                data_type_amount_dict[data_type] = amount
        else:
            data_type_amount_dict[data_type] = amount
    for key, value in data_type_amount_dict.items():
        new_list.extend(generate_list(value, key))
    return new_list


def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """
    new_list = generate_combined_list(inputs)
    for i in new_list:
        if new_list.count(i) > 1:
            if type(i) is int:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['int'])
            elif type(i) is float:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['float'])
            elif type(i) is str:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['string'])
    return new_list


def generate_combined_list_unique_advanced(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    All the data types from the first function are used here.
    The returned list can contain only unique elements.
    """
    new_list = generate_combined_list(inputs)
    for i in new_list:
        if new_list.count(i) > 1:
            if type(i) is int:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['int'])
            elif type(i) is float:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['float'])
            elif type(i) is str:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['string'])
            elif type(i) is tuple:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['tuple'])
            elif type(i) is dict:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['dict'])
            elif type(i) is set:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['set'])
            elif type(i) is bool:
                new_list[new_list.index(i)] = random.choice(data_type_dictionary['bool'])
    return new_list


if __name__ == '__main__':
    # The given outputs are only some of possible outputs, for example for (3, 'string')
    # in the first part an output of ["kass", "koer", "kana"] would also work.

    # Part 1
    print(generate_list(2, 'set'))  # [set(), set()]
    print(generate_list(3, 'string'))  # ["a", "kass", "a"]
    print(generate_list(1, 'list'))  # [[]]
    print(generate_list(5, 'int'))  # [1, 2, 3, 3, 3]
    print()

    # Part 2
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [0, 0, 0, 0, 0]
    print(generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')]))  # [100, 80, 60, 40, 20]
    print(generate_combined_list([(2, 'list'), (3, 'string')]))  # ["a", [], "a", [], "a"]
    print(generate_combined_list([(2, 'float'), (3, 'dict')]))  # [{}, {}, {}, 3.14, 3.15]
    print()

    # Part 3
    print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))  # [43, 93, 4.3, 2.1]
    print()

    # Part 4
    print(generate_combined_list_unique_advanced([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique_advanced([(2, 'list'), (3, 'string')]))  # ["a", [2], "asd", [], "abc"]
    print(
        generate_combined_list_unique_advanced([(2, 'float'), (3, 'dict')]))  # [{3: "abd"}, {"a": "a"}, {}, 3.14, 3.15]
    print()
