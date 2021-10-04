"""Hobbies."""


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    new_dict = {}
    list_of_keys = dic.keys()
    for element in list_of_keys:
        new_dict[element] = sorted(dic[element])
    return new_dict


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    new_dict = {}
    list_of_people_with_hobby = data.split('\n')
    for element in list_of_people_with_hobby:
        key, value = element.split(':')
        if key in new_dict:
            if value in new_dict[key]:
                continue
            else:
                new_dict[key] = new_dict[key] + [value]
        else:
            new_dict[key] = [value]
    return new_dict


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    new_dict_of_hobbies = {}
    new_dict = create_dictionary(data)
    for key, value in new_dict.items():
        for element in value:
            if element in new_dict_of_hobbies:
                new_dict_of_hobbies[element] = new_dict_of_hobbies[element] + [key]
            else:
                new_dict_of_hobbies[element] = [key]
    return sort_dictionary(new_dict_of_hobbies)


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    new_dict = create_dictionary(data)
    list_of_values = new_dict.values()
    list_of_length = []
    for element in list_of_values:
        list_of_length.append(len(element))
    max_of_hobbies = max(list_of_length)
    list_of_names = []
    for name in new_dict:
        if len(new_dict[name]) == max_of_hobbies:
            list_of_names.append(name)
    return sorted(list_of_names)


def find_people_with_least_hobbies(data: str) -> list:
    """
    Find the people who have least hobbies.

    :param data: given string from database
    :return: list of people with least hobbies. Sorted alphabetically.
    """
    new_dict = create_dictionary(data)
    list_of_values = new_dict.values()
    list_of_length = []
    for element in list_of_values:
        list_of_length.append(len(element))
    min_of_hobbies = min(list_of_length)
    list_of_names = []
    for name in new_dict:
        if len(new_dict[name]) == min_of_hobbies:
            list_of_names.append(name)
    return sorted(list_of_names)


def creating_dict_of_popularity(data):
    """This function create a dict of popularity for next tasks"""
    new_dict = create_dictionary(data)
    list_of_values = new_dict.values()
    all_hobbies = []
    for element in list_of_values:
        all_hobbies = all_hobbies + element
    set_of_all_hobbies = set(all_hobbies)
    dict_of_popularity = {}
    for element in set_of_all_hobbies:
        count = 0
        for value in list_of_values:
            if element in value:
                count += 1
        dict_of_popularity[element] = count
    return dict_of_popularity


def find_most_popular_hobbies(data: str) -> list:
    """
    Find the most popular hobbies.

    :param data: given string from database
    :return: list of most popular hobbies. Sorted alphabetically.
    """
    dict_of_popularity = creating_dict_of_popularity(data)
    the_most_popular = max(dict_of_popularity.values())
    list_of_hobbies = []
    for element in dict_of_popularity:
        if dict_of_popularity[element] == the_most_popular:
            list_of_hobbies.append(element)
    return sorted(list_of_hobbies)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    dict_of_popularity = creating_dict_of_popularity(data)
    the_least_popular = min(dict_of_popularity.values())
    list_of_hobbies = []
    for element in dict_of_popularity:
        if dict_of_popularity[element] == the_least_popular:
            list_of_hobbies.append(element)
    return sorted(list_of_hobbies)


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    new_dict = sort_dictionary(create_dictionary(data))
    one_big_list = []
    for element in new_dict:
        one_big_list.append(element)
    one_big_list = sorted(one_big_list)
    for element in one_big_list:
        one_big_list[one_big_list.index(element)] = (element, tuple(new_dict[element]))
    return tuple(one_big_list)


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(find_people_with_least_hobbies(sample_data))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(find_most_popular_hobbies(sample_data))  # -> ['football', 'gaming', 'sport']
    print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']

    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == ('Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre'))
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")
    # print(sort_names_and_hobbies(sample_data))