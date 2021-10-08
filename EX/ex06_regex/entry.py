"""Regex, I think."""
import re


class Entry:
    """Entry class."""

    def __init__(self, first_name: str, last_name: str, id_code: str, phone_number: str, date_of_birth: str,
                 address: str):
        """Init."""
        self.first_name = first_name
        self.last_name = last_name
        self.id_code = id_code
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.address = address

    def format_date(self):
        """
        Return the date in the following format: 'Day: {day}, Month: {month}, Year: {year}'.

        Just for fun, no points gained or lost from this.

        Example: 'Day: 06, Month: 11, Year: 1995'
        If the object doesn't have date of birth given, return None.
        :return:
        """
        if self.date_of_birth is None:
            return None
        else:
            date = self.date_of_birth.split('-')
        return f'Day: {date[0]}, Month: {date[1]}, Year: {date[2]}'

    def __repr__(self) -> str:
        """Object representation."""
        return f"Name: {self.first_name} {self.last_name}\n" \
               f"ID code: {self.id_code}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Date of birth: {self.format_date()}\n" \
               f"Address: {self.address}"

    def __eq__(self, other) -> bool:
        """
        Compare two entries.

        This method is perfect. Don't touch it.
        """
        return self.first_name == other.first_name\
            and self.last_name == other.last_name\
            and self.id_code == other.id_code\
            and self.phone_number == other.phone_number\
            and self.date_of_birth == other.date_of_birth\
            and self.address == other.address


def parse(row: str):
    """
    Parse data from input string.

    :param row: String representation of the data.
    :return: Entry object with filled values
    """
    first_name = re.findall(r'^[A-Z][a-z]+', row)
    if not first_name:
        name1 = None
    else:
        name1 = first_name[0]
        row = row.replace(name1, '')

    last_name = re.findall(r'^[A-Z][a-z]+', row)
    if not last_name:
        name2 = None
    else:
        name2 = last_name[0]
        row = row.replace(name2, '')

    id_code = re.findall(r'^\d{11}', row)
    row = row.replace(id_code[0], '')

    phone_number = re.findall(r"^(\+\d{3}|\+\d{3} |(?<!\d))(\d{7,8})", row)
    if not phone_number:
        phone = None
    else:
        phone = phone_number[0][0] + phone_number[0][1]
        row = row.replace(phone, '')

    date_of_birth = re.findall(r'^\d\d\-\d\d\-\d{4}', row)
    if not date_of_birth:
        date = None
    else:
        date = date_of_birth[0]
        row = row.replace(date, '')

    if not row:
        address = None
    else:
        address = row
    person = Entry(name1, name2, id_code[0], phone, date, address)
    return person


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: None None
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: None
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: None
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 5688736402-12-1998'))
    """Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: None
    """
