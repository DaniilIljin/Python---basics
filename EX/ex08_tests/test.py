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


def test_part2_minimal_testing_length():
    for type_ in ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']:
        for size in range(100):
            answer = solution.generate_combined_list([(size, type_)])
            assert len(answer) == size


def test_par2_wrong_types():
    answer = solution.generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')])
    for item in answer:
        assert isinstance(item, int)
