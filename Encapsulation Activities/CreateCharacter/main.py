from create_character import CreateCharacter

player1 = CreateCharacter("Berserker", "Heavy", 50, 20, 7, 15, 4, 4)
player2 = CreateCharacter("Coder", "Techy", 50, 5, 5, 7, 20, 13)

print(f"Player 1 Name: {player1.get_name()}")
print(f"Player 1 Classtype: {player1.get_classtype()}")
print(f"Player 1 Level: {player1.get_level()}")

print(f"Player 2 Name: {player2.get_name()}")
print(f"Player 2 Classtype: {player2.get_classtype()}")
print(f"Player 2 Level: {player2.get_level()}")

player1.set_name("Slicer")
print(f"New Player 1 Name: {player1.get_name()}")

player1.set_classtype("Stealth")
print(f"New Player 1 Classtype: {player1.get_classtype()}")

player1.set_level(51)
print(f"New Player 1 Level: {player1.get_level()}")

player2.set_name("Knight")
print(f"New Player 2 Name: {player2.get_name()}")

player2.set_classtype("Swordsman")
print(f"New Player 2 Classtype: {player2.get_classtype()}")

player2.set_level(51)
print(f"New Player 2 Level: {player2.get_level()}")

player1.upgrade_stats()
