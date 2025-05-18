class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

# Getter method: Return the account number
    def get_accno(self):
        return self.account_number
# Getter method: Return the balance    
    def get_balance(self):
        return self.balance
# Getter method: Return the owner name
    def get_owner_name(self):
        return self.owner_name
# Setter method: Set the account number    
    def set_accno(self, newaccount_number):
        if isinstance(newaccount_number, int) and len(str(newaccount_number)) == 6:
            self.account_number = newaccount_number
        else:
            raise ValueError("Account number must be an integer and 6 characters in length.")
 # Setter method: Set the balance       
    def set_balance(self, new_balance):
        if isinstance(new_balance, int):
            self.balance = new_balance
        else:
            raise ValueError("Balance must be an integer")
# Setter method: Set the owner name         
    def set_owner_name(self, new_name):
        if isinstance(new_name, str):
            self.owner_name = new_name
        else:
            raise ValueError("Name must be a string")
# Function: Withdraw a subtracted balance        
    def withdraw(self, subtracted_balance):
        if isinstance(subtracted_balance, int):
            self.balance -= subtracted_balance
        else:
            raise ValueError("Subtracted balance must be an integer")
# Function: Deposit an added balance          
    def deposit(self, added_balance):
        if isinstance(added_balance, int):
            self.balance += added_balance
        else:
            raise ValueError("Added balance must be an integer")
# Function: Make a new account
def newaccount():
    accountnumber = int(input("Create an account number 6 characters in length all numbers: "))
    balance = int(input("Enter your current balance: "))
    ownername = str(input("Enter your owner name: "))

    if len(str(accountnumber)) != 6:
        raise ValueError("Account number must be 6 characters")
    
    return BankAccount(accountnumber, balance, ownername)
