"""ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """
    id_code = ""
    count = 0
    for character in text:
        if character.isdigit():
            id_code += character
            count += 1
    if count > 11:
        return "Too many numbers!"
    elif count < 11:
        return "Not enough numbers!"
    else:
        return id_code


def is_valid_gender_number(numb: int) -> bool:
    """description."""
    if 6 >= numb >= 1:
        return True
    else:
        return False


def get_gender(numb: int):
    """description."""
    if 1 <= numb <= 6:
        if numb % 2 != 0:
            return "male"
        else:
            return "female"
    else:
        return None


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 1 <= month_number <= 12:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if 1 <= birth_number <= 999:
        return True
    else:
        return False


def is_leap_year(year: int) -> bool:
    """Define that if this year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    if 1 <= birth_number <= 10:
        return "Kuressaare"
    elif 11 <= birth_number <= 20 or 271 <= birth_number <= 370:
        return "Tartu"
    elif 21 <= birth_number <= 220 or 471 <= birth_number <= 710:
        return "Tallinn"
    elif 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    elif 371 <= birth_number <= 420:
        return "Narva"
    elif 421 <= birth_number <= 470:
        return "Pärnu"
    elif 711 <= birth_number <= 999:
        return "undefined"
    else:
        return "Wrong input!"


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    year = 0
    if 1 <= gender_number <= 6 and 1 <= year_number <= 99:
        if gender_number == 1 or gender_number == 2:
            year += 1800
        elif gender_number == 4 or gender_number == 3:
            year += 1900
        else:
            year += 2000
    year += year_number
    return year


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    if id_code.isdigit() and len(id_code) == 11:
        numbers = list(id_code[:10])
        first_round = 1 * int(numbers[0]) + 2 * int(numbers[1]) + 3 * int(numbers[2]) + 4 * int(numbers[3]) \
                      + 5 * int(numbers[4]) + 6 * int(numbers[5]) + 7 * int(numbers[6]) + 8 * int(numbers[7]) \
                      + 9 * int(numbers[8]) + 1 * int(numbers[9])
        valid_number = first_round % 11
        if 10 > valid_number == int(id_code[10]):
            return True
        elif valid_number >= 10:
            second_round = 3 * int(numbers[0]) + 4 * int(numbers[1]) + 5 * int(numbers[2]) + 6 * int(numbers[3]) \
                           + 7 * int(numbers[4]) + 8 * int(numbers[5]) + 9 * int(numbers[6]) + 1 * int(numbers[7]) \
                           + 2 * int(numbers[8]) + 3 * int(numbers[9])
            valid_number2 = second_round % 11
            if 10 > valid_number2 == int(id_code[10]):
                return True
            elif valid_number2 >= 10 and int(id_code[10]) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]
    if month_number in months_with_30_days and 1 <= day_number <= 30:
        return True
    elif month_number in months_with_31_days and 1 <= day_number <= 31:
        return True
    elif month_number == 2:
        if is_leap_year(get_full_year(gender_number, year_number)) and 1 <= day_number <= 29:
            return True
        if not is_leap_year(get_full_year(gender_number, year_number)) and 1 <= day_number <= 28:
            return True
        else:
            return False
    else:
        return False


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if is_valid_control_number(id_code):
        return True
    else:
        return False


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_valid_control_number(id_code):
        gender = get_gender(int(id_code[0]))
        month = int(id_code[3]) * 10 + int(id_code[4])
        day = int(id_code[5]) * 10 + int(id_code[6])
        year = get_full_year(int(id_code[0]), (int(id_code[1]) * 10 + int(id_code[2])))
        location = get_birth_place(int(id_code[7]) * 100 + int(id_code[8]) * 10 + int(id_code[9]))
        return f'This is a {gender} born on {day:02}.{month:02}.{year}. in {location}.'
    else:
        return 'Given invalid ID code!'


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
