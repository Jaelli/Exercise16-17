from account import Account, InsufficientFundsException

my_account = Account(1000.00)
print("Current balance of my_account is: £" + str(my_account.getbalance()))
my_account.deposit(550.23)
my_account.deposit(100)
my_account.withdraw(50)

print("New balance of my_account is: £" + str(my_account.getbalance()))

another = Account(0)
another.deposit(10)

jade = Account(907253)
jade.deposit(50000)

print("Balance of another account is: £" + str(another.getbalance()))
print("Balance of Jade's account is: £" + str(jade.getbalance()))
print("The number of accounts currently in use is: " + str(Account.numCreated))

print("Account 'another' is class type: " + another.__class__.__name__)
print("Account 'jade' is class type: " + jade.__class__.__name__)
print("Jade: " + str(jade))
print("Another: " + str(another))

# Overriding operators
#if jade > another:
#    print(f"{jade} has more money than {another}!")
#if another < my_account:
#    print(f"{another} has less money than {my_account}!")

try:
    print("Current balance is: £" + jade.getbalance())
    jade.withdraw(150000000)
except InsufficientFundsException as e:
    print(e)
finally:
    print(jade)

# Using a class method
print(Account.get_total_balance())
