def mergesort(array):
    return sort_helper(array)


def sort_helper(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = sort_helper(array[mid:])
        right = sort_helper(array[:mid])
        return merge(left, right)

    return array


def merge(left, right):
    left_index, right_index = 0, 0
    merged = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index = left_index + 1
        else:
            merged.append(right[right_index])
            right_index = right_index + 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index = left_index + 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index = right_index + 1

    return merged
