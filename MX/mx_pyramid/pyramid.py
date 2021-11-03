"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    if base >= 0:
        if base % 2 == 0:
            amounts_of_char_in_list = [i for i in range(base + 1) if i % 2 == 0 and i != 0]
        else:
            amounts_of_char_in_list = [i for i in range(base + 1) if i % 2 != 0]
        pyramid = []
        for element in amounts_of_char_in_list:
            layer_of_pyramid = []
            spaces = int((base - element) / 2)
            layer_of_pyramid.extend([' ' for i in range(spaces)])
            layer_of_pyramid.extend([char for i in range(element)])
            layer_of_pyramid.extend([' ' for i in range(spaces)])
            pyramid.append(layer_of_pyramid)
        return pyramid
    else:
        return []


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    connected_pyramids = []
    layers_of_space = []
    if pyramid_b == pyramid_a == []:
        return []
    elif len(pyramid_a) == len(pyramid_b):
        for index, layer in enumerate(pyramid_a):
            new_layer = layer + pyramid_b[index]
            connected_pyramids.append(new_layer)
        return connected_pyramids
    else:
        if len(pyramid_a) < len(pyramid_b):
            small = pyramid_a
            big = pyramid_b
        else:
            small = pyramid_b
            big = pyramid_a
        for i in range(len(small[0])):
            layers_of_space.append(' ')
        for index, layer in enumerate(big):
            new_index = -(index + 1)
            if -new_index <= len(small):
                new_layer = small[new_index] + big[new_index]
                connected_pyramids.insert(0, new_layer)
            else:
                new_layer = layers_of_space + big[new_index]
                connected_pyramids.insert(0, new_layer)
        return connected_pyramids


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    pass


if __name__ == '__main__':
    pyramid_a = make_pyramid(4, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(4, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    joined = join_pyramids(pyramid_a, pyramid_b)
    print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    # pyramid_string = to_string(joined)
    # print(pyramid_string)  # ->
    # """
    #      aa
    #  A  aaaa
    # AAAaaaaaa
    # """
