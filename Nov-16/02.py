
user_data1 = input("Введите первое число: ")
user_data2 = input("Введите второе число: ")

num1, num2 = float(user_data1), float(user_data2)

sum = num1 + num2
difference1 = num1 - num2
difference2 = num2 - num1 
multiplication = num1 * num2
division1 = num1 / num2 
division2 = num2 / num1 

print(num1, "+", num2, "=", sum)
print(num1, "-", num2, "=", difference1)
print(num2, "-", num1, "=", difference2)
print(num1, "*", num2, "=", multiplication)
print(num1, "/", num2, "=", division1)
print(num2, "/", num1, "=", division2)