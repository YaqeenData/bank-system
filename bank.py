class Transaction:
    def __init__(self, trans_type, amount, date, target=None):
        self.trans_type = trans_type
        self.__amount = amount
        self.date = date
        self.__target = target

class Account:
    def __init__(self, account_number, owner, email, phone_number, password, balance = 0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        self.__email = email
        self.__passwrod = password
        self.__phone_number = phone_number
        self.__transactions = []
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Your current balance is {self.__balance}")

    def withdraw(self, amount):
        if self.__balance == 0:
            print("There is no money in your account!")
        elif self.__balance < amount:
            print("There is no enough money in your account to withdraw the needed amount.")
        else:
            self.__balance -= amount
            print(f"You successfully withdrawed {amount} Saudi Riyal")

    def transfer(self, amount, target_account):
        if self.__balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)


    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance
    
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number
    
    def set_password(self, new_password):
        self.__passwrod = new_password
        print("Your new password is set.")
    

class AavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, interest_rate =0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.__balance += self.__balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit = 500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.__balance + self.overdraft_limit >= amount:
            self.__balance -= amount
        else:
            print("Overdraft limit exceeded.")

class Bank:
    def __init__(self, accounts):
        _accounts = dict()

    def add_account(self, owner, email, phone_number, password):
        self.__owner = owner
        self.__email = email
        self.__phone_number = phone_number
        self.__password = password
        new_account = Account(self.__owner, self.__email, self.__phone_number,self.__password)
    
    def remove_account(self, account_number, owner):
        pass

    def get_all_accounts(self):
        return self._accounts 
    
    def get_an_account(self, account_number):
        pass