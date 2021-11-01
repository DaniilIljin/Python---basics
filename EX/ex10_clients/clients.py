"""Client."""
from typing import Optional
import csv


list_of_clients = []


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """
    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.
        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        return (self.current_amount - self.starting_amount) / self.account_age


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    new_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            new_list.append(row)
    list_of_names = []
    for index, person in enumerate(new_list):
        new_client = Client(person[0], person[1], int(person[2]), int(person[3]), int(person[4]))
        list_of_names.append(new_client.__repr__())
        list_of_clients.append(new_client)
    return list_of_names


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    clients_of_the_bank = []
    for client in list_of_clients:
        if client.bank == bank:
            clients_of_the_bank.append(client)
    return clients_of_the_bank


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    checking_earnings = []
    for client in list_of_clients:
        earnings = client.current_amount - client.starting_amount
        if earnings <= 0:
            checking_earnings.append(client)
    if len(checking_earnings) == len(list_of_clients):
        return None
    else:
        sorted_clients = sorted(list_of_clients, key=lambda person: (-person.earnings_per_day(), person.account_age))
        return sorted_clients[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    checking_earnings = []
    for client in list_of_clients:
        earnings = client.current_amount - client.starting_amount
        if earnings < 0:
            checking_earnings.append(client)
    if not checking_earnings:
        return None
    else:
        sorted_clients = sorted(list_of_clients, key=lambda person: (person.earnings_per_day(), person.account_age))
        return sorted_clients[0]


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
