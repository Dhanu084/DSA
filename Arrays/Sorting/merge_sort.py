#  Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as
#  merge sort always divides the array into two halves and takes linear time to merge two halves.

# Auxiliary Space: O(n)

def merge_sort(arr):
    return [] if len(arr) == 0 else merge_sort_array(arr, 0, len(arr)-1)


def merge_sort_array(arr, start, end):
    if start >= end:
        return [arr[start]]

    mid = start + (end-start)//2

    arr1 = merge_sort_array(arr, start, mid)
    arr2 = merge_sort_array(arr, mid+1, end)

    new_array = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(arr1) and right_idx < len(arr2):
        if arr1[left_idx] <= arr2[right_idx]:
            new_array.append(arr1[left_idx])
            left_idx += 1
        else:
            new_array.append(arr2[right_idx])
            right_idx += 1

    for k in range(left_idx, len(arr1)):
        new_array.append(arr1[k])
    for k in range(right_idx, len(arr2)):
        new_array.append(arr2[k])

    return new_array


arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))
print(merge_sort([1]))
print(merge_sort([]))
print(merge_sort([1, 0]))
print(merge_sort([2, 1, 0]))
print(merge_sort([7, 6, 5, 4, 3, 2, 1, -1, -2, -2, -2, -5]))
