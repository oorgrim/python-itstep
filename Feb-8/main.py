from money import Money
from account import Account

money1 = Money(270, "USD")
money2 = Money(70, "USD")
money3 = Money(10, "EUR")

print(money1)
print(money2)
print(money3)

try:
    print(money1 + money2)
    print(money1 + money3)

except ValueError:
    print(ValueError)

try:
    print(money1 / 5)
    print(money2 / 2)
    print(money3 / 3)
    print(money1 / 0)

except ValueError:
    print(ValueError)

except TypeError:
    print(TypeError)

account = Account(500)
print(account)

try:
    account += money1
    print(account)
    account += money3

except ValueError:
    print(ValueError)
    
except TypeError:
    print(TypeError)