class Armor:
    """ Equipment that alters strength attr. """
    def __init__(self):
        pass
    
class LightArmor(Armor):
    """ Moderately increase defense and strength of target"""
    def __init__(self):
        self.add_defense = .10
        self.add_strength = .10

    def up_defense(self, target):
        """ Increase target armor by .10. """
        target._defense += round(self.add_defense * target._defense)
        print("{} defense increased to {}".format(target._name, target._defense))

    def up_strength(self, target):
        """ Increase target strength by .10. """
        target._strength += round(self.add_strength * target._strength)
        print("{} strength increased to {}".format(target._name, target._defense))

    
class HeavyArmor(Armor):
    """ Greatly incease defense and strength of target
    
    Target attribute buffs: up_defense and up_strength.
    """
    
    def __init__(self):
        self.add_defense = .25
        self.add_strength = .25
    
    def up_defense(self, target):
        """ Increase target armor by .25. """
        target._defense += round(self.add_defense * target._defense)
        print("{} defense increased to {}".format(target._name, target._defense))

    def up_strength(self, target):
        """ Increase target strength by .25. """
        target._strength += round(self.add_strength * target._strength)
        print("{} strength incresed to {}".format(target._name, target._strength))


class Cap(Hat):
    """ Moderately increase mind of target. """
    def __init__(self):
        self.add_mind = .10

    def up_mind(self, target):
        """ Increase target mind by .10. """
        target._mind += round(self.add_mind * target._mind)
        print("{} mind increased to {}".format(target._name, target._mind))

