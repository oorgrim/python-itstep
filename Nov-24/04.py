
user_data = input("Введите количество USD: ")
try:
    usd_amount = float(user_data)
except ValueError:
    print("Введите в числах!")
else:
    current = input("Выберите валюту для конвертации (EUR, UAN, AZN): ")
    
    usd_to_eur= 0.91
    usd_to_uan = 7.15
    usd_to_azn = 1.7
    
    if current == "EUR" or current == "eur":
        result = usd_amount * usd_to_eur
        print(usd_amount, "USD равно", result, "EUR")
    elif current == "UAN" or current == "uan":
        result = usd_amount * usd_to_uan
        print(usd_amount, "USD равно", result, "UAN")
    elif current  == "AZN" or current == "azn":
        result = usd_amount * usd_to_azn
        print(usd_amount, "USD равно",  result, "AZN")
    else:
        print("Извините, выбранная валюта недоступна")