class Solution:
    def missingNumber(self, nums) -> int:
        missing_number = -1
        i = 0
        
        while i<len(nums):
            current_number = nums[i]
            if current_number != i+1 and current_number!=0:
                nums[i],nums[current_number-1] = nums[current_number-1],nums[i]
            else:
                i+=1
        print(nums)

        i = 1
        for num in nums:
            if num != i:
                return i
            i+=1
        
        return missing_number
            
sol = Solution()
ans = sol.missingNumber([9,6,4,2,3,5,7,0,1])
print(ans)

ans = sol.missingNumber([9,6,4,2,3,5,7,8,1])
print(ans)

ans = sol.missingNumber([0,2,3])
print(ans)