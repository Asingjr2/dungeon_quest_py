"""Module contains base type for enemies user will face."""


class Enemy(object):
    """Base class of enemy that will attack heroes.
    
    Attributes include name, health, strength, defense, and intelligence.
    Methods include checks for living, being on the ground, and description
    of all character stats.
    """

    def __init__(self, name, hp, mp, str_, def_, intel=0):
        self.name = name
        self._health = hp
        self.magic = mp
        self.strength = str_
        self.defense = def_
        self.intelligence = intel

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

    def current_stats(self):
        """Returns description of all enemy stats."""
        return print("Name = {}, Health = {}, Magic = {}, Strength = {}, Defense = {}, Intelligence = {}".format(self.name, self._health, self.magic, self.strength, self.defense, self.intelligence))
