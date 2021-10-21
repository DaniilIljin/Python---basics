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
    for type_ in inputed_types:
        actual_type = types[inputed_types.index(type_)]
        answer = solution.generate_list(1, type_)
        assert type(answer[0]) == actual_type


def test_part2_minimal_possible_length():
    answer = solution.generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')])
    assert len(answer) == 5

