#CLIENT CLASS
class Client:
    def __init__(self, CIN, firstName, lastName, tel=""):
        self.__CIN = CIN
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel

        # List of accounts owned by client (new)
        self.__accounts = []

    # Getters
    def getCIN(self):
        return self.__CIN

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getTel(self):
        return self.__tel

    # Setter
    def setTel(self, tel):
        self.__tel = tel

    # Add account to the client (new)
    def addAccount(self, account):
        self.__accounts.append(account)

    # List all client's accounts (new)
    def listAccounts(self):
        print(f"Accounts of {self.__firstName} {self.__lastName}:")
        for acc in self.__accounts:
            print(f"  - Account Code: {acc.getCode()} | Balance: {acc.getBalance()}")

    def display(self):
        print("Client Information:")
        print(f"- CIN: {self.__CIN}")
        print(f"- Name: {self.__firstName} {self.__lastName}")
        print(f"- Tel: {self.__tel}")

#ACCOUNT CLASS

class Account:
    __nb_accounts = 0

    def __init__(self, owner):
        self.__balance = 0
        Account.__nb_accounts += 1
        self.__code = Account.__nb_accounts
        self.__owner = owner

        # New: list of transactions
        self.__transactions = []

        # Register this account inside the owner object
        owner.addAccount(self)

    # Getters
    def getBalance(self):
        return self.__balance

    def getCode(self):
        return self.__code

    def getOwner(self):
        return self.__owner

    # Add transaction to history
    def __log(self, message):
        self.__transactions.append(message)

    # Credit money
    def credit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return

        self.__balance += amount
        self.__log(f"Credited: +{amount}")

    # Debit money
    def debit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        self.__log(f"Debited: -{amount}")

    # Transfer money: debit from self and credit other account
    def transfer(self, amount, otherAccount):
        if amount <= 0:
            print("Amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance for transfer.")
            return

        self.__balance -= amount
        otherAccount.__balance += amount

        self.__log(f"Transfer sent: -{amount} to Account {otherAccount.getCode()}")
        otherAccount.__log(f"Transfer received: +{amount} from Account {self.getCode()}")

    # Display account
    def display(self):
        print("Account Information:")
        print(f"- Code: {self.__code}")
        print(f"- Balance: {self.__balance}")
        print(f"- Owner: {self.__owner.getFirstName()} {self.__owner.getLastName()}")

    # Display total accounts
    @staticmethod
    def displayNbAccounts():
        print(f"Total accounts: {Account.__nb_accounts}")

    # NEW: display history
    def displayTransactions(self):
        print(f"Transaction History of Account {self.__code}:")
        if not self.__transactions:
            print("  No transactions yet.")
        else:
            for t in self.__transactions:
                print("  -", t)

#adding  inheritance
#SavingsAccount inherits from Account

class SavingsAccount(Account):
    def __init__(self, owner, interest_rate):
        super().__init__(owner) # Call the original constructor
        self.interest_rate = interest_rate

    #Add interest
    def add_interest(self):
        interest = self.getBalance() * self.interest_rate
        self.credit(interest)
        print(f"Interest added: {interest} DA")