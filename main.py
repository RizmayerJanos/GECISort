def occurrence_table(arr):
    occurrences = {}
    for element in arr:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += 1
    return occurrences

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def worst_sort(arr):
    original = occurrence_table(arr)
    for sorted_arr in list(worst_sort_recursive(arr, len(arr))):
        if is_sorted(sorted_arr):
            if occurrence_table(sorted_arr) == original:
                return sorted_arr
    return None

def worst_sort_recursive(arr, j):
    if j == 0:
        yield []
    else:
        for elem in arr:
            for partial in worst_sort_recursive(arr, j - 1):
                yield [elem] + partial


print("Input the desired list of numbers: ")
input_arr = [int(i) for i in input().split()]


print(worst_sort(input_arr))

