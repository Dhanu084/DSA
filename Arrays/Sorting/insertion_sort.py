# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)-1):
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
def recursive_insertion_sort(arr, index=1):
    if index >= len(arr):
        return arr

    key = arr[index]
    j = index - 1

    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

    return recursive_insertion_sort(arr, index+1)


arr = [64, 34, 25, 12, 22, 11, 90]
# 34 64 25 12 22 11 90
# 25 34 64 12 22 11 90
# 12 25 34 64 22 11 90
# 12 22 25 34 64 11 90
# 11 12 22 25 34 64 90


# print(insertion_sort(arr))
print(recursive_insertion_sort(arr))
