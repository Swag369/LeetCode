class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1#preserves odd/even
            elif nums[m] >= target:
                # r = m-1 #switches odd/even
                r = m #switches odd/even

        
        if nums[l] >= target:
            return l
        else:
            return l+1
