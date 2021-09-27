def heapify(arr, i, n):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[l]>arr[largest]:
        largest = l
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if largest!=i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,largest,n)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        print(arr)
        heapify(arr,i,n)
    print(arr)
    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,0,i)

# arr = [7, 6, 5, 4, 3, 2, 1, -1, -2, -2, -2, -5]
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)
