from base_entity import Entity
from heroes import PlayerCharacter, Warrior
from enemies import Enemy, Troll, Mage


player = PlayerCharacter("Mighty Joe",100,50,10,10,10,10,10)
enemy = Enemy("Gooloff", 50,20,9,9,9,9,9)

player.physical_attack([enemy])
print(enemy._current_hp)

mini_troll = Troll("Jerk",47,0,8,8,8,8,8)
mini_troll.shriek()
print(mini_troll._strength)
print(mini_troll._name)
print(mini_troll._max_hp)
print(mini_troll._current_hp)

mage1  = Mage("Evelyn", 80,45, 6,6,12,11,6)
print(mage1._name)
mage1.focus()
print("mage mind is now {}".format(mage1._mind))
mage1.boost(mini_troll)
print(mini_troll._max_hp)

conan = Warrior("Conan", 100,50,10,10,10,10,10)
print(conan.ability())