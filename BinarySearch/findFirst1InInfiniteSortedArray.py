def binarySearch(arr, low, high):
    if arr[high] < 1:
        return binarySearch(arr, low, high + min(5, len(arr)-high-1))

    if low > high: return -1
    
    mid = low + (high - low)//2
    prev = mid - 1
    if prev>=0 and arr[prev] == 0 and arr[mid] == 1:
        return mid

    if arr[mid] < 1:
        return binarySearch(arr, mid + 1, high)
    elif prev >= 0 and arr[prev] == 1 and arr[mid] == 1:
        return binarySearch(arr, low, prev)
    else:
        return binarySearch(arr, low, prev)

arr = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]
print(binarySearch(arr, 0, 5))
print(binarySearch(arr, 0, len(arr)-1))
print(binarySearch(arr, 8, 10))
arr = [0,1,1,1,1,1,1]
print(binarySearch(arr, 0, 4))
print(binarySearch(arr, 1, 5))