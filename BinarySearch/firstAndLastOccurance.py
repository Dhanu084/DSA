
def binarySearch(arr, target):
    n = len(arr)
    left, right = 0, n-1
    last_pos = -1

    while left <= right:
        mid = left + (right - left)//2
        next = (mid+1)%n
        # print(mid)
        if arr[mid] == target:
            last_pos = max(last_pos, mid)
        if arr[next] == target or arr[mid] <= target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return last_pos
        


arr = [1,1,2,2,2,3,3,4,5]
for i in set(arr):
    print(i, binarySearch(arr, i))
print(binarySearch(arr, 10))