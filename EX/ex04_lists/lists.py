"""EX04 - List and Tuple."""


def generate_list(amount: int, data_type: str) -> list:
    """Write a function that returns a list with amount elements of type data_type."""
    new_list = []
    for element in range(amount):
        if data_type == 'string':
            new_list.append(str(element))
        elif data_type =='int':
            new_list.append(element)
        elif data_type == 'float':
            new_list.append(element * 0.5)
        elif data_type == 'list':
            new_list.append([element])
        elif data_type == 'tuple':
            new_list.append((element, ))
        elif data_type == 'dict':
            new_list.append(dict(element=element))
        elif data_type == 'float':
            new_list.append(element)
    return new_list


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    """



def generate_combined_list_unique(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    Data types used in this function are 'int', 'float' and 'str' (string).
    The returned list can contain only unique elements.
    """


def generate_combined_list_unique_advanced(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains
    at least 'amount' of elements of type 'data_type'.
    All the data types from the first function are used here.
    The returned list can contain only unique elements.
    """



if __name__ == '__main__':

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
    print(generate_combined_list_unique([(100, 'string')]))
    print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))  # [43, 93, 4.3, 2.1]
    print()

    # Part 4
    print(generate_combined_list_unique_advanced([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique_advanced([(2, 'list'), (3, 'string')]))  # ["a", [2], "asd", [], "abc"]
    print(
        generate_combined_list_unique_advanced([(2, 'float'), (3, 'dict')]))  # [{3: "abd"}, {"a": "a"}, {}, 3.14, 3.15]
    print()
