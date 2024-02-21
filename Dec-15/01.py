
try:
    fd = open("01u.txt", encoding="utf8")
    emails = fd.read().splitlines()
except FileNotFoundError:
    print("Файл не найден")
    exit()

for email in emails:
    parts = email.split('@')
    if "@" in email and "." in parts[-1] and "." in parts[-2]:
        print(f"{email} - корректный адрес!")
    else:
        print(f"{email} - некорректный адрес!")

try:
    open("output2.txt", encoding="utf8")
except PermissionError:
    print("Здесь  нельзя создать файл")



