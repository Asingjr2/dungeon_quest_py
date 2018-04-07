from base_entity import Entity


class PlayerCharacter(Entity):
    pass

class Warrior(Entity):
    
    def ability(self):
        increase = round(self._strength * 1.2)
        self._strength += increase 
        print("{} used special ability and strength increased to {}".format(self._name, self._strength))
        return self._strength


class Thief(Entity):

     def ability(self):
        increase = round(self._luck * 1.2)
        self._luck += increase 
        print("{} used special ability and luck increased to {}".format(self._name, self._luck))
        return self._luck
        
    # Not sure if worth implementing, but would be required to buy items or armor/equipment
    # def pick_pocket(self, target):
    #     if target.wallet.money > 0:
    #         stolen_money = round(target.wallet.money *= .1)
    #         target.wallet.money -= stolen_money
    #         self.wallet.money += stolen_money



