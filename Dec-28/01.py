def list_nums(numbers):
    if not numbers:
        return 0

    current_length = 1
    max_length = 1

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            current_length += 1
        else:
            current_length = 1
            
        max_length = max(max_length, current_length)
    return max_length

def test_list_nums():
    assert list_nums([1, 2, 3, 2, 3, 4, 5]) == 4
    assert list_nums([1, 2, 3, 2, 5, 6, 7, 8]) == 5
    assert list_nums([1, 1, 2, 3, 4, 4, 5]) == 7
    assert list_nums([5, 4, 3, 2, 1]) == 1
    assert list_nums([]) == 0
    print("Тест пройден")

test_list_nums()