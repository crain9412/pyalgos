def quicksort(array):
    sort_helper(array, 0, len(array) - 1)


def sort_helper(array, first_index, last_index):
    if first_index < last_index:
        pivot_index = partition(array, first_index, last_index)
        sort_helper(array, first_index, pivot_index - 1)
        sort_helper(array, pivot_index + 1, last_index)


def partition(array, first_index, last_index):
    mid_index = (first_index + last_index) // 2
    i = first_index
    store_index = first_index
    pivot = array[mid_index]

    swap(array, mid_index, last_index)

    while i < last_index:
        if array[i] < pivot:
            swap(array, i, store_index)
            store_index = store_index + 1
        i = i + 1

    swap(array, last_index, store_index)
    return store_index


def swap(array, i, j):
    if i == j: return
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
