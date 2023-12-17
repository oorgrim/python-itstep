
user_data1 = input("Введите цену покупки: ")
user_data2 = input("Введите скидку: ") 
try:
    purchase_price = float(user_data1)
    discount_percentage = float(user_data2)

except ValueError:
    print('Введите корректные данные!')

else:
    discount_amount = (discount_percentage / 100) * purchase_price
    total = purchase_price - discount_amount

    print("Стоимость покупки: $%.2f" % purchase_price)
    print("Размер скидки: %.2f%%" % discount_percentage)
    print("Сумма к оплате после скидки: $%.2f" % total)