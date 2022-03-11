from users_with_BankAccounts import BankAccount


class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance:,.2f}")
        return self


bank1 = BankAccount(0.2, 0)
bank2 = BankAccount(0.5, 0)

user1 = User("Michael", "michaellay2689@gmail.com", bank1)
user2 = User("Nancy", "Nancy@gmail.com", bank2)

user1.make_deposit(100).make_deposit(100000).make_deposit(
    1000000).make_withdrawal(50000).display_user_balance()

user2.make_deposit(500).make_deposit(1000).make_withdrawal(
    100).make_withdrawal(200).display_user_balance()
