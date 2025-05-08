from bank_account import BankAccount

account = BankAccount(59092009, 10000000, "Ronen Gupta")
account2 = BankAccount(80520253, 2, "Victor Guo")

print("Welcome to Da Bank! Your current listed accounts are below. Press 1 to withdraw, press 2 to deposit, and press 3 to exit!")

print(f"Account 1 Name: {account.get_owner_name()}")
print(f"Account 1 Number: {account.get_accno()}")
print(f"Account 1 Balance: {account.get_balance()}")

print(f"Account 2 Name: {account2.get_owner_name()}")
print(f"Account 2 Number: {account2.get_accno()}")
print(f"Account 2 Balance: {account2.get_balance()}")

while True:
    choice = int(input("What would you like to do? (1, 2, 3) "))
    if choice == 1:
        subtracted_balance = input("How much would you like to withdraw? ")
        account.withdraw(subtracted_balance)
        print(f"Your new balance is: {account.get_balance()}")
    elif choice == 2:
        added_balance = input("How much would you like to deposit? ")
        account.deposit(added_balance)
        print(f"Your new balance is {account.get_balance()}")
    elif choice == 3:
        break


# account.set_owner_name("Victor Guo")
# account.set_accno(80520253)
# account.set_balance(2)

# account2.set_owner_name("Ronen Gupta")
# account2.set_accno(59092009)
# account2.set_balance(10000000)

# print(account.get_owner_name())
# print(account.get_accno())
# print(account.get_balance())

# print(account2.get_owner_name())
# print(account2.get_accno())
# print(account2.get_balance())


