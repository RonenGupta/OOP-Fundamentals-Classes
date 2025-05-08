class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def get_accno(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def get_owner_name(self):
        return self.owner_name
    
    def set_accno(self, newaccount_number):
        if isinstance(newaccount_number, int):
            self.account_number = newaccount_number
        else:
            raise ValueError("Account number must be an integer.")
        
    def set_balance(self, new_balance):
        if isinstance(new_balance, int):
            self.balance = new_balance
        else:
            raise ValueError("Balance must be an integer")
        
    def set_owner_name(self, new_name):
        if isinstance(new_name, str):
            self.owner_name = new_name
        else:
            raise ValueError("Name must be a string")
        
    def withdraw(self, subtracted_balance):
        if isinstance(subtracted_balance, int):
            self.balance -= subtracted_balance
          
    def deposit(self, added_balance):
        if isinstance(added_balance, int):
            self.balance += added_balance
          