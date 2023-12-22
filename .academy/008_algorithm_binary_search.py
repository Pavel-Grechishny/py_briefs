from random import choice


list_range = [*range(5000000, -1, -1)]
# list_range = [*range(5, 30, 3)]
list_range.sort()

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

    
