"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    """
    Check if the parameter number is a prime number.

    Conditions:
    1. If number is a prime number then return boolean True
    2. If number is not a prime number then return boolean False

    :param number: the number for check.
    :return: boolean True if number is a prime number or False if number is not a prime number.
    """
    if number != 1 and number != 0:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False
print(is_prime_number(169))
# if __name__ == '__main__':
#     print(is_prime_number(2))  # -> True
#     print(is_prime_number(89))  # -> True1
#     print(is_prime_number(23))  # -> True
#     print(is_prime_number(4))  # -> False
#     print(is_prime_number(7))  # -> True
#     print(is_prime_number(88))  # -> False
