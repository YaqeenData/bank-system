class Bank:
    def __init__(self, accounts):
        _accounts = dict()

    def add_account():
        pass
    
    def remove_account():
        pass

    def get_all_accounts():
        pass
    
    def get_an_account():
        pass
class Transaction:
    def __init__(self, trans_type, amount, date, target=None):
        self.trans_type = trans_type
        self.__amount = amount
        self.date = date
        self.__target = target

class Account:
    def __init__(self, account_number, owner, balance = 0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []
    
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount, target_account):
        pass

    def get_balance(self):
        pass

    def set_balance(self, balance):
        pass
    
    def get_owner(self):
        pass

    def set_owner(self, owner):
        pass

    def get_account_number(self):
        pass

class AavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, interest_rate =0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        pass

class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit = 500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        pass