class Solution:
    def twoSum(self, s: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(s) - 1

        while(l < r):

            if s[l] + s[r] > target:
                r -= 1
            elif s[l] + s[r] < target:
                l += 1
            else:
                return [l+1, r+1]