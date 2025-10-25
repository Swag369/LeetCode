class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        oldi = nums[0]-1

        for i in range(len(nums)):
        
            if nums[i] == oldi:
                continue
            else:
                oldi = nums[i]
        
            j = i+1
            k = len(nums)-1

            while (j < k):
                if nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    oldj = nums[j]
                    while j < k and nums[j] == oldj:
                        j += 1
                    
        return ans