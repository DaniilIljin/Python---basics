import pytest
import solution


def test_part1_int_correct_len():
    for size in range(200):
        for type_ in ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']:
            res = solution.generate_list(size, type_)
            assert len(res) == size


def test_part1_correct_type():
    types = [str, int, set, dict, tuple, list, float]
    inputed_types = ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']
    for index, type_ in enumerate(types):
        actual_type = inputed_types[index]
        answer = solution.generate_list(1, actual_type)
        assert isinstance(answer[0], type_)



def test_part2_minimal_possible_length():
    for type_ in ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']:
        answer = solution.generate_combined_list([(3, type_), (5, type_), (4, type_)])
        assert len(answer) == 5

