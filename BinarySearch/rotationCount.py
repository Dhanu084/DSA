def binarySearch(arr):
    n = len(arr)
    l, r = 0, n-1

    while l <= r:
        mid = l + (r - l)//2
        next = (mid + 1)%n
        prev = (mid-1+n)%n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        
        # search the sorted part
        if arr[mid] <= arr[l]:
            r = mid - 1
        else:
            l = mid + 1
       
    return 0

arr = [15, 18, 2, 3, 6, 12]

# print(binarySearch(arr))
# print(binarySearch([1,2,3,4,5]))
# print(binarySearch([4,1,2,3]))
print(binarySearch([3,4,5,1,2]))