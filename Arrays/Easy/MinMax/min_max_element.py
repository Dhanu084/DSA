class Solution:
    def __init__(self) -> None:
        self.min = 10 ^ 12
        self.max = 0

    def min_max(self, array):
        for ele in array:
            if ele > self.max:
                self.max = ele
            if ele < self.min:
                self.min = ele
        return (self.min, self.max)


if __name__ == "__main__":
    sol = Solution()
    ans = sol.min_max([1, 4, 5, 6, -1, 10])
    print(ans)
