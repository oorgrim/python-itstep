import time

def measuretime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() #засечь время выполненяи ф-ии
        result = func(*args, **kwargs)
        end_time = time.time() #время заверш-я
        passed_ms = (end_time - start_time) * 1000
        print(f"Время: {passed_ms:.2f} мс")
        return result
    return wrapper

@measuretime
def test_func():
    total_sum = sum(range(1*2))
    print("Сумма чисел в цикле:", total_sum)

test_func()