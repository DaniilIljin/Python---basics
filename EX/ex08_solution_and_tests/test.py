"""Ex08 testing."""
import solution


def test_students_study_right_time_for_coffee():
    for time in range(1, 25):
        if 1 <= time <= 4:
            assert solution.students_study(time, False) is True
            assert solution.students_study(time, True) is False
        elif 5 <= time <= 17:
            assert solution.students_study(time, True) is True
            assert solution.students_study(time, False) is False
        elif 18 <= time <= 24:
            assert solution.students_study(time, True) is True
            assert solution.students_study(time, False) is True
