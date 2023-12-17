user_data = input("Введите сумму покупки: ")
try:
    purchase_amount = float(user_data)
except ValueError:
    print("Введите число!!!" )
else:
    if 200 <= purchase_amount < 300:
        discount = 0.03
        discounted_amount = purchase_amount * (1 - discount)
        print(f"Сумма к олпате со скидкой 3%:", discounted_amount)

    elif 300 <= purchase_amount < 500:
        discount = 0.05
        discounted_amount = purchase_amount * (1 - discount)
        print(f"Сумма к олпате со скидкой 5%: {discounted_amount:.2f}")

    elif purchase_amount >= 500:
        discount = 0.07
        discounted_amount = purchase_amount * (1 - discount)
        print(f"Сумма к оплате со скидкой 7%: {discounted_amount:.2f} руб.")

    else:
        print(f"Сумма к оплате без скидки: {purchase_amount:.2f} руб.")