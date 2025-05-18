from bank_account import BankAccount, newaccount

# Class Instances
account = BankAccount(59092009, 10000000, "Ronen Gupta")
account2 = BankAccount(80520253, 2, "Victor Guo")

# Introduction
print("Welcome to Da Bank! Press 1 to withdraw, press 2 to deposit, press 3 to create a new account, and press 4 to exit!")
print(f"Account 1 Name: {account.get_owner_name()}")
print(f"Account 1 Number: {account.get_accno()}")
print(f"Account 1 Balance: {account.get_balance()}")

# Initialise Class Deposit and Withdraw Functions, as well as creating a new account
while True:
    choice = int(input("What would you like to do? (1, 2, 3) "))
    if choice == 1:
        subtracted_balance = int(input("How much would you like to withdraw? "))
        account.withdraw(subtracted_balance)
        print(f"Your new balance is: {account.get_balance()}")
    elif choice == 2:
        added_balance = int(input("How much would you like to deposit? "))
        account.deposit(added_balance)
        print(f"Your new balance is {account.get_balance()}")
    elif choice == 3:
        new_account = newaccount()
        print(f"Account created for {new_account.get_owner_name()}!")
    elif choice == 4:
        break

# Testing Class Methods (Also 6 character length for account number)
    # account.set_owner_name("Victor Guo")
    #account.set_accno(805223)
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


