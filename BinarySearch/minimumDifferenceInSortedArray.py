from math import inf
def binarySearch(arr, key):
    n = len(arr)
    low, high = 0, n-1
    minDiff = inf

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == key:
            return 0
        minDiff = min(minDiff, abs(key - arr[mid]))
        
        if arr[mid] > key:
            high = mid -1 
        else:
            low = mid + 1

    return minDiff


print(binarySearch([1,2,3,4,5], 7))
print(binarySearch([4,6,10], 7))
print(binarySearch([4,6,7, 10], 7))
print(binarySearch([4,6,8,10], 7))
print(binarySearch([1,3,8,10,15], 12))