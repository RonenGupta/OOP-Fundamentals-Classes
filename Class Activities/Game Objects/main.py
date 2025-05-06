from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
characters = []
weapons = []
CurrentCharacter = ''
CurrentWeapon = ''
# Create an instance of Player
player_character1 = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)
characters.append(player_character1.name)

player_character2 = Player('Victor', 'Guo', 'Computer Nerd', 1, 5432780537205732985743205235732805743820574380275483025743025749023578432057438025743820532704532050)
characters.append(player_character2.name)

player_character3 = Player('Levin', 'Shao', 'Egg', 0, 29137239139321723857129856478218943287472972653428064738025784923563295462354792356492356423785623795423795437564789235647892356425439)
characters.append(player_character3)

player_character4 = Player('Ronen', 'Gupta', 'idk', 3413431483194813948104, 1804314713947147310497318947139)
characters.append(player_character4)

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapon_sword1 = Weapon('Dragonslayer', 'Melee', random.randint(12, 15))
weapons.append(weapon_sword1)

weapon_sword2 = Weapon('Dog Sword', 'Melee', random.randint(10, 12))
weapons.append(weapon_sword2)

weapon_sword3 = Weapon('Victor Gun', 'Ranged Auto', random.randint(1, 3))
weapons.append(weapon_sword3)

weapon_sword4 = Weapon('Levin Shaotty', 'Ranged Nuker', random.randint(20, 50))
weapons.append(weapon_sword4)

def ChooseCharWeapon():
    print("Welcome to the game!")

    while True:
        try:
            ChosenCharacter = int(input("Choose your character (1-4) "))
            if ChosenCharacter in [1, 2, 3, 4]:
                break
            else:
                print("Please choose between 1 and 4.")
        except ValueError:
             print("Please choose between 1 and 4.")
    if ChosenCharacter == 1:
            CurrentCharacter = player_character1.name
            print(CurrentCharacter)
    elif ChosenCharacter == 2:
            CurrentCharacter = player_character2.name
            print(CurrentCharacter)
    elif ChosenCharacter == 3:
            CurrentCharacter = player_character3.name
    elif ChosenCharacter == 4:
            CurrentCharacter = player_character4.name
    
    print(f"Your chosen character is {CurrentCharacter}")

    while True:
        try:
             ChosenWeapon = int(input("Choose your weapon (1-4) "))
             if ChosenWeapon in [1, 2, 3, 4]:
                break
             else:
                print("Please choose between 1 and 4.")
        except ValueError:
            print("Please choose between 1 and 4.")
    if ChosenWeapon == 1:
        CurrentWeapon = weapon_sword1.wpnname
    elif ChosenWeapon == 2:
        CurrentWeapon = weapon_sword2.wpnname
    elif ChosenWeapon == 3:
        CurrentWeapon = weapon_sword3.wpnname
    elif ChosenWeapon == 4:
        CurrentWeapon = weapon_sword4.wpnname

    print(f"Your chosen weapon is {CurrentWeapon}")

ChooseCharWeapon()
    
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy_character = Enemy('Mr Scott', 'Programmer', random.randint(15,18), random.randint(80, 140))

# Print the player character details
print(f"Player Name: {player_character1.name}")
print(f"Player Race: {player_character1.race}")
print(f"Player Class: {player_character1.cls}")
print(f"Player Attack: {player_character1.atk}")
print(f"Player Health: {player_character1.health}")

#TODO: Print the player weapon details
print(f"Weapon Name: {weapon_sword1.wpnname}")
print(f"Weapon Category: {weapon_sword1.category}")
print(f"Weapon Damage: {weapon_sword1.damage}")

#TODO: Print the enemy character details
print(f"Enemy Name: {enemy_character.enmname}")
print(f"Enemy Race: {enemy_character.enmrace}")
print(f"Enemy Damage: {enemy_character.enmdamage}")
print(f"Enemy Health: {enemy_character.enmhealth}")

