class Armor:
    """ Equipment that alters strength attr. """
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
class LightArmor(Armor):
    """ Moderately increase defense and strength of target"""
    def __init__(self, name, category):
        super().__init__(name, category)
        self.add_defense = .10
        self.add_strength = .10

    def raise_defense(self, target):
        """ Increase target armor by .10. """
        target.defense += round(self.add_defense * target._defense)
        print("{} defense increased to {}".format(target.name, target.defense))

    def raise_strength(self, target):
        """ Increase target strength by .10. """
        target.strength += round(self.add_strength * target.strength)
        print("{} strength increased to {}".format(target.name, target.strength))

    
class HeavyArmor(Armor):
    """ Greatly incease defense and strength of target
    
    Target attribute buffs: up_defense and up_strength.
    """
    def __init__(self, name, category):
        super().__init__(name, category)
        self.add_defense = .25
        self.add_strength = .25
    
    def raise_defense(self, target):
        """ Increase target armor by .25. """
        target._defense += round(self.add_defense * target.defense)
        print("{} defense increased to {}".format(target.name, target.defense))

    def raise_strength(self, target):
        """ Increase target strength by .25. """
        target._strength += round(self.add_strength * target.strength)
        print("{} strength incresed to {}".format(target.name, target.strength))


class Cap(Hat):
    """ Moderately increase mind of target. """
    def __init__(self, name, category):
        super().__init__(name, category)
        self.add_intel = .10

    def raise_intelligence(self, target):
        """ Increase target mind by .10. """
        target.intelligence += round(self.add_intel * target.intelligence)
        print("{} mind increased to {}".format(target.name, target.intelligence))

