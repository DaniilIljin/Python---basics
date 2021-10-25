"""EX08 Cakes making."""


class Factory:
    """Factory to make cakes."""

    def __init__(self):
        """Initiate a Factory class."""
        self.small_count = 0
        self.medium_count = 0
        self.large_count = 0

    def bake_cake(self, toppings: int, base: int) -> int:
        """Start baking."""
        count = 0
        if toppings == base >= 0:
            if toppings >= 5:
                large_cakes = toppings // 5
                count += large_cakes
                self.large_count += large_cakes
                toppings = toppings - large_cakes * 5
                if toppings >= 2:
                    medium_cakes = toppings // 2
                    count += medium_cakes
                    self.medium_count += medium_cakes
                    toppings = toppings - medium_cakes * 2
                    count += toppings
                    self.small_count += toppings
                else:
                    count += toppings
                    self.small_count += toppings
            elif toppings >= 2:
                medium_cakes = toppings // 2
                count += medium_cakes
                self.medium_count += medium_cakes
                toppings = toppings - medium_cakes * 2
                count += toppings
                self.small_count += toppings
            else:
                count += toppings
                self.small_count += toppings
        return count

    def get_last_cakes(self, n: int) -> list:
        """Get list of last cakes."""
        list_of_cakes = self.get_cakes_baked()
        index = -n
        if index != 0:
            cakes_in_the_end = list_of_cakes[index:]
            return cakes_in_the_end
        else:
            return []

    def get_cakes_baked(self) -> list:
        """list of baked cakes."""
        list_of_cakes = []
        for large in range(self.large_count):
            list_of_cakes.append(Cake(5, 5))
        for medium in range(self.medium_count):
            list_of_cakes.append(Cake(2, 2))
        for small in range(self.small_count):
            list_of_cakes.append(Cake(1, 1))
        return list_of_cakes

    def __str__(self):
        """How many factory made."""
        if len(Factory.get_cakes_baked(self)) == 1:
            return f"Factory with {len(Factory.get_cakes_baked(self))} cake."
        else:
            return f"Factory with {len(Factory.get_cakes_baked(self))} cakes."


class Cake:
    """My tasty cakes."""

    def __init__(self, base_amount, toppings_amount):
        """Right cakes."""
        if base_amount == toppings_amount and base_amount in (1, 2, 5):
            self.base_amount = base_amount
            self.toppings_amount = toppings_amount
        else:
            raise WrongIngredientsAmountException

    @property
    def type(self):
        """Define a type of specific cake."""
        if self.toppings_amount == self.base_amount == 1:
            return "basic"
        elif self.toppings_amount == self.base_amount == 2:
            return 'medium'
        elif self.toppings_amount == self.base_amount == 5:
            return 'large'

    def __repr__(self):
        """Define type of cake."""
        if self.toppings_amount == self.base_amount == 1:
            return "Cake(basic)"
        elif self.toppings_amount == self.base_amount == 2:
            return "Cake(medium)"
        elif self.toppings_amount == self.base_amount == 5:
            return "Cake(large)"

    def __eq__(self, other):
        """Compare cakes."""
        return self.toppings_amount, self.base_amount == other.toppings_amount, other.base_amount


class WrongIngredientsAmountException(Exception):
    """I do not know for what purpose it is."""


