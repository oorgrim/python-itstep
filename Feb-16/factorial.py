from functools import lru_cache

class FactorialCalculator:
    @lru_cache
    def found_factorial(self, n):
        if n < 0:
            raise ValueError("Введите положиьельное число!")

        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

factorial_calculator = FactorialCalculator()

test1 = factorial_calculator.found_factorial(3)
print(test1)

test2 = factorial_calculator.found_factorial(7)
print(test2)