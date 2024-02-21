try:
    fd = open("00.txt", encoding="utf8")
except FileNotFoundError:
    print("Файл не найден!")
    exit()

text = fd.read()
fd.close()
protokol, rest_url = text.split("://", 1)
print(protokol)
domain, rest_url = rest_url.split("/", 1)
print(domain)
search, rest_url = rest_url.split("?", 1)
print(search)
parameters = rest_url.split("&")

for parameter in parameters:
    name, value = parameter.split("=", 1)
    print(f"{name} = {value}")

try:
    with open("output.txt", "w", encoding="utf8") as output_file:
        output_file.write(f"Протокол: {protokol}\n")
        output_file.write(f"Доменное имя: {domain}\n")
        output_file.write(f"Запрос: {search}\n")
        output_file.write("Параметры:\n")
        for parameter in parameters:
            name, value = parameter.split("=", 1)
            output_file.write(f"   {name} = {value}\n")

except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Здесь нельзя создать файл")