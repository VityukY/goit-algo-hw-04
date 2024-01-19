# зберегти рези у файл
# зберегти рези у файл
import random
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def get_random_array(amount=100000):
    test_array = [random.randint(1, 100) for _ in range(amount)]
    return test_array

def test_sorting_algorithm(algorithm, data):
    def sort_data():
        return algorithm(data.copy())
    return timeit.timeit(sort_data, number=1)

small_array = get_random_array (100)
medium_array = get_random_array (1000)
large_array = get_random_array (10000)

small_result_merge = test_sorting_algorithm(merge_sort, small_array)
small_result_inseert = test_sorting_algorithm(insertion_sort, small_array)
small_result_defult = test_sorting_algorithm(sorted, small_array)
medium_array_merge = test_sorting_algorithm(merge_sort, medium_array)
medium_array_inseert = test_sorting_algorithm(insertion_sort, medium_array)
medium_array_defult = test_sorting_algorithm(sorted, medium_array)
large_array_merge = test_sorting_algorithm(merge_sort, large_array)
large_array_inseert = test_sorting_algorithm(insertion_sort, large_array)
large_array_defult = test_sorting_algorithm(sorted, large_array)

with open("readme.md", 'w') as fp:
    small_data_result = f'Data size: small.\nMerge method time result {small_result_merge}\nInsert method time result {small_result_inseert}\nDefault method time result {small_result_defult}\n\n'
    fp.writelines (small_data_result)
    medium_mall_data_result = f'Data size: medium.\nMerge method time result {medium_array_merge}\nInsert method time result {medium_array_inseert}\nDefault method time result {medium_array_defult}\n\n'
    fp.writelines (medium_mall_data_result)
    large_data_result = f'Data size: large.\nMerge method time result {large_array_merge}\nInsert method time result {large_array_inseert}\nDefault method time result {large_array_defult}\n\n'
    fp.writelines (large_data_result)