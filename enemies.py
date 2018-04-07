from base_entity import Entity, Dragon


class Enemy(Entity):
    pass


class Troll(Entity):
    
    # Why will below not work with @property 
    def shriek(self):
        increase = round(self._strength * .1)
        self._strength += increase
        print( "{} strength increased by {}".format(self._name, increase))
            

class Mage(Entity):

    def focus(self):
        self._mind = round(self._mind * 1.1)

    def boost(self, target):
        increase = round(target._max_hp * .1)
        target._max_hp += increase
        print("{} max health increased by {} HP".format(target._name, increase))

class first_boss_dragon(Dragon):

    # is there a way to make dragon invicible to physical attacks?  Not sure how to sense other methods that impact this instance
    def fly(self):
        pass
