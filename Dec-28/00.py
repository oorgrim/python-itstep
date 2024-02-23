def get_count_of_emoji(count_emoji):
    emoji = "😊"
    return  emoji * count_emoji

try:
    user_input = input('Сколько вы хотите смайликов? ')
    count_emoji = int(user_input)
    result = get_count_of_emoji(count_emoji)
    print(result)

except ValueError:
    print("Ведите целое число")

def test_get_count_of_emoji():
    assert result.count("😊") == count_emoji
    print("Тест пройден")

test_get_count_of_emoji() 

#VN: 1. Cначала должен запускаться тест, а потом вся остальная логика (строки 5 - 12). Это относится ко всем задачам
#    2. В блоке try много лишнего!