"""Fruits delivery application."""
import re


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price

    def get_name(self):
        """."""
        return self.name

    def get_price(self):
        """."""
        return self.price


class Order:
    """Order class."""

    def __init__(self, customer='Someone'):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.customer = customer
        self.products = {}

    def get_products(self):
        """."""
        return self.products

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        return ''.join([f'{fruit}: {self.products[fruit]} kg, ' for fruit in self.products.keys()])[:-2]

    def get_customer(self):
        """."""
        return self.customer

    def add_product(self, product):
        """Method for adding a single product to the dictionary."""
        if product[0] in self.products:
            self.products[product[0]] += product[1]
        else:
            self.products[product[0]] = product[1]

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for product in products:
            self.add_product(product)


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.list_of_customers = []
        self.list_of_products_and_prices = self.import_products('pricelist.txt')
        self.list_of_orders = []

    def get_list_of_customers(self):
        """."""
        return self.list_of_customers

    def get_products(self) -> list:
        """Getter for products list."""
        if self.list_of_products_and_prices:
            return self.list_of_products_and_prices

    def get_orders(self) -> list:
        """Getter for orders list."""
        return self.list_of_orders

    def get_customers(self):
        """."""
        return self.list_of_customers

    def import_products(self, filename) -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        with open(filename, 'r') as file_content:
            content = file_content.read()
        matches = re.findall(r'.+[^\n]', content)
        return [Product(match.split(' - ')[0], float(match.split(' - ')[1])) for match in matches]

    def find_product_by_name(self, product):
        """."""
        if product:
            for product_ in self.list_of_products_and_prices:
                if product_.get_name() == product:
                    return product_

    def order_products(self, something_to_order):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        """
        if something_to_order:
            if type(something_to_order) is list:
                new_list = []
                for element in something_to_order:
                    if element[0] not in [product_.get_name() for product_ in self.get_products()]:
                        raise Exception("Woopsie. There is no such product as ")
                    if element:
                        new_list.append(element)
                new_order = Order()
                new_order.add_products(new_list)
                self.list_of_orders += [new_order]
            else:
                if something_to_order[0] not in [product_.get_name() for product_ in self.get_products()]:
                    raise Exception("Woopsie. There is no such product as ")
                new_order = Order()
                new_order.add_product(something_to_order)
                self.list_of_orders += [new_order]

    def order(self, customers_name, products_and_their_mass):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        for customer in self.list_of_customers:
            if customer.name == customers_name:
                new_order = Order(customer)
                if type(products_and_their_mass) is list:
                    for element in products_and_their_mass:
                        if element[0] not in [product_.get_name() for product_ in self.get_products()]:
                            raise Exception("Woopsie. There is no such product as ")
                    new_order.add_products(products_and_their_mass)
                else:
                    if products_and_their_mass[0] not in [product_.get_name() for product_ in self.get_products()]:
                        raise Exception("Woopsie. There is no such product as ")
                    new_order.add_product(products_and_their_mass)
                customer.add_new_order(new_order)

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.list_of_customers += [customer]

    def add_customers(self, customers):
        """Method for adding several customers to the list."""
        self.list_of_customers.extend(customers)

    def second_way(self):
        """."""
        string = ''
        total_total = 0
        for customer in self.list_of_customers:
            if self.calculate_total(customer) != 'nothing':
                total_total += self.calculate_total(customer)
        for costomer in self.list_of_customers:
            string += f'{costomer.get_name()}:\n'
            if costomer.get_orders():
                a = costomer.get_orders()
                counter = 0
                for order in a:
                    if not order.get_products():
                        counter += 1
                if counter == len(a):
                    string += 'nothing\n\n'
                else:
                    for order in a:
                        if order:
                            string += order.get_products_string() + '\n'
                        else:
                            continue
                    string += '\n'
            else:
                string += 'nothing\n\n'
        return string[:-2]

    def first_way(self):
        """."""
        string = ''
        total_total = 0
        for customer in self.list_of_customers:
            if self.calculate_total(customer) != 'nothing':
                total_total += self.calculate_total(customer)
        for costomer in self.list_of_customers:
            string += f'{costomer.get_name()}:\n'
            if costomer.get_orders():
                a = costomer.get_orders()
                counter = 0
                for order in a:
                    if not order.get_products():
                        counter += 1
                if counter == len(a):
                    string += 'nothing\n'
                    string += 'Total: 0.00\n\n'
                else:
                    for order in a:
                        if order:
                            string += order.get_products_string() + '\n'
                        else:
                            continue
                    b = format(round(self.calculate_total(costomer), 2), '.2f')
                    string += f'Total: {b}\n\n'
            else:
                string += 'nothing\n'
                string += 'Total: 0.00\n\n'
        return string[:-2]

    def show_all_orders(self, is_summary) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        if is_summary:
            return self.first_way()
        else:
            return self.second_way()

    def calculate_total(self, customer) -> float:
        """Method for calculating total price for all customer's orders."""
        total = 0.0
        if customer.get_orders():
            for order in customer.get_orders():
                dic = order.get_products()
                for product in dic.keys():
                    for product_ in self.get_products():
                        if product_.get_name() == product:
                            total += dic[product] * product_.get_price()
                            break
        else:
            total = 'nothing'
        return total

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        string = ''
        total_total = 0
        for customer in self.list_of_customers:
            if self.calculate_total(customer) != 'nothing':
                total_total += self.calculate_total(customer)
        for costomer in self.list_of_customers:
            string += f'{costomer.get_name()}:\n'
            if costomer.get_orders():
                a = costomer.get_orders()
                counter = 0
                for order in a:
                    if not order.get_products():
                        counter += 1
                if counter == len(a):
                    string += 'nothing\n'
                    string += 'Total: 0.00\n\n'
                else:
                    for order in a:
                        if order:
                            string += order.get_products_string() + '\n'
                        else:
                            continue
                    b = format(round(self.calculate_total(costomer), 2), '.2f')
                    string += f'Total: {b}\n\n'
            else:
                string += 'nothing\n'
                string += 'Total: 0.00\n\n'
        string = string[:-1] + f'ALL ORDERS TOTAL: {round(total_total, 2)}'
        return string


class Customer:
    """Customer to  implement."""

    def __init__(self, name, address):
        """Create a customer."""
        self.name = name
        self.address = address
        self.list_of_orders = []

    def get_name(self):
        """."""
        return self.name

    def get_address(self):
        """."""
        return self.address

    def get_orders(self):
        """."""
        return self.list_of_orders

    def add_new_order(self, order):
        """."""
        self.list_of_orders += [order]

    def __repr__(self):
        """."""
        return self.name


if __name__ == '__main__':
    app = App()
    # Adding default customers to our app.
    app.add_customers([Customer("name1", "home"), Customer("name1", "home-table"), Customer("name12", "Dorm 1"),
                       Customer("orderer1", "Dorm 2"), Customer("orderer2", "Muhha's lair")])
    # Ordering some food for everyone.
    app.order("name1", [])
    app.order("name1", [])
    app.order("name12", [])
    app.order("orderer1", [("Avocado", 2), ("Orange", 3)])
    app.order("orderer1", [])
    app.order("orderer1", [("Grenades", 5), ("Lychees", 123)])
    app.order("orderer2", [("Grenades", 5), ("Lychees", 123), ("Green pepper", 3)])
    # Checking products dictionary format (we want numeric price, not string).
    print("=======")
    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    app.calculate_summary()
