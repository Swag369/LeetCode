class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ret = 0

        nums = set(nums)
        for n in nums:
            if n-1 in nums:
                continue
            
            a = 1
            while n+1 in nums:
                n = n+1
                a += 1
            
            ret = max(ret, a)
        
        return ret