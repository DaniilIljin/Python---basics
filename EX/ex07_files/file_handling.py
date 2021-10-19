"""Fear files EX07."""

import csv
import datetime
import glob
import re


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
    if data:
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
    else:
        with open(filename, 'w', newline='') as csv_file:
            pass


def create_checking_type_list(list_of_info):
    """Create lists of data to check its type."""
    header = list_of_info[0]
    list_of_info.pop(0)
    checking_type_list = []
    number_of_lists = len(header)
    for number in range(number_of_lists):
        checking_type_list.append([])
    for lst in list_of_info:
        counter = 0
        for element1 in lst:
            checking_type_list[counter].append(element1)
            counter += 1
    return checking_type_list


def choose_the_scenaries_to_make_list_of_dicts(list_of_info: list) -> list:
    """Find the scenario for a group of objects."""
    checking_type_list = create_checking_type_list(list_of_info)
    total_list_of_types = []
    for list1 in checking_type_list:
        list_of_types = []
        for element2 in list1:
            if element2 != '-':
                if [element2] == re.findall(r'\d\d\.\d\d\.\d{4}', element2):
                    day, month, year = element2.split('.')
                    if datetime.date(int(year), int(month), int(day)):
                        list_of_types.append(type(datetime.date(int(year), int(month), int(day))))
                    else:
                        list_of_types.append(type(element2))
                elif element2.isdigit():
                    list_of_types.append(type(int(element2)))
                else:
                    list_of_types.append(type(element2))
        total_list_of_types.append(list_of_types)
    list_of_scenarios = []
    for element in total_list_of_types:
        if element:
            if element.count(element[0]) == len(element):
                list_of_scenarios.append(0)
            else:
                list_of_scenarios.append(1)
        else:
            list_of_scenarios.append(0)
    return list_of_scenarios


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,01.01.2020

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
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
        scenarios = choose_the_scenaries_to_make_list_of_dicts(list_of_info)
        for element in list_of_info:
            new_dict = {}
            for element1 in element:
                if element1 != '-':
                    if scenarios[element.index(element1)] == 0:
                        if element1.isdigit():
                            new_dict[header[element.index(element1)]] = int(element1)
                        elif [element1] == re.findall(r'\d\d\.\d\d.\d{4}', element1):
                            day, month, year = element1.split('.')
                            new_dict[header[element.index(element1)]] = datetime.date(int(year), int(month), int(day))
                        elif element1 == '-':
                            new_dict[header[element.index(element1)]] = None
                        else:
                            new_dict[header[element.index(element1)]] = str(element1)
                    else:
                        new_dict[header[element.index(element1)]] = str(element1)
                else:
                    new_dict[header[element.index(element1)]] = None
                element[element.index(element1)] = 'nothing'
            big_list.append(new_dict)
    return big_list


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.

    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    list_of_all_data = []
    for file in glob.glob(directory + '/*.csv'):
        list_of_all_data.extend(read_csv_file_into_list_of_dicts_using_datatypes(file))
    all_ids = []
    for dict1 in list_of_all_data:
        if 'id' in dict1:
            all_ids.append(dict1['id'])
    big_dicts = []
    for id_ in all_ids:
        connected_dict = {}
        for dict2 in list_of_all_data:
            if id_ in dict2.values():
                connected_dict.update(dict2)
        big_dicts.append(connected_dict)
    new_dict = {}
    for dict2 in big_dicts:
        new_dict[dict2['id']] = dict2
    return new_dict


def calculate_the_age(date1, date2):
    """Calculate the age of a person."""
    day, month, year = date1.strftime('%d.%m.%Y').split('.')
    day1, month1, year1 = date2.strftime('%d.%m.%Y').split('.')
    if int(year1) - int(year) > 0:
        if int(month1) - int(month) < 0:
            age = int(year1) - int(year) - 1
        elif int(month1) - int(month) > 0:
            age = int(year1) - int(year)
        elif int(month1) == int(month) and int(day1) - int(day) < 0:
            age = int(year1) - int(year) - 1
        else:
            age = age = int(year1) - int(year)
    else:
        age = 0
    return age


def date_magic(x):
    """Convert the date for lambda."""
    day, month, year = x.strftime('%d.%m.%Y').split('.')
    x = int(year) * 1000 + int(month) * 100 + int(day)
    return x

def add_status(data):
    """Add status"""
    dead = []
    alive = []
    idk = []
    for person in data:
        if data[person]['death'] is not None and data[person]['birth'] is not None:
            data[person]['status'] = 'dead'
            dead.append(person)
        elif data[person]['birth'] is not None:
            data[person]['death'] = '-'
            data[person]['status'] = 'alive'
            alive.append(person)
        else:
            data[person]['death'] = '-'
            data[person]['birth'] = '-'
            data[person]['status'] = 'alive'
            data[person]['age'] = -1
            idk.append(data[person])
    return dead, alive, idk, data


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the files should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before people with  name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    data = read_people_data(person_data_directory)
    dead, alive, idk, data = add_status(data)
    sorted_with_normal_age = []
    for person in data:
        if data[person] not in idk:
            if data[person]['death'] == '-':
                age = calculate_the_age(data[person]['birth'], datetime.date.today())
                data[person]['age'] = age
                sorted_with_normal_age.append(data[person])
            else:
                age = calculate_the_age(data[person]['birth'], data[person]['death'])
                data[person]['age'] = age
                sorted_with_normal_age.append(data[person])
    all_sorted_data = []
    all_sorted_data.extend(sorted(sorted_with_normal_age, key=lambda x: (
        x['age'], -date_magic(x['birth']), x['name'] if 'name' in x else '', x['id'])))
    all_sorted_data.extend(sorted(idk, key=lambda t: (t['name'] if t['name'] is None else '', t['id'])))
    for dict_ in all_sorted_data:
        if dict_['birth'] != '-' and dict_['death'] != '-':
            dict_['birth'] = dict_['birth'].strftime('%d.%m.%Y')
            dict_['death'] = dict_['death'].strftime('%d.%m.%Y')
        elif dict_['birth'] != '-':
            dict_['birth'] = dict_['birth'].strftime('%d.%m.%Y')
        elif dict_['death'] != '-':
            dict_['death'] = dict_['death'].strftime('%d.%m.%Y')
    write_list_of_dicts_to_csv_file(report_filename, all_sorted_data)
