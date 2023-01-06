def binarySearch(arr, target):
    n = len(arr)
    left, right = 0, n-1

    while left <= right:
        mid = left + (right - left)//2
        prev = mid - 1
        next = mid + 1

        if arr[mid] == target:
            return mid
        
        if prev >= 0 and arr[prev] == target:
            return prev
        
        if mid + 1 < n and arr[next] == target:
            return next
        
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1


org = [3, 10, 20, 40, 50, 70, 80]
arr = [10, 3, 40, 20, 50, 80, 70]

for a in arr:
    print(binarySearch(arr, a))
