"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""



def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return create_a_table(input_string)


def get_info_for_table(t: str) -> list:
    """O."""
    list_of_info = []
    m = re.finditer(r'(([0-2]\d)\D([0-5]\d)|(\d)\D([0-5]\d)|([0-2]\d)\D(\d)|(\d)\D(\d)) +(([A-Za-z]+)|([^A-Za-z]))', t)
    for match in m:
        if None not in [match.group(2), match.group(3), match.group(11)]:
            list_of_info.append([match.group(2), match.group(3), match.group(11)])
        elif None not in [match.group(4), match.group(5), match.group(11)]:
            list_of_info.append([match.group(4), match.group(5), match.group(11)])
        elif None not in [match.group(6), match.group(7), match.group(11)]:
            list_of_info.append([match.group(6), match.group(7), match.group(11)])
        elif None not in [match.group(8), match.group(9), match.group(11)]:
            list_of_info.append([match.group(8), match.group(9), match.group(11)])
        elif None not in [match.group(2), match.group(3), match.group(12)]:
            list_of_info.append([match.group(2), match.group(3), 'No items found'])
        elif None not in [match.group(4), match.group(5), match.group(12)]:
            list_of_info.append([match.group(4), match.group(5), 'No items found'])
        elif None not in [match.group(6), match.group(7), match.group(12)]:
            list_of_info.append([match.group(6), match.group(7), 'No items found'])
        elif None not in [match.group(8), match.group(9), match.group(12)]:
            list_of_info.append([match.group(8), match.group(9), 'No items found'])
    return list_of_info


def normalize_data(text: str) -> list:
    """O."""
    info = get_info_for_table(text)
    normalized_data_list = []
    for element in info:
        updated_element = []
        hours = element[0]
        minutes = element[1]
        item = element[2]
        if item != 'No items found':
            item = item.lower()
        if 0 <= int(hours) <= 24:
            if 0 < int(hours) < 12:
                time = '{:02d}'.format(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.append([time, item])
                normalized_data_list.extend(updated_element)
            elif 12 < int(hours) < 24:
                hours = str(int(hours) % 12)
                time = '{:02d}'.format(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' PM'
                updated_element.append([time, item])
                normalized_data_list.extend(updated_element)
            elif hours == '12':
                time = '{:02d}'.format(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' PM'
                updated_element.append([time, item])
                normalized_data_list.extend(updated_element)
            elif hours == '24' and int(minutes) == 0:
                hours = '12'
                time = '{:02d}'.format(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.append([time, item])
                normalized_data_list.extend(updated_element)
            elif int(hours) == 0:
                hours = '12'
                time = '{:02d}'.format(int(hours)) + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.append([time, item])
                normalized_data_list.extend(updated_element)
    return normalized_data_list


def creating_dictionary(text: str) -> dict:
    """O."""
    data = normalize_data(text)
    new_dict = {}
    for element in data:
        time = element[0]
        item = element[1]
        if time in new_dict:
            new_dict[time] = new_dict[time] + [item]
        else:
            new_dict[time] = [item]
    return new_dict


def sort_dictionary(text: str) -> dict:
    """O."""
    new_dict = creating_dictionary(text)
    for element in new_dict:
        new_dict[element] = sorted(list(set(new_dict[element])))
    return new_dict


def change_value_to_string(text: str) -> dict:
    new_dict = sort_dictionary(text)
    changed_dict = {}
    for element in new_dict:
        if new_dict[element] != ['No items found']:
            changed_dict[element] = ''
            for element1 in new_dict[element]:
                if element1 != new_dict[element][-1]:
                    changed_dict[element] = f'{element1}, '
                else:
                    changed_dict[element] = changed_dict[element] + str(element1)
        else:
            changed_dict[element] = 'No items found'
    return changed_dict


def sort_time(time: list) -> list:
    sorted_list_of_time = []
    list_of_twelve = []
    list_of_others = []
    for element1 in time:
        if element1[:2] == '12':
            list_of_twelve.append(element1)
        else:
            list_of_others.append(element1)
    sorted_list_of_time.extend(sorted(list_of_twelve))
    sorted_list_of_time.extend(sorted(list_of_others))
    return sorted_list_of_time


def create_a_table(text: str) -> str:
    """O ."""
    final_dict = change_value_to_string(text)
    if final_dict != {}:
        new_list = []
        for element in final_dict.values():
            new_list.append(len(element))
        if len(new_list) > 0:
            second_side_maximum_length = max(new_list),
        else:
            second_side_maximum_length = 0,
        table = ''
        line_with_minuses = '-' * 14 + '-' * second_side_maximum_length[0] + '--\n'
        table += line_with_minuses
        second_line = '|' + "{:>10}".format("time") + ' | items' + ' ' * (second_side_maximum_length[0] - 5) + ' |\n'
        table += second_line + line_with_minuses
        list_of_am = []
        list_of_pm = []
        for element2 in final_dict.keys():
            if element2[-2:] == 'AM':
                list_of_am.append(element2)
            else:
                list_of_pm.append(element2)
        sorted_list_of_am = sort_time(list_of_am)
        sorted_list_of_pm = sort_time(list_of_pm)
        all_time = sorted_list_of_am + sorted_list_of_pm
        for element1 in all_time:
            if element1[0] == '0':
                table += f'|{element1[1:]:>{10}} | {final_dict[element1]:{second_side_maximum_length[0]}} |\n'
            else:
                table += f'|{element1:>{10}} | {final_dict[element1]:{second_side_maximum_length[0]}} |\n'
        table += line_with_minuses
    else:
        table = "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    return table


if __name__ == '__main__':
    print(create_schedule_string("9:0011:010:00"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")

