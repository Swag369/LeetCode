class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        self.sums = [0]*len(nums)
        self.sums[0] = nums[0]
        # print(self.nums)
        for i in range(1, len(self.nums)):
            self.sums[i] = self.sums[i-1] + nums[i]
        # print(self.sums)



    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)