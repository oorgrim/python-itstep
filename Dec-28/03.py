def find_local_extremes(temperatures):
    local_min = []
    local_max = []

    for i in range(1, len(temperatures) - 1):
        if temperatures[i] < temperatures[i - 1] and temperatures[i] < temperatures[i + 1]:
            local_min.append((i + 1, temperatures[i]))
        elif temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            local_max.append((i + 1, temperatures[i]))

    return local_min, local_max

temperatures = [20, 18, 22, 16, 25, 19, 21, 23, 17, 20]

local_min, local_max = find_local_extremes(temperatures)

print("Локальные минимумы:")
for day, temperature in local_min:
    print(f"день {day} - {temperature}°")

print("\nЛокальные максимумы:")
for day, temperature in local_max:
    print(f"день {day} - {temperature}°")

def test_find_local_extremes():
    temperatures = [10, 5, 8, 12, 6]
    local_min, local_max = find_local_extremes(temperatures)
    assert local_min == [(2, 5)]
    assert local_max == [(4, 12)]

    temperatures = [11, 11, 11, 11, 11] # одинаовые значения
    local_min, local_max = find_local_extremes(temperatures)
    assert local_min == []
    assert local_max == []
    
    print('Тест пройден')

test_find_local_extremes()