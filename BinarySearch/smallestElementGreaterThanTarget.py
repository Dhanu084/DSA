from typing import List
def nextGreatestLetter(letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n-1
        res = 'z'

        while left <= right:
            mid = left + (right - left)//2

            if letters[mid] == target:
                found = True
            
            if letters[mid] > target:
                res = min(res, letters[mid])
            
            if target < letters[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return res if letters[-1] > target else letters[0]

print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["x","x","y","y"], "z"))
print(nextGreatestLetter(["a", "b"], "b"))