# Class Client
class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel

    # Getters and setters for all attributes
    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel

    def set_tel(self, tel): self.__tel = tel

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")

# Class Account
class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner

    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # Credit and debit methods
    def credit(self, amount, account=None):
        if account is None:
            self.__balance += amount
        else:
            self.__balance += amount
            account.debit(amount)

    def debit(self, amount, account=None):
        if self.__balance >= amount:
            self.__balance -= amount
            if account is not None:
                account.credit(amount)
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)


