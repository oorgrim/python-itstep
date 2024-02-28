import threading

def calculate_average(sub_list, result_list):
    average = sum(sub_list) / len(sub_list)
    result_list.append(average)

def parallel_average_calc(num_list, num_threads):
    sublist_size = len(num_list) // num_threads
    sublists = [num_list[i:i+sublist_size]
    for i in range(0, len(num_list), sublist_size)]

    result_list = []
    threads = []

    for sublist in sublists:
        thread = threading.Thread(target=calculate_average, args=(sublist, result_list))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_average = sum(result_list) / len(result_list)
    return total_average

if __name__ == "__main__":
    numbers = [17, 717, 11, 77, 19, 713, 72, 711, 137, 177]
    num_threads = 4
    average = parallel_average_calc(numbers, num_threads)
    print("Среднее значение:", average)
