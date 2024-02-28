class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def currency(self):
        return self._currency
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Добавить  деньги в другой валюте нельзя!")
            return Money(self.amount + other.amount, self.currency)
        else:
            raise TypeError("Не поддерживаемый тип!")
    
    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ValueError("Ошибка деления на ноль!")
            share = self.amount / divisor
            return [Money(share, self.currency) for _ in range(divisor)]
        else:
            raise TypeError("Не поддерживаемый тип!")

