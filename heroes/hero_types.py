"""Hero types that extend base human class.

Current classes include Warrior, Wizard, and Theif classes.
"""
from base_hero import Human


class Warrior(Human):
    """Warrior class that extends Humna base with method to increase strength."""
    def __init__(self, name, hp, mp, str_, def_, intel, luck):
        super().__init__(name, hp, mp, str_, def_, intel, luck)

    def raise_strength(self):
        """Small boost to strength stat."""
        increase = round(self.strength * 1.2)
        self.strength += increase 
        print("{} used special ability and strength increased to {}".format(self.name, self.strength))
        return self.strength


class Wizard(Human):
    """Class that extends Human base with method to increase strength."""
    def __init__(self, name, hp, mp, str_, def_, intel, luck):
        super().__init__(name, hp, mp, str_, def_, intel, luck)

    def raise_intel(self):
        """Small boost to intellignce stat."""
        increase = round(self.intelligence * 1.2)
        self.intelligence += increase 
        print("{} used special ability and intelligence increased to {}".format(self.name, self.intelligence))
        return self.intelligence


class Thief(Human):
    """Class class that extends Human base with method to increase strength."""
    def __init__(self, name, hp, mp, str_, def_, intel, luck):
        super().__init__(name, hp, mp, str_, def_, intel, luck)

    def raise_luck(self):
        """Small boost to luck stat."""
        increase = round(self.luck * 1.2)
        self.luck += increase 
        print("{} used special ability and luck increased to {}".format(self.name, self.luck))
        return self.luck
        