"""My first tests."""
import solution


def test_part1_int_correct_length():
    """Test possible lengths."""
    for size in range(200):
        for type_ in ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']:
            res = solution.generate_list(size, type_)
            assert len(res) == size


def test_part1_correct_type():
    """Test type in output."""
    types = [str, int, set, dict, tuple, list, float]
    inputed_types = ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']
    for index, type_ in enumerate(types):
        actual_type = inputed_types[index]
        answer = solution.generate_list(1, actual_type)
        assert isinstance(answer[0], type_)


def test_part2_testing_length():
    """Test possible lengths."""
    for type_ in ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']:
        for size in range(100):
            answer = solution.generate_combined_list([(size, type_)])
            assert len(answer) == size


def test_par2_wrong_types():
    """Test type in output."""
    types = [str, int, set, dict, tuple, list, float]
    inputed_types = ['string', 'int', 'set', 'dict', 'tuple', 'list', 'float']
    counter = 0
    for type_ in types:
        actual_type = inputed_types[counter]
        answer = solution.generate_combined_list([(1, actual_type)])
        for element in answer:
            assert isinstance(element, type_)
        counter += 1


def test_part3_testing_length():
    """Test possible lengths."""
    for type_ in ['string', 'int', 'float']:
        for size in range(100):
            answer = solution.generate_combined_list_unique([(size, type_)])
            assert len(answer) == size


def test_part3_wrong_types():
    """Test type in output."""
    types = [str, int, float]
    inputed_types = ['string', 'int', 'float']
    counter = 0
    for type_ in types:
        actual_type = inputed_types[counter]
        answer = solution.generate_combined_list_unique([(1, actual_type)])
        for element in answer:
            assert isinstance(element, type_)
        counter += 1


def test_part3_uniq_elements():
    """Test if all elements are unique."""
    inputed_types = ['string', 'int', 'float']
    for type_ in inputed_types:
        answer = solution.generate_combined_list_unique([(10, type_)])
        for element in answer:
            assert answer.count(element) == 1
