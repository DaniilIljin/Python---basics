"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""


def get_info_for_table(t: str) -> list:
    """To find all needed data."""
    list_of_info = []
    matches = re.finditer(r'( |(?<=\n))([0-2]\d\D[0-5]\d|(?<!\d)\d\D[0-5]\d|[0-2]\d\D\d|(?<!\d)\d\D\d) +([A-Za-z]+)', t)
    for match in matches:
        list_of_info.append([match.group(2), match.group(3)])
    return list_of_info


def normalize_data(t: str) -> list:
    """To sort the data and normalize it."""
    normalized_data_list = []
    all_data = get_info_for_table(t)
    for element in all_data:
        time = element[0]
        item = element[1]
        hours, minutes = re.split(r'\D', time)
        if 0 <= int(hours) < 24:
            updated_element = []
            item = item.lower()
            if 0 < int(hours) < 12:
                new_time = str(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
            elif 12 < int(hours) < 24:
                hours = str(int(hours) % 12)
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' PM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
            elif hours == '12':
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' PM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
            elif int(hours) == 0:
                hours = '12'
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
    return normalized_data_list


def create_sorted_dict(t: str) -> dict:
    """To create a dictionary with normalized time and string."""
    new_dict = {}
    needed_list = normalize_data(t)
    for element in needed_list:
        key = element[0]
        value = element[1]
        if key in new_dict:
            if value not in new_dict[key]:
                new_dict[key] = new_dict[key] + [value]
        else:
            new_dict[key] = [value]
    changed_dict = {}
    for key in new_dict:
        changed_dict[key] = ''
        for element in new_dict[key]:
            if element != new_dict[key][-1]:
                changed_dict[key] += f'{element}, '
            else:
                changed_dict[key] += str(element)
    return changed_dict


def sort_time(time: list) -> list:
    """To sort time for table."""
    sorted_list_of_time = []
    list_of_twelve = []
    list_of_one_hour_digit = []
    list_of_two_hour_digit = []
    for element1 in time:
        if element1[:2] == '12':
            list_of_twelve.append(element1)
        elif len(element1.split(':')[0]) == 2:
            list_of_two_hour_digit.append(element1)
        else:
            list_of_one_hour_digit.append(element1)
    sorted_list_of_time.extend(sorted(list_of_twelve))
    sorted_list_of_time.extend(sorted(list_of_one_hour_digit))
    sorted_list_of_time.extend(sorted(list_of_two_hour_digit))
    return sorted_list_of_time


def find_max_length_for_table(my_dict: dict) -> int:
    """To find max length of table."""
    list_of_lengths = []
    for element in my_dict.values():
        list_of_lengths.append(len(element))
    if max(list_of_lengths) > 5:
        maximum_length = max(list_of_lengths)
    else:
        maximum_length = 5
    return maximum_length


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    my_dict = create_sorted_dict(input_string)
    if my_dict == {}:
        table = "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    else:
        maximum_length = find_max_length_for_table(my_dict)
        list_of_am = []
        list_of_pm = []
        for element2 in my_dict.keys():
            if element2[-2:] == 'AM':
                list_of_am.append(element2)
            else:
                list_of_pm.append(element2)
        sorted_list_of_am = sort_time(list_of_am)
        sorted_list_of_pm = sort_time(list_of_pm)
        all_time = sorted_list_of_am + sorted_list_of_pm
        lengths = []
        for element4 in all_time:
            lengths.append(len(element4))
        if max(lengths) == 7:
            table = ''
            line_with_minuses = '-' * 12 + '-' * maximum_length + '--\n'
            table += line_with_minuses
            second_line = '|' + "{:>8}".format("time") + ' | items' + ' ' * (maximum_length - 5) + ' |\n'
            table += second_line + line_with_minuses
            all_time = sorted_list_of_am + sorted_list_of_pm
            for element1 in all_time:
                if element1[0] == '0':
                    table += f'|{element1[1:]:>{8}} | {my_dict[element1]:{maximum_length}} |\n'
                else:
                    table += f'|{element1:>{8}} | {my_dict[element1]:{maximum_length}} |\n'
            table += line_with_minuses
        else:
            table = ''
            line_with_minuses = '-' * 13 + '-' * maximum_length + '--\n'
            table += line_with_minuses
            second_line = '|' + "{:>9}".format("time") + ' | items' + ' ' * (maximum_length - 5) + ' |\n'
            table += second_line + line_with_minuses
            all_time = sorted_list_of_am + sorted_list_of_pm
            for element1 in all_time:
                if element1[0] == '0':
                    table += f'|{element1[1:]:>{9}} | {my_dict[element1]:{maximum_length}} |\n'
                else:
                    table += f'|{element1:>{9}} | {my_dict[element1]:{maximum_length}} |\n'
            table += line_with_minuses
    return table


if __name__ == '__main__':
    print(create_schedule_string(""" 12n34 uy 12o34 fg 12n34 uy"""))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
