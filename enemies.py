from base_entity import Entity, Dragon


class Enemy(Entity):
    pass


class Troll(Entity):
    """ Low level enemy type."""
    
    # Why will below not work with @property 
    def shriek(self):
        increase = round(self._strength * .1)
        self._strength += increase
        print( "{} strength increased by {}".format(self._name, increase))
            

class Mage(Entity):

    def focus(self):
        self._mind = round(self._mind * 1.1)
        print("{} mind increased to {}".format(self._name, self._mind))

    def boost(self, target):
        increase = round(target._max_hp * .3)
        target._max_hp += increase
        print("{} max health increased by {} HP".format(target._name, increase))

