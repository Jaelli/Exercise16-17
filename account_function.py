from account import Account

my_account = Account(1000.00)
my_account.deposit(550.23)
my_account.deposit(100)
my_account.withdraw(50)

print(my_account.getbalance())

another = Account(0)
another.deposit(10)

jade = Account(907253)
jade.deposit(50000)

print(another.getbalance())
print(jade.getbalance())
print(Account.numCreated)

print("object another is class", another.__class__.__name__)
print(jade.__class__.__name__)
print(jade)
print(another)
# Overriding operators
if jade > another:
    print(f"{jade} has more money than {another}!")
if another < my_account:
    print(f"{another} has less money than {my_account}!")

# Using a class method
print(Account.get_total_balance())
