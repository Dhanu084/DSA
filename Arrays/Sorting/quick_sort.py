# Worst Case : O(n)
# Best and Average Case : O(n)

def partition(arr, low, high):
    pivot_index = low

    while low<high:
        while low<len(arr) and arr[low]<=arr[pivot_index]:
            low+=1
        
        while arr[high]>arr[pivot_index]:
            high-=1

        if low<high:
            arr[low],arr[high] = arr[high],arr[low]
    arr[high],arr[pivot_index] = arr[pivot_index],arr[high]
    return high


def quick_sort(arr, low, high):
    if low > high:
        return

    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot-1)
    quick_sort(arr, pivot+1, high)


def quick_sort_fun(arr):
    if len(arr) <= 1:
        return arr
    quick_sort(arr, 0, len(arr)-1)


arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_fun(arr)
print(arr)
arr = [3, 2, 1]
quick_sort_fun(arr)
print(arr)

arr = [7, 6, 5, 4, 3, 2, 1, -1, -2, -2, -2, -5]
quick_sort_fun(arr)
print(arr)

arr = [7]
quick_sort_fun(arr)
print(arr)

arr = [-1, -100]
quick_sort_fun(arr)
print(arr)

arr = []
quick_sort_fun(arr)
print(arr)
