def binarySearch(arr, target, low, high):
    if arr[high] < target:
        return binarySearch(arr, target, low, high + min(5, len(arr)-high-1))

    if low > high: return -1
    
    mid = low + (high - low)//2
    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binarySearch(arr, target, mid + 1, high)
    else:
        return binarySearch(arr, target, low, mid - 1)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(binarySearch(arr,2,0,7))
print(binarySearch(arr, 1, 0, 7))
print(binarySearch(arr,7,0,7))
print(binarySearch(arr, 15, 0, 7))
print(binarySearch(arr,14,0,10))
print(binarySearch(arr, 12, 0, 4))
print(binarySearch(arr,0,0,7))