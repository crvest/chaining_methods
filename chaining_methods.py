class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    
    def transfer_money(self, other, amount):
        self.make_withdrawl(amount)
        other.make_withdrawl(amount)
        return self

# create 3 users
tom = User("Tom", "tom@tom.tom")
bill = User("Bill", "bill@bill.bill")
spiderman = User("Peter", "p.parker@friend.ly")

#  tom makes 3 deposits, 1 withdrawl, and displays balance
tom.make_deposit(300).make_deposit(100).make_deposit(100).make_withdrawl(250).display_user_balance()

print("----------------")

# bill makes 2 deposits and 2 withdrawls and displays balance
bill.make_deposit(50).make_deposit(50).make_withdrawl(25).make_withdrawl(75).display_user_balance()

print("----------------")

# spiderman makes 1 deposit and 3 withdrawls and displays balance
spiderman.make_deposit(1000).make_withdrawl(400).make_withdrawl(200).make_withdrawl(50).display_user_balance()

print("----------------")

# bonus: tom transfers money to spiderman, prints both balances
tom.transfer_money(spiderman, 100)
tom.display_user_balance()
spiderman.display_user_balance()