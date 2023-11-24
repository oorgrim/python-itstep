user_data = input("Введите числа от 0 до 9: ")
match user_data:
    case "0":
        print(")")
    case "1":
        print("!")
    case "2":
        print("@")
    case "3":
        print("#")
    case "4":
        print("$")
    case "5":
        print("%")
    case "6":
        print("^")
    case "7":
        print("&")
    case "8":
        print("*")
    case "9":
        print("(")
    case _:
        print("На данной кнопке нет числа")