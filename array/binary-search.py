class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            halfindex = (l+r)//2
            half = nums[halfindex]
            if half < target:
                l = halfindex + 1
                print("moving up")
            elif half > target:
                r = halfindex -1
                print("moving down")
            else:
                return halfindex
            print(l, r, halfindex, half)
        return -1