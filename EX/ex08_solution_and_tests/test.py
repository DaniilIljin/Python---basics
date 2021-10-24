"""Ex08 testing."""
import solution


def test_students_study_right_time_for_coffee():
    """Test the right time for coffee."""
    for time in range(1, 25):
        if 1 <= time <= 4:
            assert solution.students_study(time, False) is False
            assert solution.students_study(time, True) is False
        elif 5 <= time <= 17:
            assert solution.students_study(time, True) is True
            assert solution.students_study(time, False) is False
        else:
            assert solution.students_study(time, True) is True
            assert solution.students_study(time, False) is True


def test_lottery_testing_fives():
    """Test all fives."""
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_testing_testing_diff_a_b_c():
    """All different."""
    for num in range(100):
        a = num
        b = num + 1
        c = num + 2
        assert solution.lottery(a, b, c) == 1


def test_lottery_testing_zero():
    """All zeros."""
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_testing_similar_positive():
    """Test positive."""
    for num in range(1, 5):
        assert solution.lottery(num, num, num) == 5


def test_lottery_testing_similar_negative():
    """Test negative."""
    for num in range(-15, -5):
        assert solution.lottery(num, num, num) == 5


def test_lottery_testing_same_a_b_diff_c():
    """Two are same."""
    for num in range(1, 4):
        assert solution.lottery(num, num, num + 1) == 0


def test_lottery_testing_same_a_c_diff_b():
    """Two are same."""
    for num in range(1, 5):
        assert solution.lottery(num, num + 1, num) == 0


# def test_lottery_testing_same_c_b_diff_a():
#     """Two are same."""
#     assert solution.lottery(6, 1, 1) == 0
def test_fruit_order__all_zero():
    """All zeros."""
    assert solution.fruit_order(0, 0, 0) == 0


def test_fruit_order__only_big_more_than_required_no_match():
    """O."""
    assert solution.fruit_order(0, 5, 8) == -1


def test_fruit_order__only_big_exact_match():
    assert solution.fruit_order(0, 2, 10) == 0


def test_fruit_order__only_small_exact_match():
    assert solution.fruit_order(5, 0, 5) == 5


def test_fruit_order__zero_amount_zero_small():
    assert solution.fruit_order(0, 5, 0) == 0


def test_fruit_order__zero_amount_zero_big():
    assert solution.fruit_order(5, 0, 0) == 0


def test_fruit_order__zero_amount_others_not_zero():
    assert solution.fruit_order(5, 6, 0) == 0


def test_fruit_order__only_big_not_enough_but_multiple_of_5():
    assert solution.fruit_order(0, 3, 20) == -1


def test_fruit_order__only_big_more_than_required_match():
    assert solution.fruit_order(0, 6, 20) == 0


def test_fruit_order__only_small_match_more_than_5_smalls():
    assert solution.fruit_order(6, 0, 6) == 6


def test_fruit_order__only_small_not_enough_more_than_5_smalls():
    assert solution.fruit_order(6, 0, 7) == -1


def test_fruit_order__only_small_more_than_required():
    assert solution.fruit_order(7, 0, 6) == 6


def test_fruit_order__all_positive_exact_match():
    assert solution.fruit_order(7, 3, 22) == 7


def test_fruit_order__use_all_smalls_some_bigs():
    assert solution.fruit_order(2, 5, 22) == 2


def test_fruit_order__use_some_smalls_all_bigs():
    assert solution.fruit_order(7, 4, 22) == 2


def test_fruit_order__use_some_smalls_some_bigs():
    assert solution.fruit_order(7, 8, 22) == 2


def test_fruit_order__enough_bigs_not_enough_smalls():
    assert solution.fruit_order(1, 5, 22) == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    assert solution.fruit_order(6, 3, 22) == -1


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    assert solution.fruit_order(3, 27, 140) == -1
