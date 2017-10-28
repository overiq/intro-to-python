class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print("Error: Not enough funds")
        else:
            print("Successfully withdrawn $", amount, sep="")
            self.balance -= amount

    def get_balance(self):
        return self.balance


my_account = BankAccount(5000)   # Create my bank account with $5000
print("Current Balance: $", my_account.get_balance(), sep="")

print("Withdrawing $10000 ...")
my_account.make_withdrawal(10000)

print("Lets try withdrawing $1000 ...")
my_account.make_withdrawal(1000)

print("Now Current Balance: $", my_account.get_balance(), sep="")

print("Depositing $2000 ...")
my_account.make_deposit(2000)
print("Now Current Balance: $", my_account.get_balance(), sep="")