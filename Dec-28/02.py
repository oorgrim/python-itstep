def find_same_surnames(names):
    surname_dict = {}

    for full_name in names:
        first_name, surname = full_name.split()
        if surname in surname_dict:
            surname_dict[surname].append(full_name)
        else:
            surname_dict[surname] = [full_name]

    return surname_dict

names_list = ["Юнона Иванова", "Милена Симонова", "Анастасия Иванова", "Дэниел Кан", "Милена Симонова"]
result_dict = find_same_surnames(names_list)
def test_find_same_surnames():
    assert result_dict.get("Иванова") == ["Юнона Иванова", "Анастасия Иванова"]
    assert result_dict.get("Симонова") == ["Милена Симонова", "Милена Симонова"]
    assert result_dict.get("Кан") == ["Дэниел Кан"]
    assert result_dict.get("Ибраев") is None
    print("Тест пройден")

test_find_same_surnames()