import time
 
 
def bubble_sort(numbers):
    numbers = numbers.copy()
    length = len(numbers)
 
    for i in range(length - 1):
        for j in range(length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
 
    return numbers
 
 
def insertion_sort(numbers):
    numbers = numbers.copy()
 
    for i in range(1, len(numbers)):
        current_number = numbers[i]
        j = i - 1
 
        while j >= 0 and numbers[j] > current_number:
            numbers[j + 1] = numbers[j]
            j = j - 1
 
        numbers[j + 1] = current_number
 
    return numbers
 
 
def selection_sort(numbers):
    numbers = numbers.copy()
    length = len(numbers)
 
    for i in range(length - 1):
        smallest_index = i
 
        for j in range(i + 1, length):
            if numbers[j] < numbers[smallest_index]:
                smallest_index = j
 
        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]
 
    return numbers
 
 
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
 
    middle = len(numbers) // 2
    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])
 
    merged_list = []
    i = 0
    j = 0
 
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_list.append(left_half[i])
            i = i + 1
        else:
            merged_list.append(right_half[j])
            j = j + 1
 
    merged_list.extend(left_half[i:])
    merged_list.extend(right_half[j:])
 
    return merged_list
 
 
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
 
    pivot = numbers[len(numbers) // 2]
 
    smaller_numbers = []
    equal_numbers = []
    bigger_numbers = []
 
    for number in numbers:
        if number < pivot:
            smaller_numbers.append(number)
        elif number == pivot:
            equal_numbers.append(number)
        else:
            bigger_numbers.append(number)
 
    sorted_smaller = quick_sort(smaller_numbers)
    sorted_bigger = quick_sort(bigger_numbers)
 
    return sorted_smaller + equal_numbers + sorted_bigger
 
 
def measure_sort_time(sort_function, numbers):
    start_time = time.perf_counter()
    sort_function(numbers)
    end_time = time.perf_counter()
 
    seconds_taken = end_time - start_time
    milliseconds_taken = seconds_taken * 1000
    return milliseconds_taken
 
 
list_sizes_to_test = [100, 200, 300, 400, 500]
 
print("SORTING SPEED TEST - REVERSE SORTED NUMBERS")
print("==============================================")
print()
 
for size in list_sizes_to_test:
 
    reverse_numbers = list(range(size, 0, -1))
 
    print(f"Sorting a list of {size} REVERSE SORTED numbers:")
 
    time_taken = measure_sort_time(bubble_sort, reverse_numbers)
    print(f"   Bubble Sort:    {time_taken:.3f} ms")
 
    time_taken = measure_sort_time(insertion_sort, reverse_numbers)
    print(f"   Insertion Sort: {time_taken:.3f} ms")
 
    time_taken = measure_sort_time(selection_sort, reverse_numbers)
    print(f"   Selection Sort: {time_taken:.3f} ms")
 
    time_taken = measure_sort_time(merge_sort, reverse_numbers)
    print(f"   Merge Sort:     {time_taken:.3f} ms")
 
    time_taken = measure_sort_time(quick_sort, reverse_numbers)
    print(f"   Quick Sort:     {time_taken:.3f} ms")
 
    print()
 