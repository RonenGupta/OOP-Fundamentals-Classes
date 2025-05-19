from Animal import *
from Weapons import *
from Weapons import WeaponsDictionary



Dog = Dog("Dog", "Woof")
Dog.get_sound()

Cat = Cat("Cat", "Meow")
Cat.get_sound()


Sword = Sword("Sebastian Slayer", "Sword", 10, "Slashing")
Sword.get_stats()

Bow = Bow("Short Levin", "Bow", 30, "Piercing")
Bow.get_stats()

Longbow = Longbow("Long Levin", "Longbow", 50, "Bleeding", 750)
Longbow.get_stats()

Shortbow = Shortbow("Even Shorter Levin", "Shortbow", 20, "Bludgeoning", 80)
Shortbow.get_stats()



createweapon()

print(WeaponsDictionary)
