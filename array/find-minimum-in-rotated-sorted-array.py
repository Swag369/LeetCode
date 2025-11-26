class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we know first "part" is sorted
        # we know second "part" is sorted
        # do we have 2 parts? could have rotated into itself again
        # if we have 2 parts, then we know that there is some combo of max, min
        # we know that start of first run start is > end of second run

        if nums[-1] > nums[0]:
            return nums[0]

        l = 0
        r = len(nums)-1


        while l<r-1:

            i = (l+r)//2

            # is on first run or second run?
            
            if nums[i] < nums[l]: # i in second run, l in first
                r = i
            elif nums[i] > nums[r]: #i in first run, r in second
                l = i
        
            # we never have a situation where l and r in same run - it doesn't make sense
            # we want l to be max of 1st run and r to be min of 2nd run
        

        return nums[r]