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




