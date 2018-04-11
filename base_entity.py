from abc import ABC 
import random

# Do not fully understand this yet and what impact will be
class InvalidStateError(Exception):
    pass


class Entity:
    def __init__(self, name, hp, mp, str_, def_, mag, mind, luck):
        self._name = name
        self._max_hp= hp
        self._current_hp = hp
        self._max_mp= mp
        self._current_mp= mp
        self._strength= str_
        self._defense = def_
        self._magic = mag
        self._mind = mind 
        self._luck = luck
        self._on_ground = "YES"
        self._inventory = {}
        self._level = {"Level":1, "Required EXP": 100, "Current EXP":0}

    @property
    def current_hp(self):
        return self._current_hp

    @property
    def strength(self):
        return self._strength

    @property 
    def defense(self):
        return self._defense

    @property
    def is_alive(self):
        print("hey {}".format(self._name))
        return self._current_hp > 0
    
    @property
    def on_ground(self):
        return self._on_ground

    @property
    def level(self):
        print("{} currently level is {}".format(self._name, self._level["Level"]))
        return str(self._level["Level"])

    @property
    def inventory(self):
        print("{} has {} item(s) in inventory".format(self._name, len(self._inventory)))
        return self._inventory

    def take_damage(self, damage):
        if damage < 0:
            raise InvalidStateError

        print("hp={}, damage={}".format(self._current_hp, damage))
        self._current_hp -= damage
        if self._current_hp < 0:
            self._current_hp = 0
    
    # Made target of attack a list so more than on thing can get attaked at once
    def physical_attack(self, targets):
        if not targets:
            raise InvalidStateError

        for target in targets:
            if target.is_alive:
                if target._on_ground == "NO":
                    print("{} cannot be hit with physical attacks".format(target._name))
                    return None
                damage = (self._strength - target._defense)
                rand_val = random.randint(0, 100)
                # cool way to implement luck concept
                if self._luck > rand_val:
                    damage *= 4

                target.take_damage(damage)

    
class AerialCreature:
    def __init__(self):
        pass

    def fly(self):
        self._on_ground = "NO"


class Dragon(AerialCreature):
    def __init__(self, name, hp, mp, str_, def_, mag):
        self._name = name
        self._max_hp= hp
        self._current_hp = hp
        self._max_mp= mp
        self._current_mp= mp
        self._strength= str_
        self._defense = def_
        self.on_ground = "YES"

        
    @property
    def is_alive(self):
        return self._current_hp > 0

    def take_damage(self, damage):
        if damage < 0:
            raise InvalidStateError

        print("hp={}, damage={}".format(self._current_hp, damage))
        self._current_hp -= damage
        if self._current_hp < 0:
            self._current_hp = 0
    
    # Made target of attack a list so more than on thing can get attaked at once
    def physical_attack(self, targets):
        if not targets:
            raise InvalidStateError

        for target in targets:
            if target.is_alive:
                damage = (self._strength - target._defense)
                rand_val = random.randint(0, 100)
                target.take_damage(damage)

    def final_fireball(self, targets):
        if not targets:
            raise InvalidStateError
        
        for target in targets:
            if target.is_alive:
                damage = target._current_hp - 1
                target.take_damage(damage)


