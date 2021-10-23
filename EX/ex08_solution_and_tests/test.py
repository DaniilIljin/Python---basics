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


def test_lottery_testing_similar():
    """Test numbers in range(100)."""
    for num in range(100):
        assert solution.lottery(num, num, num) == 5

#
# def test_lottery_testing_testing_diff_a_b_c():
#     for num in range(100):
#         a = num
#         b = num + 1
#         c = num + 2
#         assert solution.lottery(a, b, c) == 1
