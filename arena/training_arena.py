from base_entity import Entity, Dragon
from heroes import PlayerCharacter, Warrior
from enemies import Enemy, Troll, Mage
from equipment import LightArmor, HeavyArmor, Cap


player = PlayerCharacter("Mighty Joe",100,50,10,10,10,10,10)
enemy = Enemy("Gooloff", 50,20,9,9,9,9,9)

player.physical_attack([enemy])
print(enemy._current_hp)

mini_troll = Troll("Jerk",47,0,8,8,8,8,8)
mini_troll.shriek()
print(" Name = {} Strength = {}, Max HP = {}".format(mini_troll._name, mini_troll._strength, mini_troll._max_hp))

mage1 = Mage("Evelyn", 80,45, 6,6,12,11,6)
mage1.focus()
mage1.boost(mini_troll)

conan = Warrior("Conan", 100,50,10,10,10,10,10)
print("{}'s Current Strength = {}, Defense = {}, Mind = {}".format(conan._name, conan._strength, conan._defense, conan._mind))
(conan.ability())

#Testing Armor and Cap Functions
knights_armor = HeavyArmor()
knights_armor.up_defense(conan)
knights_armor.up_strength(conan)
guards_armor = LightArmor()
guards_armor.up_defense(player)
guards_armor.up_strength(player)
blue_hat = Cap()
blue_hat.up_mind(conan)

print("{}'s Buffed Strength = {}, Defense = {}, Mind = {}".format(conan._name, conan._strength, conan._defense, conan._mind))  

baby_dragon = Dragon("baby_dragon", 200,30,15,15,15)
baby_dragon.fly()
conan.physical_attack([baby_dragon])
conan.level
conan.inventory
conan.on_ground 