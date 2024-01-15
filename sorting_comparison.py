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


while True:
    try:
        size = int(input("Sorting will be run 100 times, for data collection. Pring the size of testing data:\n >>>"))
        array = get_random_array(size)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting gracefully.")
        break
    except:
        print ("Wrong input")
        continue

    timer_sorted = timeit.Timer(lambda: sorted(array))
    result_sorted = timer_sorted.timeit(number=100)

    timer_insertsort = timeit.Timer(lambda: insertion_sort(array))
    result_insertsort = timer_insertsort.timeit(number=100)

    timer_margesort = timeit.Timer(lambda:merge_sort(array))
    result_margesort = timer_margesort.timeit(number=100)

    print (f"Result of using Python base algo for sorting data take {result_sorted} seconds.")
    print (f"Result of using insert sort algo for sorting data take {result_insertsort} seconds.")
    print (f"Result of using merge sort algo for sorting data take {result_margesort} seconds.")

    if result_sorted < result_insertsort and result_sorted < result_margesort:
        print (f"\nPython base algo win with result: {round (result_sorted,6)} ")
    elif result_insertsort < result_margesort:
        print (f"Insert sort method algo win with result: {round (result_insertsort,6)} ")
    else:
        print (f"Merge sort method algo win with result: {round (result_margesort,6)} ")
    print ("\nYou can try again or Ctrl+C for out=)\n\n\n")


