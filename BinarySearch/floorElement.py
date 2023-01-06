#  Floor of an element in Binary search

def binarySearch(arr, target):
    n = len(arr)
    left, right = 0, n-1
    res = -1

    while left <= right:
        mid = left + (right - left) // n
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            res = max(res, arr[mid])
        
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return res

print(binarySearch([1, 2, 8, 10, 10, 12, 19], 5))
print(binarySearch([1, 2, 8, 10, 10, 12, 19], 20))
print(binarySearch([2,3,4,5], 1))