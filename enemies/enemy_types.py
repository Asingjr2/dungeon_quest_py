"""Enemy types that extend base human class.

Current classes include Troll and Pyromancer classes.
"""
from base_enemy import Enemy


class Troll(Enemy):
    """Class that extends Enemy base with method to increase strength."""
    def __init__(self, name, hp, str_, def_, intel):
        super().__init__(name, hp, str_, def_, intel)
    
    def shriek(self):
        """Small boost to strenght stat."""
        increase = round(self.strength * .1)
        self.strength += increase
        print( "{} strength increased by {}".format(self._name, increase))
            

class Pyromancer(Enemy):
    """Class that extends Enemy base with method to increase intelligence."""
    def __init__(self, name, hp, str_, def_, intel):
        super().__init__(name, hp, str_, def_, intel)

    def focus(self):
        """Small boost to intellignce stat."""
        self.intelligence = round(self.intelligence * 1.1)
        print("{} intellignce increased to {}".format(self.name, self.intelligence))


j = Troll("goon", 100, 29, 6,7)
j.current_stats()
hey = Pyromancer("spiro", 300, 32, 5,80)
hey.focus()
hey.current_stats()


