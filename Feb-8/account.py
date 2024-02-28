from money import Money

class Account:
    def __init__(self, balance):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def __iadd__(self, money):
        if isinstance(money, Money):
            if money.currency != 'USD':
                raise TypeError("Только доллары!")
            self._balance += money.amount
            return self
        else:
            raise TypeError("Тип не поддерживается")
    
    def __repr__(self):
        return f"Account balance: {self.balance} USD"
