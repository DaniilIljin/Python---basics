"""EX15 Santas workshop."""
import csv
import urllib.request
import urllib.parse
import json


class Santas_factory:
    """This is Santa`s factory."""

    def __init__(self, wish_list_csv_file, nice_list_csv_file, naughty_list_csv_file):
        """
        At factory initialisation factory receives a wish_list, a nice_list and a naughty_list.

        Also factory creates a list 'self.children', where in the future it will hold info about children,
         and a list 'self.presents', where it will hold presents, which have to be made.
        """
        self.nice_list = self.recieve_info_from_file(nice_list_csv_file)
        self.naughty_list = self.recieve_info_from_file(naughty_list_csv_file)
        self.wish_list = self.recieve_info_from_file(wish_list_csv_file)
        self.children = []
        self.presents = []

    def recieve_info_from_file(self, filename):
        """To receive info from file."""
        if filename:
            new_list = []
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    new_list.append(row)
                if new_list:
                    return new_list

    def create_children(self, list_of_children, status):
        """To create child(info about him)."""
        if list_of_children:
            for child in list_of_children:
                wishes = self.find_childs_wishes_by_name(child[0])
                new_child = Child(child[0], child[1], wishes, status)
                if new_child:
                    self.children.append(new_child)

    def find_childs_wishes_by_name(self, name):
        """
        To create child finder to connect child with his wishes.

         I decided, that every child may have max 3 presents,
        and function takes 3 first of wishes or less.
        """
        for childs_wishes in self.wish_list:
            if childs_wishes[0] == name:
                if len(childs_wishes) > 1:
                    wishes = [wish[1:] for wish in childs_wishes[1:]]
                else:
                    wishes = None
                if len(wishes) <= 3 or not wishes:
                    return wishes
                else:
                    return wishes[:4]

    def create_presents(self):
        """
        To create presents in the warehouse.

        Nice child receive all 3 presents, but naughty one only one. :( .
        """
        for child in self.children:
            if child.status == "nice":
                if child.wishes:
                    for present in child.wishes:
                        self.creating_presents_info(present)
            elif child.status == "naughty":
                if child.wishes:
                    self.creating_presents_info(child.wishes[0])

    def creating_presents_info(self, present_name):
        """To receive info about present."""
        if present_name:
            if present_name in [present.name for present in self.presents]:
                pass
            else:
                encoded_present = urllib.parse.urlencode({"name": present_name})
                response = urllib.request.urlopen("http://api.game-scheduler.com:8089/gift?" + encoded_present)
                final_dict = json.loads(response.read())
                new_present = Present(final_dict["gift"], final_dict['material_cost'],
                                      final_dict['production_time'],
                                      final_dict['weight_in_grams'])
                self.presents += [new_present]


class Child:
    """A child from lists."""

    def __init__(self, name, country, wishes, status):
        """Object to store some info about child."""
        self.name = name
        self.wishes = wishes
        self.status = status
        self.country = country
        self.warning = None


class Present:
    """Present."""

    def __init__(self, name, material_cost, production_time, weight_in_grams):
        """Object to store some info about present."""
        self.name = name
        self.cost = material_cost
        self.time = production_time
        self.weight = weight_in_grams
