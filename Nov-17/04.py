
user_data1 = input("Введите часы: ")
user_data2 = input("Введите минуты: ")

hours = int(user_data1)
minutes = int(user_data2)

left = (24 - hours - 1) *60 + (60 - minutes)
hours_left = left // 60
minutes_left = left % 60

print("До следующего дня осталось", hours_left, "часов и", minutes_left, "минут")