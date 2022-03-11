class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount:
            print(
                f'Your current balance: ${self.balance:,.2f} , the amount being withdrawn {amount:,.2f}, fund is not available. Charging a $5 fee.')
            self.balance -= 5
        else:
            self.balance -= amount
            print("Your withraw is completed!")
        return self
