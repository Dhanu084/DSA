def binarySearch(arr, target):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


arr = [1,2,3,4,5,6,7]

for a in arr:
    print(a, binarySearch(arr, a))
print(binarySearch(arr, 10))