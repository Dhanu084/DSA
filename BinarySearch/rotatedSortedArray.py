def binarySearch(arr, target):
    n = len(arr)
    left, right = 0, n-1

    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        
        if arr[mid] >= arr[left]:
            if arr[left] <= target and arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= target and arr[right] >= target:
                left = mid + 1
            else:
                right = mid - 1 

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]

for a in arr:
    print(binarySearch(arr, a))