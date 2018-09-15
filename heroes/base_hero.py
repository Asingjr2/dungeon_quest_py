"""Module contains base type for heroes used by player."""


class Human(object):
    """Base class for human-like heroes.
    
    Attributes include name, health, magic, strength, defense, intelligence, and luck.
    Methods include checks for living, being on the ground, and description
    of character stats.
    """
    def __init__(self, name, hp, mp, str_, def_, intel=0, luck=0):
        self.name = name
        self._health = hp
        self.magic = mp
        self.strength = str_
        self.defense = def_
        self.intelligence = intel
        self.luck = luck
        self.current_health = hp
        self.max_health = hp
        self.on_ground = True
        self.alive = True

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        """Attribute setting with validation using python getter and setter."""
        if health <=0:
            raise ValueError("Health cannot be less than 0")
        self._health = health

    @property
    def current_hp(self):
        return self.current_health

    def is_alive(self):
        """Checks to see if character's current health is above 0."""
        if self.current_health > 0:
            return True
        else:
            self.is_alive = False
            return self.is_alive
    
    def is_on_ground(self):
        """Checks to see if character on_ground attribute is true."""
        return self.on_ground

    def current_stats(self):
        """Returns description of all character stats."""
        return print("Name = {}, Health = {}, Magic = {}, Strength = {}, Defense = {}, Intelligence = {}, Luck = {}".format(self.name, self._health, self.magic, self.strength, self.defense, self.intelligence, self.luck))

