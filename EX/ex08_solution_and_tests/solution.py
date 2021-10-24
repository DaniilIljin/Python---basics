"""EX08 2nd."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    return 5 <= time <= 24 and (5 <= time <= 17 and coffee_needed or 18 <= time <= 24 and (not coffee_needed or coffee_needed))


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c and b != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount >= 0 and big_baskets >= 0 and small_baskets >= 0:
        if big_baskets * 5 >= ordered_amount:
            if ordered_amount % 5 == 0:
                return 0
            else:
                needed_to_be_filled = ordered_amount % 5
                only_big = ordered_amount // 5
                if 5 * only_big + small_baskets * needed_to_be_filled == ordered_amount:
                    return small_baskets
                else:
                    return -1
        elif big_baskets * 5 + small_baskets >= ordered_amount:
            do_not_needed = big_baskets * 5 + small_baskets - ordered_amount
            if big_baskets * 5 + small_baskets - do_not_needed == ordered_amount:
                return small_baskets - do_not_needed
            else:
                return -1
        else:
            return -1
    else:
        return -1
