"""My tests."""
import santas_workshop


def test_info_list_creation():
    """Testing received info from files."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    assert s.recieve_info_from_file('testing_1.csv') == [['Tanya', ' United Kingdom'], ['Jamie', ' Canada'], ['Chelsea', ' South Africa'],
                                                         ['Taylor', ' United Kingdom'], ['Hannah', ' United States of America']]


def test_children_creation():
    """Testing creation of class object Child."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    s.create_children(s.nice_list, 'nice')
    a = [[child_.name, child_.status] for child_ in s.children]
    for child in s.nice_list:
        b = [child_.name for child_ in s.children]
        assert child[0] in [child_.name for child_ in s.children]


def test_wishes_finder():
    """."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    s.create_children(s.nice_list, 'nice')
    s.create_children(s.naughty_list, 'naughty')
    for child in s.children:
        assert s.find_childs_wishes_by_name(child.name) == child.wishes


def test_child_recieve_only_three_or_less_presents():
    """."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    s.create_children(s.naughty_list, 'naughty')
    s.create_children(s.nice_list, 'nice')
    for child in s.children:
        if child.status == 'naughty':
            assert len(child.wishes) <= 3


def test_create_presents():
    """."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    s.create_children(s.nice_list, 'nice')
    s.create_children(s.naughty_list, 'naughty')
    s.create_presents()
    for child in s.children:
        a = child.name
        if child.status == 'naughty':
            assert child.wishes[0] in [present.name for present in s.presents]
        else:
            for wish in child.wishes:
                assert wish in [present.name for present in s.presents]


def test_receive_presents_info():
    """."""
    s = santas_workshop.Santas_factory('testing_3.csv', 'testing_1.csv', 'testing_2.csv')
    for present in ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition']:
        s.creating_presents_info(present)
        assert present in [present_.name for present_ in s.presents]
