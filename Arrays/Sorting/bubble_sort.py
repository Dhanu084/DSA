
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# O(n^2) T and O(1) S
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# O(n^2) T and O(n) S

def bubble_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return bubble_sort_recursive(arr[0:-1])+[arr[-1]]


def bubble_sort_recursive1(arr, index):
    if index < 0:
        return arr

    for i in range(0, index):
        if(arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return bubble_sort_recursive1(arr, index-1)


arr = [64, 34, 25, 12, 22, 90, 11]
print(bubble_sort_recursive1(arr, len(arr)-1))
