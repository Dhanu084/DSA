# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

# O(n) T and O(1) S
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [4, 8, 9, 0, 121, 5, 67, 4, 8]
selection_sort(arr)
print(arr)
