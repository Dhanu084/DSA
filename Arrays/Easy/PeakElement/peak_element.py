class Solution:
    # O(n) T and O(n) S
    # def peak_element(self, arr, n):
    #     if n == 0:
    #         return 0

    #     if arr[0] >= arr[1]:
    #         return 0

    #     for i in range(1, n-1):
    #         if arr[i] > arr[i+1] and arr[i] < arr[i-1]:
    #             return i

    #     return n-1

    # O(log n) T and O(n) space
    def peak_element(self, arr, n):
        if n == 0:
            return 0

        return self.peak(arr, 0, n-1)

    def peak(self, arr, low, high):

        mid = low+(high-low)//2

        if ((mid == 0 or arr[mid] >= arr[mid-1]) and (mid == high or arr[mid] >= arr[mid+1])):
            return mid

        elif mid > 0 and arr[mid-1] > arr[mid]:
            return self.peak(arr, low, mid-1)
        else:
            return self.peak(arr, mid+1, high)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.peak_element([1, 13], 2)
    print(ans)
