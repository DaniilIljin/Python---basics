import pytest
import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_correct_type():
    types = [str, int, set, dict, tuple, list]
    inputed_types = ['string', 'int', 'set', 'dict', 'tuple', 'list']
    for index, type_ in types:
        actual_type = inputed_types[index]
        answer = solution.generate_list(1, actual_type)
        assert isinstance(answer[0], type_)


def test_part2_minimal_possible_length():
    answer = solution.generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')])
    assert len(answer) == 5

