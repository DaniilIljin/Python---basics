"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""


def get_info_for_table(t: str) -> list:
    """O."""
    list_of_info = []
    matches = re.finditer(r'( |(?<=\n))([0-2]\d\D[0-5]\d|(?<!\d)\d\D[0-5]\d|[0-2]\d\D\d|(?<!\d)\d\D\d) +([A-Za-z])', t)
    for match in matches:
        list_of_info.append([match.group(2), match.group(3)])
    return list_of_info


def normalize_data(t: str) -> list:
    normalized_data_list = []
    all_data = get_info_for_table(t)
    for element in all_data:
        time = element[0]
        item = element[1]
        hours, minutes = re.split(r'\D', time)
        if 0 <= int(hours) <= 24:
            updated_element = []
            item = item.lower()
            if 0 < int(hours) < 12:
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' AM'
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
            elif hours == '24' and int(minutes) == 0:
                hours = '12'
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
            elif int(hours) == 0:
                hours = '12'
                new_time = hours + ':' + '{:02d}'.format(int(minutes)) + ' AM'
                updated_element.extend([new_time, item])
                normalized_data_list.append(updated_element)
    return normalized_data_list


def create_sorted_dict(t: str) -> dict:
    new_dict = {}
    needed_list = normalize_data(t)
    for element in needed_list:
        key = element[0]
        value = element[1]
        if key in new_dict:
            new_dict[key] = new_dict[key] + [value]
        else:
            new_dict[key] = [value]

    for key in new_dict:
        new_dict[key] = sorted(list(set(new_dict[key])))

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


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    my_dict = create_sorted_dict(input_string)
    if my_dict == {}:
        table = "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    else:
        list_of_lenghts = []
        for element in my_dict.values():
            list_of_lenghts.append(len(element))
        if max(list_of_lenghts) > 5:
            maximum_length = max(list_of_lenghts),
        else:
            maximum_length = 5,

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
            line_with_minuses = '-' * 12 + '-' * maximum_length[0] + '--\n'
            table += line_with_minuses
            second_line = '|' + "{:>8}".format("time") + ' | items' + ' ' * (maximum_length[0] - 5) + ' |\n'
            table += second_line + line_with_minuses
            all_time = sorted_list_of_am + sorted_list_of_pm
            for element1 in all_time:
                if element1[0] == '0':
                    table += f'|{element1[1:]:>{8}} | {my_dict[element1]:{maximum_length[0]}} |\n'
                else:
                    table += f'|{element1:>{8}} | {my_dict[element1]:{maximum_length[0]}} |\n'
            table += line_with_minuses
        else:
            table = ''
            line_with_minuses = '-' * 13 + '-' * maximum_length[0] + '--\n'
            table += line_with_minuses
            second_line = '|' + "{:>9}".format("time") + ' | items' + ' ' * (maximum_length[0] - 5) + ' |\n'
            table += second_line + line_with_minuses
            all_time = sorted_list_of_am + sorted_list_of_pm
            for element1 in all_time:
                if element1[0] == '0':
                    table += f'|{element1[1:]:>{9}} | {my_dict[element1]:{maximum_length[0]}} |\n'
                else:
                    table += f'|{element1:>{9}} | {my_dict[element1]:{maximum_length[0]}} |\n'
            table += line_with_minuses
    return table


if __name__ == '__main__':
    print(create_schedule_string("""    A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
     ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
     Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
     Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,
     est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.
    Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus
    eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum
     eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,
     in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.
     Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
      0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis
      risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.

    08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 18:19 a bibendum enim. Praesent
     dictum ante eget turpis tempor, 00:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,
     pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum
      efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 18:19 purus
      diam. 18:19 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.

    11:0 lorem
    0:60 bad
    1:2   goodone yes
    15:0 nocomma,
     18:19 yes-minus
      21:59 nopoint.
    23-59 canuseminusthere  22,0 CommaIsAlsoOk
    5:6
"""))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
