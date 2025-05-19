import random
WeaponsDictionary = {}
class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    def get_stats(self):
        print(f"Weapon name: {self.name}")
        print(f"Weapon category: {self.category}")
        print(f"Weapon damage: {self.damage}")

    def set_stats(self, newname, newcategory, newdamage):
        if isinstance(newname, str) and isinstance(newcategory, str) and isinstance(newdamage, int):
            self.name = newname
            self.category = newcategory
            self.damage = newdamage

class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        print(f"Weapon name: {self.name}")
        print(f"Weapon category: {self.category}")
        print(f"Weapon damage: {self.damage}")
        print(f"Weapon Damage Category: {self.damage_category}")
        print(f"Weapon crit damage: {self.damage * 3}")

    def set_stats(self, newname, newcategory, newdamage, newdamagecategory):
        if isinstance(newname, str) and isinstance(newcategory, str) and isinstance(newdamage, int) and isinstance(newdamagecategory, str):
            self.name = newname
            self.category = newcategory
            self.damage = newdamage
            self.damage_category = newdamagecategory

class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        print(f"Weapon name: {self.name}")
        print(f"Weapon category: {self.category}")
        print(f"Weapon damage: {self.damage}")
        print(f"Weapon Damage Category: {self.damage_category}")
        print(f"Weapon crit damage: {self.damage * 2}")

    def set_stats(self, newname, newcategory, newdamage, newdamagecategory):
        if isinstance(newname, str) and isinstance(newcategory, str) and isinstance(newdamage, int) and isinstance(newdamagecategory, str):
            self.name = newname
            self.category = newcategory
            self.damage = newdamage
            self.damage_category = newdamagecategory

class Longbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def get_stats(self):
        print(f"Weapon name: {self.name}")
        print(f"Weapon category: {self.category}")
        print(f"Weapon damage: {self.damage}")
        print(f"Weapon Damage Category: {self.damage_category}")
        print(f"Weapon crit damage: {self.damage * 2}")
        print(f"Bow range: {self.bow_range}")

    def set_stats(self, newname, newcategory, newdamage, newdamagecategory, newbowrange):
        if isinstance(newname, str) and isinstance(newcategory, str) and isinstance(newdamage, int) and isinstance(newdamagecategory, str) and isinstance(newbowrange, int):
            self.name = newname
            self.category = newcategory
            self.damage = newdamage
            self.damage_category = newdamagecategory
            self.bow_range = newbowrange

class Shortbow(Longbow):
    pass

def createweapon():
        namechoice = input("Welcome to weapon creation! Enter the name first: ")
        categorychoice = input("Great! What is your weapon type? (Sword or Bow): ")
        damagechoice = {random.randint(1, 1000)}
        print(f"Your weapons damage: {damagechoice}")
        damagecategorychoice = input(f"Choose your damage category choice: ")

        if categorychoice == "Bow":
            print(f"Created a bow with name {namechoice}, damage {damagechoice}, category {categorychoice}, and damage category {damagecategorychoice}! Saved to your weapons list!")
            WeaponsDictionary[namechoice] = (Bow(namechoice, categorychoice, damagechoice, damagecategorychoice))
    
        
        elif categorychoice == "Sword":
            print(f"Created a sword with name {namechoice}, damage {damagechoice}, category {categorychoice}, and damage category {damagecategorychoice}! Saved to your weapons list!")
            WeaponsDictionary[namechoice] = (Sword(namechoice, categorychoice, damagechoice, damagecategorychoice))

        elif categorychoice != "Sword" or "Bow":
            print("Cannot create this weapon!")
    