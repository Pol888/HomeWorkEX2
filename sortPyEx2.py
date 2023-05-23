



#for i in range(len(array) - 1):  # сортировка выбором
#    min_element = i
#    for j in range(i + 1, len(array)):
#         if array[min_element] > array[j]:
#             min_element = j
#    if array[min_element] < array[i]:
#        array[min_element], array[i] = array[i], array[min_element]
#print(array)
#
#
#
#
#for i in range(len(array) - 1):  # сортировка вставками
#    for j in range(i + 1, len(array)):
#         if array[i] > array[j]:
#             array[i], array[j] = array[j], array[i]
#
#
#print(array)



#def q_sort (arr, start, end):
#    left = start
#    rigth = end
#    pivot = arr[(start + end) // 2]
#
#    while left <= rigth:
#        while arr[left] < pivot:
#            left += 1
#        while arr[rigth] > pivot:
#            rigth -= 1
#        if left <= rigth:
#            if left < rigth:
#                arr[left], arr[rigth] = arr[rigth], arr[left]
#            left += 1
#            rigth -= 1
#    if left < end:
#        q_sort(arr, left, end)
#    if rigth > start:
#        q_sort(arr, start, rigth)
#
#q_sort(array, 0, len(array) - 1)
#
#print(array)

# [1, 1, 2, 4, 5, 5, 6, 8]  [1, 1, 1, 2, 4, 5, 5, 6, 7, 8]

#def bionary_search(arr: list, desired, end, start=0):   # бинарный поиск
#    if end <= start:
#        return -1
#    center = (start + end) // 2
#    if arr[center] < desired:
#        return bionary_search(arr, desired, len(arr), center)
#    elif arr[center] > desired:
#        return bionary_search(arr, desired, center)
#    else:
#        return center
#
#array.sort()
#print(bionary_search(array, 3, len(array)))
        #0  1  2  3  4  5  6  7  8  9  10

import random

list_array = [random.randint(1, 100) for _ in range(41)]
def heap_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        building_an_ideal_heap(arr, 0, i)
    return arr

def building_an_ideal_heap (array, i, end):
    if (array[2 * i + 1] == array[2 * i + 2]) and array[2 * i + 2] > array[i] and 2 * i + 1 < end:
        array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
        if 2 * i + 1 <= (len(array) // 2) - 1:
            return building_an_ideal_heap(array, 2 * i + 1, end)
    elif array[2 * i + 1] > array[i] and array[2 * i + 1] > array[2 * i + 2] and 2 * i + 1 < end:
        array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
        if 2 * i + 1 <= (len(array) // 2) - 1:
            return building_an_ideal_heap(array, 2 * i + 1, end)
    elif array[2 * i + 2] > array[i] and array[2 * i + 2] > array[2 * i + 1] and 2 * i + 2 < end:
        array[i], array[2 * i + 2] = array[2 * i + 2], array[i]
        if 2 * i + 2 <= (len(array) // 2) - 1:
            return building_an_ideal_heap(array, 2 * i + 2, end)
    else:
        return array

def sequential_initialization(array, i):
    if (array[2 * i + 1] == array[2 * i + 2]) and array[2 * i + 2] > array[i]:
        array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
        if 2 * i + 1 <= (len(array) // 2) - 1:
            return sequential_initialization(array, 2 * i + 1)
    elif array[2 * i + 1] > array[i] and array[2 * i + 1] > array[2 * i + 2]:
        array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
        if 2 * i + 1 <= (len(array) // 2) - 1:
            return sequential_initialization(array, 2 * i + 1)
    elif array[2 * i + 2] > array[i] and array[2 * i + 2] > array[2 * i + 1]:
        array[i], array[2 * i + 2] = array[2 * i + 2], array[i]
        if 2 * i + 2 <= (len(array) // 2) - 1:
            return sequential_initialization(array, 2 * i + 2)
    else:
        return array

def initial_heap(array):
    for i in range((len(array) // 2) - 1, -1, -1):
        if array[i] > array[2 * i + 1] and array[i] > array[2 * i + 2]:
            continue
        elif (array[2 * i + 1] == array[2 * i + 2]) and array[2 * i + 2] > array[i]:
            array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
            if 2 * i + 1 <= (len(array) // 2) - 1:
                return sequential_initialization(array, 2 * i + 1)
        elif array[2 * i + 1] > array[i] and array[2 * i + 1] > array[2 * i + 2]:
            array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
            if 2 * i + 1 <= (len(array) // 2) - 1:
                sequential_initialization(array, 2 * i + 1)
        elif array[2 * i + 2] > array[i] and array[2 * i + 2] > array[2 * i + 1]:
            array[i], array[2 * i + 2] = array[2 * i + 2], array[i]
            if 2 * i + 2 <= (len(array) // 2) - 1:
                sequential_initialization(array, 2 * i + 2)
    return array


print(f'Изначальный массив: {list_array}')
print(f'Отсортированный: ', heap_sort(initial_heap(list_array)))




