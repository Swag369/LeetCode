class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        nz = 0
        for i in nums:
            if i == 0:
                nz += 1
            else:
                total_prod *= i

        for i in range(len(nums)):
            if nz > 1:
                nums[i] = 0
            elif nz == 1:
                if nums[i] == 0:
                    nums[i] = total_prod
                else:
                    nums[i] = 0
            else:
                nums[i] = total_prod//nums[i]

        return nums