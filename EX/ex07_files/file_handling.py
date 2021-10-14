"""Fear files EX07."""

import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r") as file_content:
        content = file_content.read()
    return content


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename, "r") as file_content:
        content_in_list = file_content.readlines()
    for element in content_in_list:
        content_in_list[content_in_list.index(element)] = element.strip()
    return content_in_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    new_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            new_list.append(row)
    return new_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, 'w') as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, 'w') as file:
        for element in lines:
            if element != lines[-1]:
                file.write(element + '\n')
            else:
                file.write(element)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    new_dict = {}
    list_of_all_data = []
    for file in [dates_file, towns_file]:
        with open(file) as csv_file:
            new_list = []
            csv_reader = csv.reader(csv_file, delimiter=':')
            for row in csv_reader:
                new_list.append(row)
            list_of_all_data.append(new_list)
    for element in list_of_all_data[0]:
        name = element[0]
        date = element[1]
        new_dict[name] = [date]
    special_list = []
    for element1 in list_of_all_data[1]:
        name1 = element1[0]
        town1 = element1[1]
        if name1 in new_dict:
            new_dict[name1].append(town1)
        else:
            special_list.append([name1, town1, '-'])
    one_big_list = [['name', 'town', 'date']]
    for element2 in list_of_all_data[0]:
        if len(new_dict[element2[0]]) == 2:
            one_big_list.append([element2[0], new_dict[element2[0]][1], new_dict[element2[0]][0]])
        else:
            one_big_list.append([element2[0], '-', new_dict[element2[0]][0]])
    one_big_list.extend(special_list)
    write_csv_file(csv_output, one_big_list)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.
    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    list_of_info = []
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            list_of_info.append(row)
    if list_of_info == [] or list_of_info[0] == [] or len(list_of_info) == 1:
        return []
    else:
        big_list = []
        header = list_of_info[0]
        list_of_info.pop(0)
        for element in list_of_info:
            new_dict = {}
            for element1 in element:
                new_dict[header[element.index(element1)]] = element1
            big_list.append(new_dict)
    return big_list


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    the_big_one = []
    list_of_all_keys = []
    for dictionary in data:
        list_of_all_keys.extend(dictionary.keys())
    header = list(set(list_of_all_keys))
    the_big_one.append(header)
    for dictionary1 in data:
        new_list = []
        for element1 in header:
            if element1 in dictionary1:
                new_list.append(dictionary1[element1])
            else:
                new_list.append('')
        the_big_one.append(new_list)
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        for row in the_big_one:
            csv_writer.writerow(row)
