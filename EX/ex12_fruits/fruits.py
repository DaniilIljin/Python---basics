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
        return ''.join([f'{fruit}: {self.products[fruit]}, ' if fruit != self.products.keys()[-1]
                        else f'{fruit}: {self.products[fruit]}' for fruit in self.products.keys()])

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
                    if element:
                        new_list.append(element)
                new_order = Order()
                new_order.add_products(new_list)
                self.list_of_orders += [new_order]
            else:
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
                    new_order.add_products(products_and_their_mass)
                else:
                    new_order.add_product(products_and_their_mass)
                customer.add_new_order(new_order)

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.list_of_customers += [customer]

    def add_customers(self, customers):
        """Method for adding several customers to the list."""
        self.list_of_customers.extend(customers)

    def show_all_orders(self) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        pass

    def calculate_total(self) -> float:
        """Method for calculating total price for all customer's orders."""
        pass

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        pass


class Customer:
    """Customer to implement."""

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
        self.list_of_orders += order

    def __repr__(self):
        """."""
        return self.name


if __name__ == '__main__':
    app = App()
    # # Adding default customers to our app.
    # app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
    #                    Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])
    # # Ordering some food for everyone.
    # app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    # app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    # app.order("Rubber Duck", [("Mango Irwin", 6)])
    # app.order("Svetozar", [("Lemon", 1)])
    # app.order("Svetozar", [("Grapefruit", 10)])
    # app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    # app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])
    # # Checking products dictionary format (we want numeric price, not string).
    # print(app.get_products())
    # print("=======")
    # # Checking how all orders and summary look like.
    # print(app.show_all_orders(False))
    # print("=======")
    # print(app.show_all_orders(True))
    # print("=======")
    # app.calculate_summary()
    print([f'{product.name} and its price {product.price}' for product in app.list_of_products_and_prices])
